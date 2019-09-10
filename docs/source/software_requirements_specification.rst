
Software Requirements Specification
====================================

| *Version 1.0 approved*
| *Version 2.0 approved*
| *Version 3.0 approved*
| *Version 3.1 approved*


Prepared by:

| Teresa Bury 
| Mateusz Grabon
| Daria Radoszewska


| Akamai Technical Academy
| 18.08.2017

Change log

+------------------+------------+----------------------------+-------------+
| Name (Jira task) | Date       | Reason For Changes         | Version     |
+==================+============+============================+=============+
| ATASCRUM1-9      | 23.08.2017 | Document created           | Version 1.0 |
+------------------+------------+----------------------------+-------------+
| ATASCRUM1-84     | 18.09.2017 | Shift in goals and         | Version 2.0 |
|                  |            | priorities after Sprtint 1 |             |
+------------------+------------+----------------------------+-------------+
| ATASCRUM1-198    | 6.10.2017  | Added registration and     | Version 3.0 |
|                  |            | login functionalities, as  |             |
|                  |            | well as user administration|             |
|                  |            | panel                      |             |
+------------------+------------+----------------------------+-------------+
| ATASCRUM1-209    | 10.10.2017 | MOD-3.REQ-8 required more  | Version 3.1 |
|                  |            | claryfication              |             |
+------------------+------------+----------------------------+-------------+

|

1. Introduction
---------------

1.1. Purpose
~~~~~~~~~~~~

This requirements specification document describes the functions and requirements specified for Data Generator tool. This Data Generator is needed to help testing login functionality. In order to make this possible the tool will create certain amount of positive and negative test data for login and password.

1.2. Definitions, Acronyms and Abbreviations 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **CLI** - Command Line Interface
* **DG** - Data Generator
* **GUI** - Graphical User Interface
* **SRS** - Software Requirements Specification
* **User** - person intended to use Data Generator tool
* **DGWS** - Data Generator Web Service

1.3. Intended Audience and Reading Suggestions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This document is intended for: developers, project managers, users, testers, and documentation writers. Sections of this SRS consist of the following information: general introduction, overall description, external interface requirements, system features, other nonfunctional requirements.

1.4. Product Scope
~~~~~~~~~~~~~~~~~~

This Data Generator shall create certain amount of test data for login and password. The user can determine positive/negative credentials constraints to check login functionality, such as: number of characters, type of characters, for both login and password features. DG tool lets user choose output file format, ratio of positive and negative data, amount of records.

2. Overall Description
----------------------

2.1. Product Perspective
~~~~~~~~~~~~~~~~~~~~~~~~

Data generator is a self-contained product. Scope of Version 1.0 contains CLI tool deployed on Users personal computer and does not relate to any larger system. Version 2.0 expects from developers team to provide service in form of web application(Data Generator Web Service) with functionality of DG.

2.2. Product Functions
~~~~~~~~~~~~~~~~~~~~~~

* Lets user enter parameters
* Lets user choose output file format
* Generates file with specified amount of records

2.3. User Classes and Characteristics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data generator is meant to be used by User, who is not familiar with programming. Installation, user guide shall be created in manner that grants full usability of product to unproficient user.

2.4. Operating Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~

System requirements for DG CLI:

* **OS: Debian based GNU/Linux distribution**
* **Python 3.5 or higher**

Requirements for accessing DGWS:

* **Internet connection**
* **Google Chrome 61 web browser**

2.5. User Documentation
~~~~~~~~~~~~~~~~~~~~~~~

User documentation will consist of installation guide and user manual. Both documents will be provided in .pdf format and will guide the user through installation process and describe program functionalities.

2.6. Assumptions and Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Version 1.0 does not depend on any other, since it is first version of our product. However important factor from architectural view is to prepare product structure for future versions.

3. External Interface Requirements
----------------------------------

3.1. User Interfaces
~~~~~~~~~~~~~~~~~~~~

**Version 1.0** - The only way for user to communicate with DG is by Command Line Interface. List of input questions shall be displayed.

**Version 2.0** - DGWS will be delivered with all the funtionalities of DG CLI provided in **version 1.0**.

3.2. Machine-to-Machine Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Version 1.0 does not provide any external API.



4. Autonomic modules
--------------------


========= ================================================ ========
Module id Module name                                      Priority 
========= ================================================ ========
MOD-1     Command Line Interface DG application (DG CLI)   High
MOD-2     Graphical User Interface DG application (DG GUI) Low
MOD-3     Data Generator Web Service (DGWS)                High
========= ================================================ ========


4.1 Command Line Interface DG application(MOD-1) Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============== ========================================== ========
Requirement id System feature name                        Priority 
============== ========================================== ========
MOD-1.REQ-1    User-application interaction               High
MOD-1.REQ-2    Constraints gathering                      High
MOD-1.REQ-3    Test data generation                       High
MOD-1.REQ-4    Output file generation                     High
MOD-1.REQ-5    Generated data storage in database         Low
MOD-1.REQ-6    Saving configuration file option           Low
MOD-1.REQ-7    Multi-field (not only login & password)    Low
============== ========================================== ========

4.1.1 Communication with user (MOD-1.REQ-1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ================================================================== ========
Requirement id System feature name                                                Priority
============== ================================================================== ========
MOD-1.REQ-1.1  Command Line Interface (CLI) communication with user               High
MOD-1.REQ-1.2  Configuration file                                                 Low
============== ================================================================== ========


4.1.2 Constraints application (MOD-1.REQ-2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ==================================================================== ========
Requirement id System feature name                                                  Priority
============== ==================================================================== ========
MOD-1.REQ-2.1  User can choose number of characters in Login (maximum value = 50)   High    
MOD-1.REQ-2.2  User can choose number of characters in Password                     High
               (maximum value = 50)
MOD-1.REQ-2.3  User can decide if special symbols (not alphanumeric) from ASCII     High
               table should be enclosed and which ones
MOD-1.REQ-2.4  User can choose number of records generated (maximum value = 1000)   High
MOD-1.REQ-2.5  User can choose the ratio of positive to negative data generated	    High
MOD-1.REQ-2.6  User decides if chosen constraints are same or separate for the      Low
               Password and Login
============== ==================================================================== ========


4.1.3 Test data generation (MOD-1.REQ-3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ============================================================= ========
Requirement id System feature name                                           Priority
============== ============================================================= ========
MOD-1.REQ-3.1  Randomly chooses length, based on neg/pos ratio	             High
MOD-1.REQ-3.2  Randomly chooses characters                                   High
MOD-1.REQ-3.3  Handle exception related to Non-ASCII character in input data Medium
============== ============================================================= ========

4.1.4 Output file generation (MOD-1.REQ-4)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ============================================================= ========
Requirement id System feature name                                           Priority
============== ============================================================= ========
MOD-1.REQ-4.1  One file for positive and negative data                       Medium
MOD-1.REQ-4.2  User can choose an output format (\*.csv, \*.txt)             Medium
MOD-1.REQ-4.3  File format: Login, flag(P\N Positive\Negative), Password,    High
               flag(P\N Positive\Negative); comma separated values
MOD-1.REQ-4.4  User can choose if columns in file will have headers          Low
============== ============================================================= ========


4.1.5 Saving and loading configuration file option (MOD-1.REQ-5)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ============================================================= ========
Requirement id System feature name                                           Priority
============== ============================================================= ========
MOD-1.REQ-5.1  Read current parameters state and saves it in config file     Low
MOD-1.REQ-5.2  Config file can be loaded and the parameters will be updated  Low
MOD-1.REQ-5.3  Config saver/loader can handle multi fields (REQ-6)           Low
============== ============================================================= ========


4.1.6 Registration extension (multi-field mode) (MOD-1.REQ-6)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ====================================================================== ========
Requirement id System feature name                                                    Priority
============== ====================================================================== ========
MOD-1.REQ-6.1  User can customize number and type of fields                           Low
MOD-1.REQ-6.2  Every field can have separate constraints                              Low
MOD-1.REQ-6.3  Each field shall be labeled by user provided name                      Low
============== ====================================================================== ========


4.2 Graphical User Interface DG application(MOD-2) Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============== ========================================== ========
Requirement id System feature name                        Priority 
============== ========================================== ========
MOD-2.REQ-1    User-application interaction               High
MOD-2.REQ-2    Constraints gathering                      High
MOD-2.REQ-3    Test data generation                       High
MOD-2.REQ-4    Output file generation                     High
MOD-2.REQ-5    Saving configuration file option           Low
MOD-2.REQ-6    Multi-field (not only login & password)    Low
============== ========================================== ========


4.2.1 Communication with user (MOD-2.REQ-1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ================================================================== ========
Requirement id System feature name                                                Priority
============== ================================================================== ========
MOD-2.REQ-1.1  Graphical User Interface (GUI) communication with user             High
MOD-2.REQ-1.2  Configuration file                                                 Low
============== ================================================================== ========


4.2.2 Constraints application (MOD-2.REQ-2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ==================================================================== ========
Requirement id System feature name                                                  Priority
============== ==================================================================== ========
MOD-2.REQ-2.1  User can choose number of characters in Login (maximum value = 50)   High    
MOD-2.REQ-2.2  User can choose number of characters in Password                     High
               (maximum value = 50)
MOD-2.REQ-2.3  User can decide if special symbols (not alphanumeric) from ASCII     High
               table should be enclosed and which ones
MOD-2.REQ-2.4  User can choose number of records generated (maximum value = 1000)   High
MOD-2.REQ-2.5  User can choose the ratio of positive to negative data generated     High
MOD-2.REQ-2.6  User decides if chosen constraints are same or separate for the      Low
               Password and Login
============== ==================================================================== ========


4.2.3 Test data generation (MOD-2.REQ-3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ============================================================= ========
Requirement id System feature name                                           Priority
============== ============================================================= ========
MOD-2.REQ-3.1  Randomly chooses length, based on neg/pos ratio               High
MOD-2.REQ-3.2  Randomly chooses characters                                   High
MOD-2.REQ-3.4  Handle exception related to Non-ASCII character in input data Medium
============== ============================================================= ========


4.2.4 Output file generation (MOD-2.REQ-4)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ============================================================= ========
Requirement id System feature name                                           Priority
============== ============================================================= ========
MOD-2.REQ-4.1  One file for positive and negative data                       Medium
MOD-2.REQ-4.2  User can choose an output format (\*.csv, \*.txt)             Medium
MOD-2.REQ-4.3  File format: Login, flag(P\N Positive\Negative), Password,    High
               flag(P\N Positive\Negative); comma separated values
MOD-2.REQ-4.4  User can choose if columns in file will have headers          Low
============== ============================================================= ========


4.2.5 Saving and loading configuration file option (MOD-2.REQ-5)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ============================================================ ========
Requirement id System feature name                                          Priority
============== ============================================================ ========
MOD-2.REQ-5.1  Read current parameters state and saves it in config file    Low
MOD-2.REQ-5.2  Config file can be loaded and the GUI fields will be updated Low
MOD-2.REQ-5.3  Config saver/loader can handle multi fields (REQ-6)          Low
============== ============================================================ ========


4.2.6 Registration extension (multi-field mode) (MOD-2.REQ-6)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ====================================================================== ========
Requirement id System feature name                                                    Priority
============== ====================================================================== ========
MOD-2.REQ-6.1  User can customize number and type of fields                           Low
MOD-2.REQ-6.2  Every field can have separate constraints                              Low
MOD-2.REQ-6.3  Each field shall be labeled by user provided name                      Low
============== ====================================================================== ========


4.3 Data Generator Web Service (MOD-3) Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


============== ========================================== ========
Requirement id System feature name                        Priority 
============== ========================================== ========
MOD-3.REQ-1    User-application interaction               High
MOD-3.REQ-2    Constraints gathering                      High
MOD-3.REQ-3    Test data generation                       High
MOD-3.REQ-4    Output file generation                     High
MOD-3.REQ-5    Generated data storage in database         Low
MOD-3.REQ-6    Saving configuration file option           Low
MOD-3.REQ-7    Multi-field (not only login & password)    Low
MOD-3.REQ-8    User registration                          High
MOD-3.REQ-9    User login                                 High
MOD-3.REQ-10   User administration panel                  High
============== ========================================== ========


4.3.1 Communication with user (MOD-3.REQ-1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== =========================================================== ========
Requirement id System feature name                                         Priority
============== =========================================================== ========
MOD-3.REQ-1.1  Web Graphical User Interface                                High
MOD-3.REQ-1.2  Web Service interatcting with User through Google Chrome 61 High
============== =========================================================== ========


4.3.2 Constraints application (MOD-3.REQ-2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ==================================================================== ========
Requirement id System feature name                                                  Priority
============== ==================================================================== ========
MOD-3.REQ-2.1  User can choose number of characters in Login (maximum value = 50)   High    
MOD-3.REQ-2.2  User can choose number of characters in Password                     High
               (maximum value = 50)
MOD-3.REQ-2.3  User can decide if special symbols (not alphanumeric) from ASCII     High
               table should be enclosed and which ones
MOD-3.REQ-2.4  User can choose number of records generated (maximum value = 1000)   High
MOD-3.REQ-2.5  User can choose the ratio of positive to negative data generated     High
MOD-3.REQ-2.6  User decides if chosen constraints are same or separate for the      Low
               Password and Login
============== ==================================================================== ========


4.3.3 Test data generation (MOD-3.REQ-3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

============== ============================================================= ========
Requirement id System feature name                                           Priority
============== ============================================================= ========
MOD-3.REQ-3.1  Randomly chooses length, based on neg/pos ratio               High
MOD-3.REQ-3.2  Randomly chooses characters                                   High
MOD-3.REQ-3.4  Handle exception related to Non-ASCII character in input data Medium
============== ============================================================= ========


4.3.4 Output file generation (MOD-3.REQ-4)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

============== ============================================================= ========
Requirement id System feature name                                           Priority
============== ============================================================= ========
MOD-3.REQ-4.1  One file for positive and negative data                       Medium
MOD-3.REQ-4.2  User can choose an output format (\*.csv, \*.txt)             Medium
MOD-3.REQ-4.3  File format: Login, flag(P\N Positive\Negative), Password,    High
               flag(P\N Positive\Negative); comma separated values
MOD-3.REQ-4.4  User can choose if columns in file will have headers          Low
============== ============================================================= ========


4.3.5 Generated data storage in database (MOD-3.REQ-5)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ======================================================================= ========
Requirement id System feature name                                                     Priority
============== ======================================================================= ========
MOD-3.REQ-5.1  Creates relational database file                                        Low
MOD-3.REQ-5.2  Labels table headers with user provided names (separate for each field) Low
MOD-3.REQ-5.3  Fills database with generated records                                   Low
============== ======================================================================= ========


4.3.6 Saving and loading configuration file option (MOD-3.REQ-6)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ============================================================ ========
Requirement id System feature name                                          Priority
============== ============================================================ ========
MOD-3.REQ-6.1  Read current GUI fields state and saves it in a config file  Low
MOD-3.REQ-6.2  Config file can be loaded and the GUI fields will be updated Low
MOD-3.REQ-6.3  Config saver/loader can handle multi fields (REQ-7)          Low
============== ============================================================ ========


4.3.7 Multi-field mode (MOD-3.REQ-7)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ====================================================================== ========
Requirement id System feature name                                                    Priority
============== ====================================================================== ========
MOD-3.REQ-7.1  User can customize number and type of fields                           Low
MOD-3.REQ-7.2  Every field can have separate constraints                              Low
MOD-3.REQ-7.3  Each field shall be labeled by user provided name                      Low
============== ====================================================================== ========


4.3.8 User registration (MOD-3.REQ-8)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ====================================================================== ========
Requirement id System feature name                                                    Priority
============== ====================================================================== ========
MOD-3.REQ-8.1  User can register to a webservice using chosen unique username, unique High
               e-mail and password
MOD-3.REQ-8.2  Username has to be at least 4 characters long and cannot exceed        High
               15 characters
MOD-3.REQ-8.3  Username string is case insensitive                                    High
MOD-3.REQ-8.4  User can use email address complaint with `IEFT RFC 5322`__            High
MOD-3.REQ-8.5  Password has to be at least 6 characters long and cannot exceed        High
               15 characters
MOD-3.REQ-8.6  Both username and password can consist alphanumeric characters and     High
               punctuation characters that are listed between quotes:
               "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
MOD-3.REQ-8.7  Every field in a form has to be validated on frontend and backend site Medium
============== ====================================================================== ========

.. __: https://tools.ietf.org/html/rfc5322

4.3.9 User login (MOD-3.REQ-9)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ====================================================================== ========
Requirement id System feature name                                                    Priority
============== ====================================================================== ========
MOD-3.REQ-9.1  User can login to a webservice using created previously account        High
MOD-3.REQ-9.2  Every field in a form has to be validated on frontend and backend site Medium
============== ====================================================================== ========


4.3.10 User administration panel (MOD-3.REQ-10)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


============== ====================================================================== ========
Requirement id System feature name                                                    Priority
============== ====================================================================== ========
MOD-3.REQ-10.1 After sucessful login user can navigate to administration panel        High
MOD-3.REQ-10.2 User can browse files generated while being logged                     High
MOD-3.REQ-10.3 User can change e-mail and/or password while being logged              High
MOD-3.REQ-10.4 User can delete owned account while being logged                       Medium
MOD-3.REQ-10.5 User can change avatar while being logged            	              Low
MOD-3.REQ-10.6 After sucessful login previous ip and login date is being displayed    Medium
============== ====================================================================== ========
