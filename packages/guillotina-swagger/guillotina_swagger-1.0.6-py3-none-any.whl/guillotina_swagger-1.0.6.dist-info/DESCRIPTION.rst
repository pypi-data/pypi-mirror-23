Introduction
============

A `guillotina` application to automatically generate swagger interfaces for
APIs defined with `guillotina`.


Configuration
-------------

Available config.json options::

    {
        "swagger": {
            "authentication_allowed": false,
            "base_configuration": {
                "swagger": "2.0",
                "info": {
                    "version": "",
                    "title": "Guillotina",
                    "description": "The REST Resource API"
                },
                "host": "",
                "basePath": "",
                "schemes": [],
                "produces": [
                    "application/json"
                ],
                "consumes": [
                    "application/json"
                ],
                "paths": {},
                "definitions": {}
            }
        }
    }


Viewing swagger for resource
----------------------------

Append `@docs` onto any url: `http://localhost:8080/@docs`.

1.0.6 (2017-06-18)
------------------

- Automatically detect auth tokens and be able to provide own authorization header
  [vangheem]


1.0.5 (2017-06-13)
------------------

- Also pull basePath for swagger from vhm if provided
  [vangheem]


1.0.4 (2017-06-13)
------------------

- Use vhm for host setting on swagger
  [vangheem]


1.0.3 (2017-06-13)
------------------

- Pay attention to vhm


1.0.2 (2017-06-12)
------------------

- be able to provide custom base_url for swagger
  [vangheem]


1.0.1 (2017-06-07)
------------------

- Fix getting path of resource


1.0.0 (2017-04-04)
------------------

- initial release


