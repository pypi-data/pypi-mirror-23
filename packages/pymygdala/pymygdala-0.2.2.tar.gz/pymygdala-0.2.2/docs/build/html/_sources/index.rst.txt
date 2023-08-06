.. pymygdala documentation master file, created by
   sphinx-quickstart on Mon Dec 19 16:31:13 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pymygdala
=========

pymygdala API
*************

.. automodule:: pymygdala
    :members:

.. autoclass:: pymygdala.LogDumper
	:members:
	:undoc-members:
	:inherited-members:

.. autoclass:: pymygdala.LogHandler
	:members:
	:undoc-members:
	:inherited-members:

.. autoclass:: pymygdala.SendEvent
	:members:
	:undoc-members:
	:inherited-members:

.. autoclass:: pymygdala.SendNRAOEvent
	:members:
	:undoc-members:
   	:inherited-members:

pymygdala CLI utilities
***********************

pym-dumplogs
------------
.. argparse::
   :module: pymygdala.commands
   :func: get_dumplogs_parser
   :prog: pym-dumplogs
   :nodefault:

pym-sendlog
-----------
.. argparse::
   :module: pymygdala.commands
   :func: get_sendlog_parser
   :prog: pym-sendlog
   :nodefault:

pym-sendevent
-------------
.. argparse::
   :module: pymygdala.commands
   :func: get_sendevent_parser
   :prog: pym-sendevent
   :nodefault:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
