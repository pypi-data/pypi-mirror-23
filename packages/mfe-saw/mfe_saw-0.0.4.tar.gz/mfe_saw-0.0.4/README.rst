McAfee SIEM API Wrapper: MFE_SAW
================================

.. image:: https://img.shields.io/pypi/v/mfe_saw.svg
        :target: https://pypi.python.org/pypi/mfe_saw

.. image:: https://img.shields.io/travis/andywalden/mfe_saw.svg
        :target: https://travis-ci.org/andywalden/mfe_saw

.. image:: https://readthedocs.org/projects/mfe_saw/badge/?version=latest
        :target: https://readthedocs.org/projects/mfe_saw/?badge=latest
        :alt: Documentation Status


McAfee SIEM API Wrapper - MFE_SAW

MFE_SAW is a wrapper around the McAfee ESM API versions 10.x and above.

This project attempts to provide a pythonic interface for specific aspects
of the product including:
* ESM Monitoring
* Datasource Management (add, edit, del)
* Simplified Query interface [TBD]
* Watchlist Operations [TBD]
 

The first target of this project is datasource management. With this library 
and accompanied front-end CLI interface, datasources can be easily added by
providing a few details. 


dsconf/new_ds_cfg.txt
```
name=DC01_DNS
ip=10.10.1.34
rec_ip=172.16.15.10
type=linux

$ mfe_saw -a 

$ mfe_saw -s "DC01_DNS"

```



.. code-block:: python

Here is an example:

.. code-block:: python

    >>> esm = ESM()
    >>> esm.login(host, username, passwd)
    >>> esm.time()
    '2017-07-07T19:47:49.0+0000'
    >>> devtree = DevTree()
    >>> 'loghost-245' in devtree
    True
    >>> devtree.search('3.1.1.1')
   {'dev_type': '0', 'name': 'NXLog-Client-1', 'id': '144119586172698880', 
   'enabled': 'T', 'ds_ip': '3.1.1.1', 'hostname': 'nxlog-client-1', 
   'typeID': '0', 'vendor': 'InterSect Alliance', 'model': 
   'Snare for Windows', 'tz_id': '', 'date_order': '', 'port': '', 
   'syslog_tls': 'F', 'client_groups': '0'}

   
.. image:: https://raw.githubusercontent.com/andywalden/mfe_saw/master/docs/_static/mfe_saw_bw.png
    :target: http://mfe-saw.readthedocs.io/en/latest/index.html

Feature Support
---------------

- Pythonic implementation
- Authentication and session tracking across objects
- Built-in multiprocessing for high performance
- Pass through of native API methods 
- CLI interface
- Get info for existing datasources
- Add new datasources 
- ESM status methods
- More to come!

mfe_saw officially supports Python 3.5–3.7 on Windows and Linux.

Installation
------------

To install MFE_SAW, use pip:

.. code-block:: bash

    $ pip install mfe_saw
    

Documentation
-------------

Documentation is available at http://mfe-saw.readthedocs.io/en/latest/index.html

