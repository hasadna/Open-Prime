=========================================
Setting up the development environment
=========================================

Pre-Requisites
==============

Open Subs is using Open Knesset as its backend serving candidates's data.

Instructions were tested on Ubuntu, but should work similarly on any
Linux flavor, OSX and even Windows.
Install rvm with stable ruby, follow instructions here: https://rvm.io/rvm/install
and then run the following commands as root:

.. code-block:: sh

    # Install nvm, follow instructions here: https://github.com/creationix/nvm
    # After nvm is installed, run the following:
    nvm install stable
    # To automatically use the stable node on login, add the following to the bottom of ~/.bashrc:
    nvm use stable
    # Install grunt and bower globally:
    npm install bower -g
    npm install grunt-cli -g
    # Install compass:
    gem install compass


Updating node and bower modules
===============================

.. code-block:: sh

    cd Open-Subs/angular
    npm install
    bower install


Setting the frontend server's settings
======================================

The angular local settings contains the url to the django backend server:

.. code-block:: sh

  cd Open-Subs/angular/app/scripts
  cp settings.js.dist settings.js

This sets up the address of the Open-Knesset API server at https://localhost:8000

If you want to run without a backend - set `offline` to true in 
the settings.js file.

if you are running open knesset, make sure to run your local open knesset on https by using manage.py runsslserver

Important! - you will need to approve security exception to allow running on https - this is OK, you are running locally..

Be sure to add an exception for your local open knesset by going to https://localhost:8000/ and approving the exception

Setting up for testing on facebook
==================================

.. code-block:: text

    Create a test app on facebook

    Add the Canvas platform and set the Secure Canvas URL to https://localhost:9000/
    Add the Website platform and set the Site URL to https://localhost:9000/

    That's it, you can now browse to your canvas app page!

Running the tests
=================

We use protractor for browser testing

For the tests to run properly you should run without a backend server and without facebook.

Just set in your settings.js: offline: true, noFacebook: true

To run the complete testing suite, run:

.. code-block:: sh

    $ node_modules/grunt-protractor-runner/node_modules/.bin/webdriver-manager update
    $ grunt test

To debug the tests:

.. code-block:: sh

    $ sudo npm install protractor -g
    $ webdriver-manager update

    # in the background - run the server

    $ grunt serve

    # then, you can run protractor directly

    $ protractor test/e2e/e2e.conf.js --baseUrl "https://localhost:9000"

    # you can run a single spec:

    $ protractor test/e2e/e2e.conf.js --baseUrl "https://localhost:9000" --specs test/e2e/specs/main.js

    # Some useful optional arguments:
    # --verbose  --pause-on-error
