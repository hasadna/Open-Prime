Development
===========

Open Prime lets' an organization host all its web projects
in on one machine using Docker_ containers.

.. note:: if you're ready to contribute, check out our board_.

Architecture
------------

Open Prime is made from multiple components each contained in a docker. Redundency is
achieved through mirroring and clustering of the entire machine. i.e. no need
for a DB cluster or for multiple apps serving the same code base.

Each of the eKnights is updated using `Travis Webhooks`_ resulting in
a cycle that starts when a committer pushes his code to github, waking up
travis and upon success, updating the App server. Prime will watch both the
`master` and `dev` branches, updating the appropiate container::

                                      +                                       +
                Unix Sockets          |               TCP Sockets             |
                                      |                                       |
   +----------+     +--------------+  |   +------------+                      |
   |          |     |              |  |   |            |                      |
   | Postgres |     | Open Knesset |  |   |    DNS     |                      |
   |          |     |              |  |   |            |                      |
   +----------+     ++------------++  |   +------------+                      |
                     |     Dev    |   |                                       |
   +----------+      +------------+   |   +------------+     +-------------+  |
   |          |                       |   |            |     |             |  |
   |  Mongo   |     +--------------+  |   | Web Server |     | Accelarator |  |
   |          |     |              |  |   |            |     |             |  |
   +----------+     | Open Pension |  |   +------------+     +-------------+  |
                    |              |  |                                       |
   +----------+     ++------------++  |   +------------+                      |
   |          |      |     Dev    |   |   |            |                      |
   |  Redis   |      +------------+   |   |   SMTP     |                      |
   |          |           ...         |   |            |                      |
   +----------+                       |   +------------+                      |
                                      |                                       |
  +---------------------------------------------------------------------------+
                                                                               
     +---------------------------------------------------------------------+   
     |                                                                     |   
     |                     Content Distribuition Network                   |   
     |                                                                     |   
     +---------------------------------------------------------------------+   

Monitoring
----------
[supervisord?, logs?]

.. _Docker: https://www.docker.com/
.. _board: https://trello.com/b/oDT8kPyC/-
.. _Travis Webhooks: http://docs.travis-ci.com/user/notifications/#Webhook-notification

