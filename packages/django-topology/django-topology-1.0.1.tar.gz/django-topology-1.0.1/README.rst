=============================
Django Topology
=============================

.. image:: https://badge.fury.io/py/django-topology.svg
    :target: https://badge.fury.io/py/django-topology

.. image:: https://travis-ci.org/george-silva/django-topology.svg?branch=master
    :target: https://travis-ci.org/george-silva/django-topology

.. image:: https://codecov.io/gh/george-silva/django-topology/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/george-silva/django-topology

Geometry and  Topology utilitaries

Documentation
-------------

The full documentation is at https://django-topology.readthedocs.io.

Quickstart
----------

Install Django Topology::

    pip install django-topology

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'topology.apps.TopologyConfig',
        ...
    )

Add Django Topology's URL patterns:

.. code-block:: python

    from topology import urls as topology_urls


    urlpatterns = [
        ...
        url(r'^', include(topology_urls)),
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
