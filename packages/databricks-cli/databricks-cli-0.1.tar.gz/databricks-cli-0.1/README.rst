databricks-cli
==============
.. image:: https://travis-ci.org/databricks/databricks-cli.svg?branch=master
   :target: https://travis-ci.org/databricks/databricks-cli
   :alt: Build Status


This repository includes the code for the command line interface to
Databricks APIs. Currently, the only APIs implemented are for DBFS.
**PLEASE NOTE**, this CLI is under active development and is released as
an experimental client. This
means that interfaces are subject to being changed and that
SLAs/engineering support are not provided.

Requirements
------------

-  Python Version > 2.7.9
-  Python 3 is not supported

Installation
---------------

To install simply run
``pip install databricks-cli``

In order to upgrade your databricks-cli installation please run
``pip install --upgrade databricks-cli``

Getting started
----------------

After installing, ``dbfs`` will be installed into your PATH. Try it out
by running ``dbfs --help``.

To configure your username/password/host try running ``dbfs configure``.
You will be prompted for your username, password, and host.

Don't have a password because of SSO?
-------------------------------------

Your administrator can choose to set a password for you.
