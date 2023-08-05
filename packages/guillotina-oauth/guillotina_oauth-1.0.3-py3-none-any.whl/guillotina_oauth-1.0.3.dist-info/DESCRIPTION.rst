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
    "oauth_settings": {
        "server": "http://localhost/",
        "jwt_secret": "secret",
        "jwt_algorithm": "HS256",
        "client_id": 11,
        "client_password": "secret"
    }
}


Installation on a site
----------------------

POST SITE_URL/@install

{
	'pluggins': [
		'guillotina.googleoauth'
	]
}

Uninstall on a site
-------------------

POST SITE_URL/@uninstall

{
	'pluggins': [
		'guillotina.googleoauth'
	]
}


Events
------

guillotina.auth.events.NewUserLogin

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


