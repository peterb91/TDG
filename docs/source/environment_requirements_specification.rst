
Environment requirements
========================

*ATA 4.0*


**Notes**


Application Data Generator will be written whole in Python 3.5.3 language with usage of 
GIT  2.11.0. Recommended open-source IDE for developing this project is PyCharm 
Community by JetBrains but if necessary one can use any other editor given.


1. Linux Ubuntu 17.04
---------------------

1.1. Python installation
~~~~~~~~~~~~~~~~~~~~~~~~

It is necessary to download all Python packages by terminal with single command:

        .. code-block:: console
        
                apt-get install python3

Best preceded by:

        .. code-block:: console
        
                apt-get update

To ensure all of our system packages are up to date.

To check if correct Python3 version downloaded properly you need to use command:

        .. code-block:: console
                
                python3 -V

Answer should be: 

        .. code-block:: console
                    
                Python 3.5.3


1.2. Pip installation
~~~~~~~~~~~~~~~~~~~~~

It is necessary to download Pip 9.0.1 by terminal using single command:

        .. code-block:: console
                
                pip install -U pip

1.3. IDE setup
~~~~~~~~~~~~~~

First it is essential to visit JetBrains page:
      https://www.jetbrains.com/pycharm/download/#section=linux

And choose Download button under Community version.
After downloading **tar.gz** archive and unpacking it into preferred folder it is necessary to open 
unpacked folder in console and go into its  **bin**  folder, then execute **pycharm.sh** file with 
command:

.. code-block:: console
                
        ./pycharm.sh

Now it is needed to follow all the installation instructions until it is finished.

1.4. GIT install and setup
~~~~~~~~~~~~~~~~~~~~~~~~~~

It is necessary to download all git packages by terminal with single command:

        .. code-block:: console
        
                apt-get install git

Best preceded by:

        .. code-block:: console
        
                apt-get update

To ensure all of our system packages are up to date.

To check if correct git downloaded properly you need to use command:

        .. code-block:: console
        
                git --version

Answer should be:

        .. code-block:: console
        
                git version 2.11.0

To setup repository it is necessary to use command:

        .. code-block:: console
        
                git clone https://ata40@bitbucket.org/wjaszcz/data-generator-ata_40.git

1.5. Flask and virtual environment install and setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is necessary to download virtual environment using commands:

        .. code-block:: console
        
        pip install virtualenv
        apt-get install python-virtualenv
        apt-get install python3-venv

Next it is needed to make environment directory in place user want to using command:

        .. code-block:: console
        
        python3 -m venv venv

Then it is essential to activate it by command:

        .. code-block:: console
        
        . venv/bin/activate

Next step is installing all additional libraries (look at "2 Additional libraries")

In the end it is needed to enter TDG_web.py file localization and use command:

        .. code-block:: console

        python3 TDG_web.py


2 Additional libraries
----------------------

To install all additions needed to develop project Test Data Generator it is necessary to visit projects localization and then use commands:

        .. code-block:: console

        pip3 install pipenv
        pipenv install --dev
