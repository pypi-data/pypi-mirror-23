=====================
IL-2 FB Events Parser
=====================

|pypi_package| |pypi_downloads| |python_versions| |license|

|unix_build| |windows_build| |coverage_status|

|code_issues| |codeclimate| |codacy| |quality| |health| |requirements|


**Table of contents**

.. contents::
    :local:
    :depth: 1
    :backlinks: none


Synopsis
--------

This is a Python library which parses events from log produced by dedicated
server of «IL-2 Forgotten Battles» flight simulator. Resulting information
about events is stored in special data structures.


Demo
----

You may see this library in action even if you do not understand its purpose.

All you need is just to `visit project's demo page`_.

That page allows you to test parser's ability to process strings. If you
do not know what to enter into a text area, you may click ``Insert test data``
and parse it.

If something goes wrong, you will be prompted to confirm automatic creation of
bug report which will be
`listed on this page <https://github.com/IL2HorusTeam/il2fb-events-parser/issues>`_.


Known events
------------

This library supports all known events produced by dedicated server
(129 unique events).

To see their list, go to the `demo page`_ and click
``See the list of supported events`` link.


Installation
------------

Get Python package from PyPI:

.. code-block:: bash

  pip install il2fb-events-parser


Usage
-----

If you need to be able to parse all events this library knows about, use
``EventsParser.parse_string()``:

Import ``EventsParser`` and create its instance:

.. code-block:: python

    from il2fb.parsers.events import EventsParser

    parser = EventsParser()


Parse a string to get an instance of event:

.. code-block:: python

    event = parser.parse("[8:33:05 PM] User0 has connected")


Explore event's internal structure:

.. code-block:: python

    print(event)
    # <Event: HumanHasConnected>

    print(event.time)
    # datetime.time(20, 33, 5)

    print(event.actor)
    # <Human 'User0'>

    print(event.actor.callsign)
    # User0


Convert event into a dictionary:

.. code-block:: python

    import pprint

    pprint.pprint(event.to_primitive())
    # {'actor': {'callsign': 'User0'},
    #  'name': 'HumanHasConnected',
    #  'time': '20:33:05',
    #  'verbose_name': 'Human has connected'}


Exceptions
----------

If you try to parse unknown event, ``EventParsingError`` will be raised:

.. code-block:: python

    parser.parse("foo bar")
    # Traceback (most recent call last):
    # …
    # EventParsingError: No event was found for string "foo bar"

Current list of supported events is rather full, but ``EventParsingError`` is
quite possible, because server's events are undocumented and this library may
do not know about all of them.

In case you need to catch this error, its full name is
``il2fb.parsers.events.exceptions.EventParsingError``.


Safe usage
----------

You can set flag ``ignore_errors=True`` if you don't care about any exceptions:

.. code-block:: python

    from il2fb.parsers.events import EventsParser

    parser = EventsParser()
    event = parser.parse("foo bar", ignore_errors=True)
    print(event is None)
    # True

Any error (except ``SystemExit`` and ``KeyboardInterrupt``) will be muted and
``None`` will be returned.


.. |unix_build| image:: https://travis-ci.org/IL2HorusTeam/il2fb-events-parser.svg?branch=master
   :target: https://travis-ci.org/IL2HorusTeam/il2fb-events-parser

.. |windows_build| image:: https://ci.appveyor.com/api/projects/status/a47k677tr59bd5wg/branch/master?svg=true
    :target: https://ci.appveyor.com/project/oblalex/il2fb-events-parser
    :alt: Build status of the master branch on Windows

.. |coverage_status| image:: http://codecov.io/github/IL2HorusTeam/il2fb-events-parser/coverage.svg?branch=master
    :target: http://codecov.io/github/IL2HorusTeam/il2fb-events-parser?branch=master
    :alt: Test coverage

.. |codeclimate| image:: https://codeclimate.com/github/IL2HorusTeam/il2fb-events-parser/badges/gpa.svg
   :target: https://codeclimate.com/github/IL2HorusTeam/il2fb-events-parser
   :alt: Code Climate

.. |codacy| image:: https://api.codacy.com/project/badge/c0385f01ffa545dea3a52a51cfc53221
    :target: https://www.codacy.com/app/oblalex/il2fb-events-parser
    :alt: Codacy Code Review

.. |quality| image:: https://scrutinizer-ci.com/g/IL2HorusTeam/il2fb-events-parser/badges/quality-score.png?b=master
   :target: https://scrutinizer-ci.com/g/IL2HorusTeam/il2fb-events-parser/?branch=master
   :alt: Scrutinizer Code Quality

.. |health| image:: https://landscape.io/github/IL2HorusTeam/il2fb-events-parser/master/landscape.svg?style=flat
   :target: https://landscape.io/github/IL2HorusTeam/il2fb-events-parser/master
   :alt: Code Health

.. |code_issues| image:: https://www.quantifiedcode.com/api/v1/project/49c826961bd54c14a5ca1959e07d05c1/badge.svg
     :target: https://www.quantifiedcode.com/app/project/49c826961bd54c14a5ca1959e07d05c1
     :alt: Code issues

.. |pypi_package| image:: http://img.shields.io/pypi/v/il2fb-events-parser.svg?style=flat
   :target: http://badge.fury.io/py/il2fb-events-parser/

.. |pypi_downloads| image:: http://img.shields.io/pypi/dm/il2fb-events-parser.svg?style=flat
   :target: https://crate.io/packages/il2fb-events-parser/

.. |python_versions| image:: https://img.shields.io/badge/Python-2.7,3.4,3.5,3.6-brightgreen.svg?style=flat
   :alt: Supported versions of Python

.. |license| image:: https://img.shields.io/badge/license-LGPLv3-blue.svg?style=flat
   :target: https://github.com/IL2HorusTeam/il2fb-events-parser/blob/master/LICENSE

.. |requirements| image:: https://requires.io/github/IL2HorusTeam/il2fb-events-parser/requirements.svg?branch=master
     :target: https://requires.io/github/IL2HorusTeam/il2fb-events-parser/requirements/?branch=master
     :alt: Requirements Status


.. _demo page: http://il2horusteam.github.io/il2fb-events-parser/
.. _visit project's demo page: `demo page`_
