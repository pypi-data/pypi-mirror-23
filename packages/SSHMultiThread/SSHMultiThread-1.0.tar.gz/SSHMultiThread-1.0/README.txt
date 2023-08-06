================
CAPACITY REPORT
================

Generates report about the account and server utilisation

-----------

A MultiThreaded program to fetch the data by SSH to remote machines and executing commands.
The number of threads are configurable and the program is optimize to use the best system resources.
This is more like of template, I can't post exact content of the script as it may have some confidential information.
In the version 2.0 I will be providing a working script with some demo use case.

Pre-requisite
===============

Please get the below files with the content as specified:

* commands.ini:  ssh#-o#UserKnownHostsFile=/dev/null#-o#StrictHostKeyChecking=no#-o#ConnectTimeout=25#root@192.168.2.101#free -g | awk '/Mem:/ {print $2}'

* inventory.ini: In the below format

[clustername2]

customer:Pandey

host:cluster02


Execution & Output
-------------------

arjun$ python capacity.py

It generates CSV, JSON intermediates file and final HTML report.


