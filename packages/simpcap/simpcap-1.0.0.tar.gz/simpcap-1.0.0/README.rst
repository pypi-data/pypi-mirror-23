Simpcap (Python-based PCAP Parser)
==================================
Simpcap is a Python-based PCAP Parser built on Python 2.7. Simpcap uses Click for command line functionality. Simpcap lists basic information about specific packets in a PCAP file. Simpcap checks the source and destination ports, layers, and TLS (or SSL) version for each packet. Simpcap will display certain packets based on what flags and options are provided when the parser is executed. Simpcap can output the results to the command line or to a TXT file.

Getting Started
---------------
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Install Python 2.7 from python.org. Then, run "pip install simpcap" in the command prompt. That's it!


Built With
----------
* `Python 2.7.13`_ - Scripting Language
.. _`Python 2.7.13`: https://www.python.org/downloads/release/python-2713/
* Click_ - Command Line Functionality
.. _Click: http://click.pocoo.org
* PyShark_ - PCAP Parsing
.. _PyShark: http://kiminewt.github.io/pyshark/


Authors
-------
* **Alex Hadi** - hadi16_
.. _hadi16: https://github.com/hadi16/


License
-------
This project is licensed under the Apache 2.0 License - see the LICENSE.txt file for details.


Acknowledgments
---------------
* Aaron Wangugi for providing the specifications for the project and assistance whenever needed.
