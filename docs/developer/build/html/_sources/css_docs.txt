==================================
Working on CSS and Documentation
==================================

CSS
=========

Our grunt tasks handle the compilation and aggregation of css files. Just edit the app/styles/main.scss


Documentation
=================

Our documentation is written with Sphinx_, install it with the virtualenv
activated::

    pip install sphinx


.. _Sphinx: http://sphinx-doc.org/

Edit the relevant docs under the ``docs`` directory, and once done, run
``make html``. You'll have the resulting documentation in ``build/html``
directory.

We have 2 documentation directories:

* api --- API and Embedding for 3rd party apps/services developers
* devel --- Developer guide for the OpenKnesset project (TBD)

e.g: To work on the devel docs, edit the files under ``docs/devel/source``, once
ready to build::

    cd docs/devel
    make html

You'll have the result under::

    docs/devel/build/html

