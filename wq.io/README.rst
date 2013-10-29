.. figure:: https://raw.github.com/wq/wq/master/images/256/wq.io.png
   :align: center
   :alt: wq.io

   wq.io

`wq.io <http://wq.io/wq.io>`_ is a collection of Python libraries
for consuming (input) and generating (output) external data resources in
various formats. It thereby facilitates interoperability between the `wq
framework <http://wq.io/>`_ and other systems and formats.

Getting Started
---------------

::

    pip install wq.io
    # Or, if using together with wq.app and/or wq.db
    pip install wq

See `the documentation <http://wq.io/docs/>`_ for more information.
See https://github.com/wq/wq.io to fork wq.io or report any issues.

Features
--------

The basic idea behind wq.io is to avoid having to remember the unique
usage of e.g. ``csv``, ``xlrd``, or ``lxml`` every time one needs to
work with an external dataset. Instead, wq.io abstracts these libraries
into a consistent interface that works as an ``iterable`` of
``namedtuples``. The field names for a dataset are automatically
determined from the source file, e.g. the column headers in an Excel
spreadsheet.

::

    from wq.io import load_file
    data = load_file('example.xls')
    for row in data:
        print row.name, row.date

It is straightforward to `extend wq.io <http://wq.io/docs/custom-io>`_
by subclassing existing functionality with custom implementations.
