connect.py
==========

.. image:: https://img.shields.io/pypi/v/connect.py.svg
   :target: https://pypi.python.org/pypi/connect.py/
.. image:: https://img.shields.io/pypi/pyversions/connect.py.svg
   :target: https://pypi.python.org/pypi/connect.py/
.. image:: https://travis-ci.org/GiovanniMCMXCIX/connect.py.svg?branch=master
   :target: https://travis-ci.org/GiovanniMCMXCIX/connect.py
.. image:: https://discordapp.com/api/v7/guilds/119860281919668226/embed.png?style=shield
   :target: https://discord.gg/u5F8y9W

Installing
----------

To install the library, you can just run the following command:

.. code:: sh

    python3 -m pip install -U connect.py

To install the development version, do the following:

.. code:: sh

    python3 -m pip install -U https://github.com/GiovanniMCMXCIX/connect.py/archive/master.zip

Requirements
------------

- Python 3.x
- `requests` library

Examples
--------

.. code:: py

    import connect

    client = connect.Client()

    def release_test():
        releases = client.search_release('friends')
        print('\n[connect.Client.search_release] Found the following:')
        for release in releases:
            print('{0.title} by {0.artists} [{0.catalog_id}] was released on {0.release_date} and has {1} track(s)'.format(
                release, len(release.tracks)))

Bugs
----

- Lists that come from the library have random positions in versions older than Python 3.6

 Example `['foo', 'bar', 'wew', 'lad']` comes as `['bar', 'lad', 'foo', 'wew']`