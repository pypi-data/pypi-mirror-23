=============
fullstop. CLI
=============

.. image:: https://travis-ci.org/zalando-stups/fullstop-cli.svg?branch=master
   :target: https://travis-ci.org/zalando-stups/fullstop-cli
   :alt: Build Status

.. image:: https://coveralls.io/repos/zalando-stups/fullstop-cli/badge.svg
   :target: https://coveralls.io/r/zalando-stups/fullstop-cli
   :alt: Code Coverage

.. image:: https://img.shields.io/pypi/dw/stups-fullstop.svg
   :target: https://pypi.python.org/pypi/stups-fullstop/
   :alt: PyPI Downloads

.. image:: https://img.shields.io/pypi/v/stups-fullstop.svg
   :target: https://pypi.python.org/pypi/stups-fullstop/
   :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/l/stups-fullstop.svg
   :target: https://pypi.python.org/pypi/stups-fullstop/
   :alt: License

Convenience command line tool for fullstop. audit reporting.

.. code-block:: bash

    $ sudo pip3 install --upgrade stups-fullstop

Usage
=====

.. code-block:: bash

    $ fullstop login
    $ fullstop violations

You can also run it locally from source:

.. code-block:: bash

    $ python3 -m fullstop

Running Unit Tests
==================

.. code-block:: bash

    $ python3 setup.py test --cov-html=true

Releasing
=========

.. code-block:: bash

    $ ./release.sh <NEW-VERSION>


