==========
Golangish
==========

Overview
---------
Port golang's CSP semantics to Python, namely the behavior of the `go`, `<-` `->` and `select` constructs.

Installation
===============

To install use pip:

    $ pip3 install golangish


Or clone the repo:

    $ git clone github.com/edouardklein/golangish
    $ python3 setup.py install
    
    

Usage
==========

Documentation
+++++++++++++++++

Read the documentation http://golangish.readthedocs.io/en/latest/ to understand how to use golangish.

In the cloned repo
++++++++++++++++++++

Helper targets
>>>>>>>>>>>>>>>>>>

To build the documentation, run:

    $ make doc
    
To run the test, run:

    $ make test

To check the code's superficial cleanliness run:

    $ make lint
    
To run tests each time a Python file is edited

    $ make live

