# General 

In this document, we will refer to the absolute file
system path in which this file lies as $PRJ_ROOT. We
call this path the project root.


# Installation

* First clone the backend project from the GitLab
  server by

> git clone git@gitlab.com:fleet-monitor/backend.git

* Open a console and switch to $PRJ_ROOT

* Install the project (creation of virtual Python environment,
  setting of the environment variable PYTHONPATH) via the make target 'install' by

> (linux)   : python3 make.py install .
> (windows) : python make.py install .

  After the execution is finished, you have a new folder
  venv/ in your project root.

  NOTE: In order for the install target to work on linux, make 
        sure that the 'virtualenv' package is installed. If you 
        want to install it, execute

> sudo apt-get install virtualenv .

  NOTE: In order for the install target on windows to work, 
        install the 'virtualenv' package in the global Python 
        interpreter by

> pip install virtualenv .

* Switch to the virtual Python environment assuming you are in $PRJ_ROOT by

> (linux)   : source venv/bin/activate .
> (windows) : source venv/Scripts/activate .

