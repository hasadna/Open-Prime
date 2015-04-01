Welcome to Open-Prime documentation!
===================================================

Open Prime lets' an organization host all its web projects
on one machine using Docker_.
Open Prime helps project committer host their project's live.
and development servers.
It includes Postgres, Mongo and Redis servers for your backend,
wraps your app server with Varnish and Nginx and servs your files from a CDN.

After a simple setup, your servers will be automaticly updated
whenever you update your git repository. The system assumes you are using
Travis for CI and if you are not, please stop reading
this guide and add Travis_ to your project.

Contents:

.. toctree::
    :maxdepth: 2

    quick_start
    developer

.. _Travis: http://travis-ci.com
.. _Docker: https://docker.com
