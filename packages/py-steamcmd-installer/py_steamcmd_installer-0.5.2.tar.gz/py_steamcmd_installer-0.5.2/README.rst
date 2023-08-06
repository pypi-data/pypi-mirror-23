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
  import py_steamcmd_installer

  # create a steamcmd object and give the steamcmd path as an argument
  steamcmd = py_steamcmd_installer.steamcmd("/usr/bin/steamcmd")

  # create a function that handels the process output
  def output_parser(output):
    # under Linux the output will be printed from the pty
    if steamcmd.__platform == "Windows":
      print(output)

  # set the output parser
  steamcmd.handleOutput = output_parser

  # install a server
  steamcmd.installServer(4020, ../server_path)
