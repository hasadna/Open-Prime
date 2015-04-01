==================
Deploying the code
==================

When you are done playing, follow this guide to deploy the code to a real server:

From your PC
===========

The following commands should run from your personal computer, not on the server:

.. code-block:: sh

    $ cd Open-Subs/angular
    $ grunt build

Now, the Open-Subs/angular/dist directory contains all the static files and you just need to copy them to the remote server.

On the server
=============

Copy the contents of the Open-Subs/angular/dist directory to the server.

Copy Open-Subs/angular/app/scripts/settings.js.dist into scripts/settings.js on the server

Then, edit it to point to the correct open knesset backend server - make sure to use the https protocol!

As long as the settings.js.dist file doesn't change it only needs to be done once, not every deployment.

Then, setup a web server to serve static files from that directory - make sure it serves on https as this is required by facebook

The server should support POST requests - when it gets them it should just treat them as GET requests

That's it.

Setting up facebook
===================

Create an Open-Subs app on facebook

Add the Canvas platform and set the Secure Canvas URL to point to your server: https://opensubs.org/
