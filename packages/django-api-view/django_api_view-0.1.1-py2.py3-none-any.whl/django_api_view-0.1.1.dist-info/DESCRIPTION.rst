Django Api View
===============

.. image:: https://travis-ci.org/anthon-alindada/django_api_view.svg?branch=master
    :target: https://travis-ci.org/anthon-alindada/django_api_view

.. image:: https://codecov.io/gh/anthon-alindada/django_api_view/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/anthon-alindada/django_api_view

Django basic api view and api response.

Documentation
-------------

The full documentation is at https://django_api_view.readthedocs.io.

Quickstart
----------

Install Django api view. In the command line::

    pip install django_api_view

Configuration
-------------

Add `'django_api_view'` it to your `INSTALLED_APPS`::

    INSTALLED_APPS = (
        ...
        'django_api_view',
        ...
    )

Simple usage
------------

Read full documentation for full features https://django_api_view.readthedocs.io.

Api View
--------

ApiView will automatically parse post data.

It accepts ``'application/json'``, ``'application/x-www-form-urlencoded'``, or ``'multipart/form-data'``

For example::

    from django_api_view.api_view import ApiView

    class BasicApiView(ApiView):

        def get(self, request):
            # For get method use 'GET' to get parameters
            email = request.GET.get('email')

        def post(self, request):
            # For post method use 'data' to get parameters
            email = request.data.get('email')

Api Response
------------

Api response retuns json response.

Basic example::

    from django_api_view.api_response import ApiResponse

    def get(request):
        # 'data' parameter is optional
        return ApiResponse().success(data={})

Version 0.1 (2017-07-25)
~~~~~~~~~~~~~~~~~~~~~~~~

- Initial release.


