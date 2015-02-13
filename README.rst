Flask-PagedList
===============

Flask-PagedList bundles features from pypagedlist into a blueprint named 'PagedList'.

Installation
------------

Flask-PagedList can be installed using ``pip`` from `PyPI`_. `virtualenv`_ is highly
recommended:

.. code-block:: bash

    pip install -U flask-pagedlist

.. _PyPI: https://pypi.python.org/pypi/Flask-PagedList
.. _virtualenv: https://virtualenv.pypa.io/en/latest/

For development, instead, clone the `github repository <https://github.com/timonwong/flask-pagedlist>`_, and use:

.. code-block:: bash

    python setup.py develop  # Or, pip install -e .


Example Project
----------------

Screenshots
~~~~~~~~~~~

Traditional
+++++++++++

.. image:: https://raw.github.com/timonwong/flask-pagedlist/gh-pages/screenshots/demo1.png

AJAX
++++

.. image:: https://raw.github.com/timonwong/flask-pagedlist/gh-pages/screenshots/demo2.png

Run
~~~

Here is a simple description about how to run the demo project:

.. code-block:: bash

    # 1. Clone this git repo in order to get the example
    git clone https://github.com/timonwong/flask-pagedlist.git
    cd flask-pagedlist

    # 2. Install flask-pagedlist
    pip install -U flask-pagedlist

    # 3. Install dependencies for the example
    pip install -U -r example-requirements.txt

    # 4. Start the example project
    python run_example.py


Usage
-----

Basic usage
~~~~~~~~~~~

Here is an example:

.. code-block:: python

    from flask_pagedlist import PagedList

    PagedList(app)


Static resources
~~~~~~~~~~~~~~~~

``pagedlist_static_for`` is recommended for requiring static resources for Flask-PagedList in templates:

.. code-block:: python

    def pagedlist_static_for(filename, use_minified=None):
        """Resource finding function, also available in templates.

        :param filename: File to find a URL for.
        :param use_minified': If set to ``True``/``False``, use/don't use
                              minified. If ``None``, use the default setting
                              from ``PAGEDLIST_USE_MINIFIED``.
        :return: A URL.
        """


Configuration
~~~~~~~~~~~~~

``PAGEDLIST_USE_MINIFIED``
++++++++++++++++++++++++++


``PAGEDLIST_PREFIX``
++++++++++++++++++++
