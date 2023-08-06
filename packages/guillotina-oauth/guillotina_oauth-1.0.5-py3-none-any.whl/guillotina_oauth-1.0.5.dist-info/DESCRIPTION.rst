.. contents::

GUILLOTINA_OAUTH
================


Features
--------

 * There is no persistence information about the user

 * The configuration is global for all application


Configuration
-------------

Generic global configuration on guillotina utilities section:

{
    "applicatoins": ["guillotina_oauth"],
    "auth_token_validators": [
        "guillotina.auth.validators.SaltedHashPasswordValidator",
        "guillotina_oauth.oauth.OAuthJWTValidator"
    ],
    "oauth_settings": {
        "server": "http://localhost/",
        "jwt_secret": "secret",
        "jwt_algorithm": "HS256",
        "client_id": 11,
        "client_password": "secret"
    }
}

1.0.5 (2017-07-24)
------------------

- @oauthgetcode now works on application root as well as container
  [vangheem]


1.0.4 (2017-06-25)
------------------

- User id on oauth may not be mail
  [bloodbare]

1.0.3 (2017-06-16)
------------------

- Handle oauth errors on connecting to invalid server
  [vangheem]


1.0.2 (2017-06-16)
------------------

- Handle errors when no config is provided
  [vangheem]


1.0.1 (2017-06-15)
------------------

- Do not raise KeyError if user is not found, raise Unauthorized
  [vangheem]


1.0.0 (2017-04-24)
------------------

- initial release


