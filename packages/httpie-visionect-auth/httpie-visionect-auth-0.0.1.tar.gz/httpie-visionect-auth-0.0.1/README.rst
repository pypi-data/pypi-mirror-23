httpie-visionect-auth
=====================

`HMAC for JoanAssistant <https://api.visionect.com/>`_ auth plugin for `HTTPie <https://github.com/jkbr/httpie>`_.


HTTP requests will be signed with a shared secret key using HMAC. Differs from AWS or other HMAC strings because: JoanAssistant
The string to sign format is:

.. code-block:: bash

    <Method>\n\n
    <Content-Type>\n
    <Date>\n
    <URL>

Example String-to-sign

.. code-block:: bash


    GET 

    application/json
    Sun, 18 Jun 2017 11:48:26 GMT
    /api/device/


Example Authorization Header with HMAC signature

.. code-block:: bash

    Authorization: 1b9dbaf5b1183037:Mx0Qi57rqYIbc4gDiDKqYERK8Vmzdwhqk3S+OYoXRu0=

Installation
------------

.. code-block:: bash

    $ pip install httpie-visionect-auth

You should now see ``visionect`` under ``--auth-type`` in ``$ http --help`` output.

Usage
-----

.. code-block:: bash

    $ http -j --auth-type=visionect --auth='client:secret' server:8081/api/users/

Examples
--------

To request status on all registered Joan Devices

.. code-block:: bash

    $ http -j --auth-type=visionect --auth="client:secret" server:8081/api/devices/

License
-------

Copyright (c) 2017 Pierre. Available under the MIT License.
