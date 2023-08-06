=====
Usage
=====

To use Dinja2 in a project, add it to your `INSTALLED_APPS`:

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
