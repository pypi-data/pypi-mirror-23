py_steamcmd_installer
=====================
Simple tool to install steam apps via python using the steamcmd

Prerequisites
=============
Make sure steamcmd and python is installed

Installing
==========
.. code-block:: bash

  pip install py_steamcmd_installer

How to use:
===========

.. code-block:: python

  # import the package
  from py_steamcmd_installer import py_steamcmd_installer

  # create a steamcmd object and give the steamcmd path as an argument
  steamcmd = py_steamcmd_installer.Steamcmd("/usr/bin/steamcmd")

  # create a function that handels the process output
  def output_parser(output):
    print("output: " + output)

  # set the output parser
  steamcmd.handleOutput = output_parser

  # install a server
  steamcmd.installServer(4020, "../server_path")
