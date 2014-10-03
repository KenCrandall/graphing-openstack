Graphing OpenStack
==================

Attempt at graphing the relationships between assorted OpenStack services

Requirements
============

Generating graphs requires GraphViz to be installed.

Key
====

Line Color
----------


* REQUIRES (black)

  * x REQUIRES y. X cannot be used without y
* CAN-USE (grey)

  * x CAN-USE y. x can be used with our without y.
* THROUGH (label)

  * x REQUIRES y THROUGH z. library z is used by x to communicate to y
* DEPENDS-ON (red)

  * x DEPEND-ON y. x depends on y to set things up and consume the resources x produces.
  * Example: cinder requires nova. Otherwise a user cannot attach a volume to an instance
