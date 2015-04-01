.. _devel_workflow:

=========================
Development Workflow
=========================

Congratulations, we have everything installed, now it's time to start working on
the project. Run the local server using: 

.. code-block:: sh

    grunt serve

Here are some guidelines and scenarios to show the flow.

Commits and Pull Requests
========================================

Make it easier for you and the maintainers, increasing the chances of a pull
request getting accepted:

- No big Pull Requests. It makes reviewing and ensuring correctness hard. If
  possible, break it to smaller commits/pulls, each related to a specific issue.
- Always work on a specific issue from our huboard_. Open new issue if
  needed and claim it in the comments.
- Discuss big things in the `open knesset forum`_.

.. _huboard: https://huboard.com/hasadna/Open-Subs/
.. _open knesset forum: http://forum.hasadna.org.il/c/5-category/12-category

Before Coding
==========================

We need to make sure we're in sync with changes done by others (upstream).

.. important::

    Please do this every time before you start developing:

Update the code and requirements
--------------------------------------

Enter your `Open-Subs` directory, and add the `hasadna` respoitory:

.. code-block:: sh

    git remote add hasadna git@github.com:hasadna/Open-Subs.git

Pull upstream changes to your fork just before you start coding:

.. code-block:: sh

    git pull hasadna master

.. note::

    Running this command requires having SSH keys registered with github. If you don't have these, or
    if you don't understand what this means and do not want to look it up, you can use:

    git pull https://github.com/hasadna/Open-Subs.git master

Refresh your code base by running:

.. code-block:: sh

    npm install; bower install


Testing
-------

.. code-block:: sh

    grunt test


See :ref:`devel_tips` for a few bash functions that may help.

While Coding
==============

General
---------

Follow this style guide: https://github.com/johnpapa/angularjs-styleguide

When an issue is done
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh

    git status # to see what changes you made
    git diff filename # to see what changed in a specific file
    git add filename # for each file you changed/added.
    git commit -m 'Initial docs #7'
    git push # pushes changes to your mirror in the clouds

.. note::

    Please write a sensible commit message, and include "#[number]"
    of the issue number you're working on (if any).

Go to github.com and send a "pull request" so your code will be reviewed and
  pulled into the main branch, make sure the base repo is
  `hasadna/Open-Subs`_.

.. _PEP20: https://www.python.org/dev/peps/pep-0020/
.. _hasadna/Open-Subs: http://github.com/hasadna/Open-Subs
