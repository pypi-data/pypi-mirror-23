Mackerel
========

Mackerel is a minimal static site generator written in typed Python 3.6+.

.. image:: https://img.shields.io/pypi/v/mackerel.svg
   :target: https://pypi.python.org/pypi/mackerel/
   :alt: Latest Version
.. image:: https://travis-ci.org/pkolios/mackerel.svg?branch=master
   :target: https://travis-ci.org/pkolios/mackerel
   :alt: Build Status
.. image:: https://coveralls.io/repos/pkolios/mackerel/badge.svg?branch=master
   :target: https://coveralls.io/r/pkolios/mackerel
   :alt: Coverage Status


Installation
------------

Installing mackerel with pip::

    $ pip install mackerel


Or by cloning the repository::

    $ git clone https://github.com/pkolios/mackerel.git


And installing mackerel::

    $ cd mackerel
    $ pip install -e .


Documentation
-------------

View the basic usage documentation at `mackerel.sh <http://mackerel.sh>`_.


Testing
-------

Running the tests from mackerel root directory::

    $ pytest


License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/pkolios/mackerel/blob/master/LICENSE>`_ file for more details.


Changelog
---------

0.2 (2017-07-09)
++++++++++++++++

**Bugfixes**

- Fix an error in the packaging that caused ``mackerel init`` command to fail
  due to the lack of ``config.ini``.

**Improvements**

- Rework the ``setup.py`` script to increase release automation.

0.1 (2017-07-09)
++++++++++++++++

* First preview release.


