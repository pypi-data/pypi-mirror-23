=============================
django-curriculum
=============================

.. image:: https://badge.fury.io/py/django-curriculum.svg
    :target: https://badge.fury.io/py/django-curriculum

.. image:: https://travis-ci.org/axeliodiaz/django-curriculum.svg?branch=master
    :target: https://travis-ci.org/axeliodiaz/django-curriculum

.. image:: https://codecov.io/gh/axeliodiaz/django-curriculum/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/axeliodiaz/django-curriculum

A simple django project to create a curriculum vitae

Documentation
-------------

The full documentation is at https://django-curriculum.readthedocs.io.

Quickstart
----------

Install django-curriculum::

    pip install django-curriculum

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_curriculum.apps.DjangoCurriculumConfig',
        ...
    )

Add django-curriculum's URL patterns:

.. code-block:: python

    from django_curriculum import urls as django_curriculum_urls


    urlpatterns = [
        ...
        url(r'^', include(django_curriculum_urls)),
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
