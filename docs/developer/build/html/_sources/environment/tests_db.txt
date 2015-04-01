.. _tests_develdb:

=============================================
Initial Testing, Development DB & Server
=============================================

After you've installed the base environment, it's time to run the tests and get
an initial development db.

.. important::

    - Linux users: you can replace ``python manage.py`` with ``./manage.py`` for
      less typing
    - Run the manage.py commands from the `Open-Knesset` directory, with the
      virtualenv activated.


Running Tests
==============

.. code-block:: sh

    python manage.py test

Download the Development DB
===============================

Download and extract dev.db.zip_ or dev.db.bz2_ (bz2 is smaller). After
unpacking, **place dev.db in the `Open-Subs` directory**.

.. important::

    TODO: the development db is still not there

.. _dev.db.zip: http://files.hasadna.org.il/osubs/dev.db.zip
.. _dev.db.bz2: http://files.hasadna.org.il/osubs/dev.db.bz2


Running the Development server
=====================================

To run the development server:

.. code-block:: sh

    python subs.py

Once done, you can access it with your browser via http://localhost:5000 .


We're cool ? Time for some :ref:`devel_workflow`.
