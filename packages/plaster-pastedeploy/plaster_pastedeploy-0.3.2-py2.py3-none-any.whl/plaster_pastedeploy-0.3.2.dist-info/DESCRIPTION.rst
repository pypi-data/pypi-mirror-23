===================
plaster_pastedeploy
===================

.. image:: https://img.shields.io/pypi/v/plaster_pastedeploy.svg
        :target: https://pypi.python.org/pypi/plaster_pastedeploy

.. image:: https://img.shields.io/travis/Pylons/plaster_pastedeploy/master.svg
        :target: https://travis-ci.org/Pylons/plaster_pastedeploy

``plaster_pastedeploy`` is a plaster_ plugin that provides a ``plaster.Loader``
that can parse ini files according to the standard set by PasteDeploy_. It
supports the ``wsgi`` plaster protocol, implementing the
``plaster.protocols.IWSGIProtocol`` interface.

Usage
=====

Applications should use ``plaster_pastedeploy`` to load settings from named
sections in a configuration source (usually a file).

- Please look at the documentation for plaster_ on how to integrate this
  loader into your application.

- Please look at the documentation for PasteDeploy_ on the specifics of the
  supported INI file format.

Most applications will want to use
``plaster.get_loader(uri, protocols=['wsgi'])`` to get this loader. It then
exposes ``get_wsgi_app``, ``get_wsgi_app_settings``, ``get_wsgi_filter`` and
``get_wsgi_server``.

.. code-block:: python

    import plaster

    loader = plaster.get_loader('development.ini', protocols=['wsgi'])
    # to get any section out of the config file
    settings = loader.get_settings('app:main')

    # to get settings for a WSGI app
    app_config = loader.get_wsgi_app_settings() # defaults to main

    # to get an actual WSGI app
    app = loader.get_wsgi_app() # defaults to main

    # to get a filter and compose it with an app
    filter = loader.get_wsgi_filter('filt')
    app = filter(app)

    # to get a WSGI server
    server = loader.get_wsgi_server() # defaults to main

    # to start the WSGI server
    server(app)

Any ``plaster.PlasterURL`` options are forwarded as defaults to the loader.
Some examples are below:

- ``development.ini#myapp``

- ``development.ini?http_port=8080#main``

- ``pastedeploy+ini:///path/to/development.ini``

- ``pastedeploy+ini://development.ini#foo``

- ``egg:MyApp?debug=false#foo``

.. _PasteDeploy: http://pastedeploy.readthedocs.io/en/latest/
.. _plaster: http://docs.pylonsproject.org/projects/plaster/en/latest/


0.3.2 (2017-07-01)
==================

- Resolve an issue in which ``NoSectionError`` would not be properly caught on
  Python 2.7 if the ``configparser`` module was installed from PyPI.
  See https://github.com/Pylons/plaster_pastedeploy/issues/5

0.3.1 (2017-06-02)
==================

- Recognize the ``pastedeploy+egg`` scheme as an ``egg`` type.

0.3 (2017-06-02)
================

- Drop the ``ini`` scheme and replace with ``file+ini`` and ``pastedeploy``.
  Also rename ``ini+pastedeploy`` and ``egg+pastedeploy`` to
  ``pastedeploy+ini`` and ``pastedeploy+egg`` respectively.
  See https://github.com/Pylons/plaster_pastedeploy/pull/4

0.2.1 (2017-03-29)
==================

- Fix a bug in 0.2 in which an exception was raised for an invalid section
  if the a non-config-file-based protocol was used.

0.2 (2017-03-29)
================

- No longer raise ``plaster.NoSectionError`` exceptions. Empty dictionaries
  are returned for missing sections and a user should check ``get_sections``
  for the list of valid sections.

0.1 (2017-03-27)
================

- Initial release.


