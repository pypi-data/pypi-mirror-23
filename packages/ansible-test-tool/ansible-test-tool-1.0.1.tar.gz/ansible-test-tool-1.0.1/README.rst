ansible-test: Ansible Local Testing Framework
=============================================

Ansible-test is a tool for testing your automation in docker containers. It works a little bit like chef's kitchen.

.. code-block:: bash

   usage: ansible-test [-h] [--ansible ANSIBLE] [--image IMAGE] role roles_path

   positional arguments:
      role                  Define the role to test
      roles_path            Define the path to the roles (like in ansible.cfg)

   optional arguments:
      -h, --help            show this help message and exit
      --ansible ANSIBLE, -a ANSIBLE
                        The ansible version to install
      --image IMAGE, -i IMAGE
                        The docker base image to test the role/playbook on.

Installation
------------

To install ansible-test:

.. code-block:: bash

   $ pip install ansible-test

Documentation
-------------

ansible-test requires that you have docker installed locally. If you are using Mac OSX, I recommend you use boot2docker.
