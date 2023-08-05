# -*- coding: utf-8 -*-
from aiohttp.web_exceptions import HTTPUnauthorized
from calendar import timegm
from datetime import datetime
from guillotina import app_settings
from guillotina import configure
from guillotina.api.content import DefaultOPTIONS
from guillotina.api.service import Service
from guillotina.async import IAsyncUtility
from guillotina.auth.users import GuillotinaUser
from guillotina.browser import Response
from guillotina.component import getUtility
from guillotina.interfaces import Allow
from guillotina.interfaces import IContainer
from guillotina.exceptions import Unauthorized

import aiohttp
import asyncio
import jwt
import logging
import time


logger = logging.getLogger('guillotina_oauth')

# Asyncio Utility
NON_IAT_VERIFY = {
    'verify_iat': False,
}


class IOAuth(IAsyncUtility):
    """Marker interface for OAuth Utility."""

    pass


REST_API = {
    'getAuthCode': ['POST', 'get_authorization_code', True],
    'getAuthToken': ['POST', 'get_auth_token', True],
    'getServiceToken': ['POST', 'get_service_token', True],
    'searchUser': ['POST', 'search_user', False],
    'validToken': ['POST', 'valid_token', True],
    'getUser': ['POST', 'get_user', False],
    'getGroup': ['POST', 'get_group', False],
    'getScopeUsers': ['POST', 'get_users', False],
    'getScopes': ['GET', 'get_scopes', False],
    'grantGlobalRoles': ['POST', 'grant_scope_roles', False],
    'revokeGlobalRoles': ['POST', 'deny_scope_roles', False],
    'searchUsers': ['POST', 'search_user', False]
}


@configure.utility(provides=IOAuth)
class OAuth(object):
    """Object implementing OAuth Utility."""

    def __init__(self, settings=None, loop=None):
        self.loop = loop

    @property
    def configured(self):
        return 'oauth_settings' in app_settings

    @property
    def server(self):
        return app_settings['oauth_settings']['server']

    @property
    def client_id(self):
        return app_settings['oauth_settings']['client_id']

    @property
    def client_password(self):
        return app_settings['oauth_settings']['client_password']

    async def initialize(self, app=None):
        self.app = app
        self._service_token = None
        if 'oauth_settings' not in app_settings:
            logger.warn('No oauth settings found, oauth will not function')
            return

        while True:
            logger.debug('Renew token')
            now = timegm(datetime.utcnow().utctimetuple())
            await self.service_token
            expiration = self._service_token['exp']
            time_to_sleep = expiration - now
            await asyncio.sleep(time_to_sleep)

    async def finalize(self, app=None):
        pass

    async def auth_code(self, scope, client_id):
        result = await self.call_auth('getAuthCode', {
            'client_id': client_id,
            'service_token': await self.service_token,
            'scopes': scope,
            'response_type': 'code'
        })
        if result:
            return result['auth_code']
        return None

    @property
    async def service_token(self):
        if self._service_token:
            now = timegm(datetime.utcnow().utctimetuple())
            if self._service_token['exp'] > now:
                return self._service_token['service_token']
        logger.info('SERVICE TOKEN OBTAIN')
        result = await self.call_auth('getServiceToken', {
            'client_id': self.client_id,
            'client_secret': self.client_password,
            'grant_type': 'service'
        })
        if result:
            self._service_token = result
            return self._service_token['service_token']
        return None

    async def getUsers(self, request):
        scope = request.container.id
        header = {
            'Authorization': request.headers['Authorization']
        }

        result = await self.call_auth(
            'getScopeUsers',
            params={
                'service_token': self._service_token['service_token'],
                'scope': scope
            },
            headers=header
        )
        return result

    async def searchUsers(self, request, page=0, num_x_page=30, term=''):
        scope = request.container.id
        header = {
            'Authorization': request.headers['Authorization']
        }

        payload = {
            'criteria': '{"mail": "' + term + '*"}',
            'exact_match': False,
            'attrs': '["mail"]',
            'page': page,
            'num_x_page': num_x_page,
            'service_token': self._service_token['service_token'],
            'scope': scope
        }
        result = await self.call_auth(
            'searchUsers',
            params=payload,
            headers=header
        )
        return result

    async def validate_token(self, request, token):
        scope = request.container.id
        result = await self.call_auth(
            'validToken',
            params={
                'code': self._service_token['service_token'],
                'token': token,
                'scope': scope
            }
        )
        if result:
            if 'user' in result:
                return result['user']
            else:
                return None
        return None

    async def call_auth(self, call, params, headers={}, future=None, **kw):
        method, url, needs_decode = REST_API[call]

        result = None
        with aiohttp.ClientSession() as session:
            if method == 'GET':
                logger.debug('GET ' + self.server + url)
                async with session.get(
                        self.server + url,
                        params=params,
                        headers=headers,
                        timeout=30) as resp:
                    if resp.status == 200:
                        try:
                            result = jwt.decode(
                                await resp.text(),
                                app_settings['jwt']['secret'],
                                algorithms=[app_settings['jwt']['algorithm']])
                        except jwt.InvalidIssuedAtError:
                            logger.error('Error on Time at OAuth Server')
                            result = jwt.decode(
                                await resp.text(),
                                app_settings['jwt']['secret'],
                                algorithms=[app_settings['jwt']['algorithm']],
                                options=NON_IAT_VERIFY)
                    else:
                        logger.error(
                            'OAUTH SERVER ERROR %d %s' % (
                                resp.status,
                                await resp.text()))
                    await resp.release()
            elif method == 'POST':
                logger.debug('POST ' + self.server + url)
                async with session.post(
                        self.server + url,
                        data=params,
                        headers=headers,
                        timeout=30) as resp:
                    if resp.status == 200:
                        if needs_decode:
                            try:
                                result = jwt.decode(
                                    await resp.text(),
                                    app_settings['jwt']['secret'],
                                    algorithms=[app_settings['jwt']['algorithm']])
                            except jwt.InvalidIssuedAtError:
                                logger.error('Error on Time at OAuth Server')
                                result = jwt.decode(
                                    await resp.text(),
                                    app_settings['jwt']['secret'],
                                    algorithms=[app_settings['jwt']['algorithm']],
                                    options=NON_IAT_VERIFY)
                        else:
                            result = await resp.json()
                    else:
                        logger.error(
                            'OAUTH SERVER ERROR %d %s' % (
                                resp.status,
                                await resp.text()))
                    await resp.release()
            session.close()
        if future is not None:
            future.set_result(result)
        else:
            return result


class OAuthJWTValidator(object):

    for_validators = ('bearer',)

    def __init__(self, request):
        self.request = request

    async def validate(self, token):
        """Return the user from the token."""
        if token.get('type') != 'bearer':
            return None

        if '.' not in token.get('token', ''):
            # quick way to check if actually might be jwt
            return None

        try:
            try:
                validated_jwt = jwt.decode(
                    token['token'],
                    app_settings['jwt']['secret'],
                    algorithms=[app_settings['jwt']['algorithm']])
            except jwt.exceptions.ExpiredSignatureError:
                logger.warn("Token Expired")
                raise HTTPUnauthorized()
            except jwt.InvalidIssuedAtError:
                logger.warn("Back to the future")
                validated_jwt = jwt.decode(
                    token['token'],
                    app_settings['jwt']['secret'],
                    algorithms=[app_settings['jwt']['algorithm']],
                    options=NON_IAT_VERIFY)

            token['id'] = validated_jwt['login']

            oauth_utility = getUtility(IOAuth)

            # Enable extra validation
            # validation = await oauth_utility.validate_token(
            #    self.request, validated_jwt['token'])
            # if validation is not None and \
            #        validation == validated_jwt['login']:
            #    # We validate that the actual token belongs to the same
            #    # as the user on oauth

            scope = self.request._container_id if hasattr(self.request, '_container_id') else 'root'
            t1 = time.time()
            result = await oauth_utility.call_auth(
                'getUser',
                params={
                    'service_token': await oauth_utility.service_token,
                    # 'user_token': validated_jwt['token'],
                    'scope': scope,
                    'user': validated_jwt['login']
                },
                headers={
                    'Authorization': 'Bearer ' + token['token']
                }
            )
            tdif = t1 - time.time()
            logger.info('Time OAUTH %f' % tdif)
            if result:
                try:
                    user = OAuthGuillotinaUser(self.request, result)
                except Unauthorized:
                    return None

                user.name = validated_jwt['name']
                user.token = validated_jwt['token']
                if user and user.id == token['id']:
                    return user

        except jwt.exceptions.DecodeError:
            pass

        return None


class OAuthGuillotinaUser(GuillotinaUser):

    def __init__(self, request, data):
        super(OAuthGuillotinaUser, self).__init__(request)
        self._init_data(data)
        self._properties = {}

    def _init_data(self, user_data):
        self._roles = {}
        for key in user_data['roles']:
            self._roles[key] = Allow
        self._groups = [key for key
                        in user_data['groups']]
        self.id = user_data['mail']
        if len(self._roles) == 0:
            logger.error('User without roles in this scope')
            raise Unauthorized('Guillotina OAuth User has no roles in this Scope')


@configure.service(context=IContainer, name='@oauthgetcode', method='GET',
                   permission='guillotina.GetOAuthGrant')
class GetCredentials(Service):

    __allow_access__ = True

    async def __call__(self):
        oauth_utility = getUtility(IOAuth)
        if 'client_id' in self.request.GET:
            client_id = self.request.GET['client_id']
        else:
            client_id = oauth_utility.client_id

        if hasattr(self.request, '_container_id'):
            scope = self.request._container_id
        else:
            scope = self.request.GET['scope']

        result = await oauth_utility.auth_code([scope], client_id)
        return {
            'auth_code': result
        }


@configure.service(context=IContainer, name='@oauthgetcode', method='OPTIONS',
                   permission='guillotina.GetOAuthGrant')
class OptionsGetCredentials(DefaultOPTIONS):

    async def __call__(self):
        headers = {}
        allowed_headers = ['Content-Type'] + app_settings['cors']['allow_headers']
        headers['Access-Control-Allow-Headers'] = ','.join(allowed_headers)
        headers['Access-Control-Allow-Methods'] = ','.join(
            app_settings['cors']['allow_methods'])
        headers['Access-Control-Max-Age'] = str(app_settings['cors']['max_age'])
        headers['Access-Control-Allow-Origin'] = ','.join(
            app_settings['cors']['allow_origin'])
        headers['Access-Control-Allow-Credentials'] = 'True'
        headers['Access-Control-Expose-Headers'] = \
            ', '.join(app_settings['cors']['allow_headers'])

        oauth_utility = getUtility(IOAuth)
        if 'client_id' in self.request.GET:
            client_id = self.request.GET['client_id']
        else:
            client_id = oauth_utility.client_id

        if hasattr(self.request, '_container_id'):
            scope = self.request._container_id
        else:
            scope = self.request.GET['scope']

        result = await oauth_utility.auth_code([scope], client_id)
        resp = {
            'auth_code': result
        }
        return Response(response=resp, headers=headers, status=200)
