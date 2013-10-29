.. figure:: https://raw.github.com/wq/wq/master/images/256/wq.db.png
   :align: center
   :alt: wq.db

   wq.db

`wq.db <http://wq.io/wq.db>`_ is a collection of Python modules for
building robust, flexible schemas and REST APIs for use in field data
collection apps and (more generally) progressively enhanced mobile-first
websites. wq.db is the backend component of `wq <http://wq.io>`_ and is
geared primarily for use with `wq.app <http://wq.io/wq.app>`_, though it
can be used separately. wq.db is built on the
`Django <https://www.djangoproject.com/>`_ platform.

Getting Started
---------------

::

    pip install wq.db
    # Or, if using together with wq.app and/or wq.io
    pip install wq

See `the documentation <http://wq.io/docs/>`_ for more information.
See https://github.com/wq/wq.db to fork wq.db or report any issues.

Features
--------

wq.db has two primary components: a REST API generator
(`wq.db.rest <http://wq.io/docs/rest>`_) and a collection of schema
design patterns (`wq.db.patterns <http://wq.io/docs/about-patterns>`_)
that facilitate flexible database layouts.

`wq.db.rest <http://wq.io/docs/rest>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extends the excellent `Django Rest
Framework <http://django-rest-framework.org>`_ with a collection of
views, serializers, and context processors useful for creating a
progresively enhanced website that serves as its own mobile app and its
own REST API. The core of the library (app.py) includes an admin-style
``autodiscover()`` that automatically routes REST urls to installed
models, and provides a descriptive JSON configuration object for
consumption by `wq.app's client-side
router <http://wq.io/docs/app-js>`_. wq.db.rest also includes a
CRS-aware GeoJSON serializer and renderer.

`wq.db.patterns <http://wq.io/docs/about-patterns>`_
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A collection of recommended design patterns
(`annotate <http://wq.io/docs/annotate>`_,
`identify <http://wq.io/docs/identify>`_,
`locate <http://wq.io/docs/locate>`_, and
`relate <http://wq.io/docs/relate>`_) that provide long-term flexibility
and sustainability for data collection systems. These patterns are
implemented as installable Django apps.

Batteries Included
~~~~~~~~~~~~~~~~~~

Like Django itself, wq.db includes a ``contrib`` module that provides
additional functionality not considered to be part of the "core"
library.

`files <http://wq.io/docs/files>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generic file manager. Supports using the same ``FileField`` for both
images and files. Also includes a URL-driven thumbnail generator.

`vera <http://wq.io/vera>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reference implementation of the ERAV model, an extention to EAV with
support for maintaining multiple versions of an entity.
