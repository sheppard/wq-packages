.. figure:: https://raw.github.com/wq/wq/master/images/512/wq.app.png
   :align: center
   :alt: wq.app

**wq.app** is a suite of Javascript modules and related assets, created
to facilitate the rapid deployment of offline-cabable HTML5 mobile and
desktop data collection apps for crowdsourcing, citizen science, and
volunteered geographic information, as well as professional field data
collection. wq.app is the client component of the `wq
framework <http://wq.io>`_, and can be used with any REST service. When
combined with a Mustache-capable REST service like
`wq.db <https://github.com/wq/wq.db>`_, wq.app can be used to create
progressively enhanced websites / apps, that can selectively render
individual application screens on the server *or* on the client
depending on project needs, network connectivity, and ``localStorage``
availability.

Project Layout
--------------

**wq.app/js** is built on `a number of
libraries <https://github.com/wq/wq.app/tree/master/js/lib#readme>`_
including `RequireJS <http://requirejs.org>`_, `jQuery
Mobile <http://jquerymobile.com>`_, `Leaflet <http://leafletjs.com>`_,
`d3 <http://d3js.org>`_, and
`Mustache.js <https://mustache.github.com/>`_. wq.app extends these
libraries with:

-  `store.js <https://github.com/wq/wq.app/blob/master/js/store.js>`_, a
   robust ``localStorage``-cached JSON REST client (with a lightweight
   implementation of models and collections)
-  `pages.js <https://github.com/wq/wq.app/blob/master/js/pages.js>`_, a
   PJAX-style ``pushState`` URL router, template renderer, and page
   injector
-  `app.js <https://github.com/wq/wq.app/blob/master/js/app.js>`_, a
   high-level application controller that combines ``store.js`` and
   ``pages.js`` into a full configuration-driven CRUD client (intended
   for use with `wq.db <https://github.com/wq/wq.db>`_'s
   `app.py <https://github.com/wq/wq.db/blob/master/rest/app.py>`_)
-  `map.js <https://github.com/wq/wq.app/blob/master/js/map.js>`_,
   Leaflet integration for app.js models that contain geometry (GeoJSON
   or simple lat/long)
-  `chart.js <https://github.com/wq/wq.app/blob/master/js/chart.js>`_,
   configurable d3-based time series and contour plots
-  and a number of other useful utilities

When using wq.app in the `recommended project
layout <https://github.com/wq/django-wq-template>`_, ``wq.app/js``
should be mapped to ``myproject/app/js/wq``.

**wq.app/css** includes the default stylesheets packaged with jQuery
Mobile and Leaflet. When using wq.app in the `recommended project
layout <https://github.com/wq/django-wq-template>`_, ``wq.app/css``
should be mapped to ``myproject/app/css/wq``.

**wq.app/scss** provides a SASS/SCSS stylesheet for use with Compass,
with appropriate macros for generating custom jQuery Mobile themes.

**wq.app/util** provides a Python-based build process for compiling wq
apps: inlining templates, optimizing code (via r.js), and generating an
application cache manifest.

wq.app does not currently include any default HTML templates, leaving
this as an exercise for the project implementer.
