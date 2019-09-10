Test strategy
=============

1. Identifier
-------------

This is a test strategy for data generator. The document provides the framework for the duration of test and cost of test execution estimation.

2. Introduction
---------------
This document provides the Testing Strategy for Data generator application. It will have an influence on tasks related to test planning, test scripts and test execution.

2.1. Test scope
~~~~~~~~~~~~~~~
All functional and non-functional requirements written in SRS-Requirements must be achieved. 

2.2. Test environment 
~~~~~~~~~~~~~~~~~~~~~
This application will operate on 3 most common OSes, such as: Windows, macOS, UNIX- Linux. In version 1.0 application will work on Linux OS. So v1.0 will be tested on Ubuntu 16.04.3 LTS, which is the same as production environment. Things which need to previously prepared are Python min. 3.*.*.  
   
3. Roles and responsibilities
-----------------------------
Below the groups which take part in project testing process are defined:

.. _roles_and_responsibilities:: 
   :widths: auto
   :align: center  


======================	========================================
Role 	                Responsibilites
====================== 	========================================
Project leader	        - manages resources in whole project
                        - controls the flow of the communication 
                        - plans and execute activities
Quality Assurance Team 	- performs tests
                        - develops test plan and test cases
                        - evaluates the test results
                        - writes and executes automated tests
Developers Team	        - prepares test cases
                        - performs unit tests
======================	========================================

4. Tests approach
-----------------
   #
   
The application will be unit and integration tested before it is delivered to customer’s testing team.

4.1. Test types
~~~~~~~~~~~~~~~

* Unit tests

  The developer’s team shall prepare test cases based on each function or class inside the module. Tests should be performed by developers in development environment. 


* Integration test

  Purpose of integration in large tests is to validate application components compatibility. All systems in application shall be integrated in test environment. 
  This level also includes performance tests, time responses of systems, application behavior under heavy traffic. User friendly interface to be tested by SMEs.


* System test

  System test will be performed by QA team in test environment to ensure predictable results and that the entire integrated software system meets requirements. 


* Acceptance test

  Acceptance testing may be performed by a third party for acceptance testing requirements. UAT shall be conducted to gain acceptance of all functionality from the user community. UAT shall verify that the system meets user requirements as specified and based on the results, the customer can decide whether to accept or decline the application.

.. _test_types::
   :widths: auto
   :align: center

================= ============================ =======================================  
Test type	  Entry Criteria               Exit Criteria
================= ============================ =======================================
Unit tests	  component/classes design     100% executed, min. 60% covered
Integration test  100% unit tests executed, 
                  functional design            0 critical defects, 0 major defects
System test	  architecture of application,
                  0 critical and major defects
	                                       100% compatible with working software,
                                               All business requirements have been met
                                               (100% coverage),
                                               0 critical and major defects,
                                               100% test cases run successfully
Acceptance test	  working application	       100% passed 
                                               100% requirements covered
================= ============================ =======================================                                             

4.2. Test methods
~~~~~~~~~~~~~~~~~
* manual testing
* automated testing

4.3.  Acceptance criteria
~~~~~~~~~~~~~~~~~~~~~~~~~
* 100% business requirements covered
* 100% critical defects solved
* 100% of test cases passed

5. Test deliverables
--------------------

* set-up of test environment
* test strategy
* test plan
* test cases
* test scripts
* test results in pdf format
* test logs and report
* defects logged in Jira
* test coverage measurement


6. Assumptions
--------------

The following assumptions were made about the testing effort:

#. The testers will control all data loads, test runs, etc.
#. Application knowledgeable (client) personnel are available per agreed upon schedules.
#. No changes to production will take place during testing.
#. If any changes to production programs are required, the conversion and testing schedules will be reviewed and may have to be modified.

7. Constrains
-------------
The following constraints apply to the testing effort:

#. All testing must be completed by TBD.

8. Dependencies
---------------

The testing effort contains the following dependencies that are external to the test team:

#. Test Hardware has been identified
#. All Software for the testing effort has been identified
#. Database identified

9. Test schedule 
----------------

.. _test_schedule::
   :widths: auto
   :align: center

============================ ===========   
Test step description	     Sprint num.
============================ ===========
Test planning 	             1
Test case development	     1
Test environment preparation 1
Test execution	             1
Test results analysis	     2
Management reporting	     2
============================ ===========

10. Test risks
--------------

The following risk and issues must be managed during the testing effort:

.. _test_risks::
   :widths: auto
   :align: center

+--------------------------+-------------------------+----------------------+
| Risk                     | Mitigation              | Contingency          |
+==========================+=========================+======================+
| Test environment may not | After each code release | Application not      |
| be the same as production| check test environment. | tested properly.     |
| environment.		   |                         |                      |
+--------------------------+-------------------------+----------------------+
| Lack of time to test all | Keep track of tests and | Not all functionality| 
| functionality.           | work duration, make some| tested.              |
|                          | prediction.             |                      |
+--------------------------+-------------------------+----------------------+
| Lost of project control  | Keep track of test.     | Application not      |
|                          |                         | tested properly.     |
+--------------------------+-------------------------+----------------------+





