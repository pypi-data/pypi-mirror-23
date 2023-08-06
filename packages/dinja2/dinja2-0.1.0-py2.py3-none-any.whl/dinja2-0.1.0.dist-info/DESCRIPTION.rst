=============================
Dinja2
=============================

.. image:: https://badge.fury.io/py/dinja2.svg
    :target: https://badge.fury.io/py/dinja2

.. image:: https://travis-ci.org/wooyek/dinja2.svg?branch=master
    :target: https://travis-ci.org/wooyek/dinja2

.. image:: https://codecov.io/gh/wooyek/dinja2/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/wooyek/dinja2

Jinja2 template backend for Django

Documentation
-------------

The full documentation is at https://dinja2.readthedocs.io.

Quickstart
----------

Install Dinja2::

    pip install dinja2

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dinja2.apps.Dinja2Config',
        ...
    )

Add Dinja2's URL patterns:

.. code-block:: python

    from dinja2 import urls as dinja2_urls


    urlpatterns = [
        ...
        url(r'^', include(dinja2_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage




History
-------

0.1.0 (2017-07-20)
++++++++++++++++++

* First release on PyPI.


