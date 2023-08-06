modconf
=======
.. image:: https://travis-ci.org/chuck1/modconf.svg?branch=master
    :target: https://travis-ci.org/chuck1/modconf
.. image:: https://codecov.io/gh/chuck1/modconf/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/chuck1/modconf
.. image:: https://readthedocs.org/projects/modconf/badge/?version=latest
   :target: http://modconf.readthedocs.io/
   :alt: Documentation Status
.. image:: https://img.shields.io/pypi/v/modconf.svg
   :target: https://pypi.python.org/pypi/modconf
.. image:: https://img.shields.io/pypi/pyversions/modconf.svg
   :target: https://pypi.python.org/pypi/modconf

Pattern for using python modules as configuration files.

Install
-------

::

    pip3 install modconf

Example
-------

Import module

::

    from modconf import import_conf

    conf = import_conf('module_name', folder='optional module search path')

``conf`` is simply the module loaded using ``__import__``

Import class

::

    from modconf import import_class

    cls = import_class('module_name', 'class_name', args, kwargs, foler='optional module search path')

``cls`` is a class definition.
``import_class`` will call ``cls.prepare(*args, **kwargs)`` before returning.

