Quick Start
===========

.. note:: nothing really works yet

First you'll need to get install the `opri` CLI::

    $ curl -Lo- https://[...] | bash

Now create a host for your project::

    $ opri host <short_name> <repo_url | local_dir> [main_url]
    ...

If you use a local_dir opri will look for the git config and use the
`origin` url as the host's blessed repo.

Next, configure your `.travis.yml` file to fire the update process on success
by adding the following lines to the end of your file::

  notifications:
    webhooks:
      urls:
        - http://opri.hasadna.org.il/events
      on_success: always
      on_failure: never
      on_start: false

Commit your changes and you're done.  Whenever you push to your `master`
or `dev` branches and your tests pass, the  host at
`<short_name>.hasadna.org.il` or `dev.<short_name>.hasdna.org.il`
will be updated.

.. _Travis: http://travis-ci.com

