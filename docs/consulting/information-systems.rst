
.. index:: Information Systems
.. _information-systems:

Information Systems
---------------------
https://en.wikipedia.org/wiki/Information_systems#Types_of_information_systems

https://en.wikipedia.org/wiki/List_of_collaborative_software


.. index:: Information Systems Glossary
.. _information-systems-glossary:

Information Systems Glossary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. TODO: split this to software-development / web-development
.. ... / computer-science

.. glossary::

   System
      An interconnected graph of nodes linked with edges through which
      flow produces predictable and unpredictable behaviors.

      https://en.wikipedia.org/wiki/System

   Information System
      A system with information inputs and outputs
      designed to solve a problem.

      https://en.wikipedia.org/wiki/Information_system

   Information Technology
      Hardware and software information systems for solving business problems.

      https://en.wikipedia.org/wiki/Information_technology

   Application
      An application of technology for a particular domain.

   App
      See :term:`Application`

   Operating System
      Software for running applications and working with devices.

      https://en.wikipedia.org/wiki/Operating_system

   API
      Advanced Programming Interface.
      A specification for inputs and outputs provided by a system
      component.

      An API specification is specified, versioned, updated, and
      deprecated.

      A reference implementation implements a model copy of an API.

      If a component utilizes an API
      it is said to be written against, with, or on top of said API.

      An API abstracts a lower-level in order to provide a higher-level
      API.

      One primary advantage of an API is that, ideally,
      system components are loosely coupled and thus interchangeable
      and incrementally upgradeable.

      https://en.wikipedia.org/wiki/Application_programming_interface

      https://en.wikipedia.org/wiki/Loose_coupling

      `<https://en.wikipedia.org/wiki/Abstraction_(computer_science)>`__

   Operating System API
      An :term:`API` provided by one or more
      :term:`Operating Systems <Operating System>`.

      Examples:

      * https://en.wikipedia.org/wiki/POSIX
      * https://en.wikipedia.org/wiki/Windows_API

   Language API
      An :term:`API` provided by or for one or more programming languages
      through a *standard library* or a third-party component.

      Examples:

      * https://en.wikipedia.org/wiki/WebGL

      https://en.wikipedia.org/wiki/Public_interface

      `<https://en.wikipedia.org/wiki/Protocol_(object-oriented_programming)>`__

      https://en.wikipedia.org/wiki/Standard_library

   Web API
      An :term:`API` for interacting with local (browser) or remote
      (e.g. :ref:`HTTP <http>`) components.

      One primary advantage of a Web API is that *downstream components*
      do not need to know anything about the underlying
      :term:`Operating System APIs <Operating System API>` and
      :term:`Language APIs <Language API>`.

      https://en.wikipedia.org/wiki/Web_API

   Web Service
      A :term:`Web API` with a formal specification.

      Generally provided over :ref:`HTTP`,
      traditionally (as in the *enterprisey* ``WS-*`` standards)
      with :ref:`XML`, but, more recently, with :ref:`JSON`.

      https://en.wikipedia.org/wiki/Web_service

   RESTful API
      Also REST API. A :term:`Web API` that abides by best-practice guidelines
      for interacting with *resources* through standard :ref:`HTTP`
      methods like ``PUT``/``POST``, ``GET``, ``POST``/``PUT``, ``DELETE``.

      Many web developers prefer RESTful APIs because
      the standard methods and error messages
      specified by :ref:`HTTP` are already implemented
      by existing, well-tested libraries
      available for most languages.

      https://en.wikipedia.org/wiki/Representational_state_transfer

      https://en.wikipedia.org/wiki/Create,_read,_update_and_delete


.. _is-criteria:

Criteria
~~~~~~~~~
* ROI (Returns/Cost :: Output/Input)
* Need / Want
* Maintainability


.. _is-roi:

ROI
++++
The investment should be justified by gains in productivity / efficiency.

Productivity / Efficiency::

    output / input

Hours, Units, Dollars

https://en.wikipedia.org/wiki/Productivity

See: :ref:`Business > ROI <business-roi>`


Need / Want
++++++++++++
Communication and collaboration are essential to success.


.. index:: Maintainability
.. _maintainability:

Maintainability
++++++++++++++++

Choosing Components

* In n-years, will I be able to find someone who can maintain this?

  * Locally? Globally?
  * Job listing keyword search [rough approximation]
  * Job board search

* In n-years, will there still be a community supporting these
  components?
* Is it open source? How do we find/pay/train someone to understand
  how it works?
* Is there a *non-profit* software foundation behind this component?


.. index:: Clouds
.. _clouds:

Clouds
~~~~~~~
https://en.wikipedia.org/wiki/Cloud_computing

https://en.wikipedia.org/wiki/Cloud_computing#Service_models

Why would I want to run my business "in the cloud"?

What are our core competencies?

Do we need/want to run this all ourselves?

Would it be more safe/secure to outsource the management of these
business systems?

Application layers:

* Application
* Platform (Database, APIs)
* Infrastructure (Physical and Virtual Servers)


.. index:: Software-as-a-Service
.. index:: SaaS
.. _SaaS:

Software-as-a-Service
+++++++++++++++++++++++
https://en.wikipedia.org/wiki/Software_as_a_service

Example: GMail is software hosted as a service on Google's
infrastructure; there's no need to internally pay for and manage servers in a
datacenter anywhere.

https://en.wikipedia.org/wiki/Application_service_provider


.. index:: Platform-as-a-Service
.. index:: PaaS
.. _PaaS:

Platform-as-a-Service
++++++++++++++++++++++
https://en.wikipedia.org/wiki/Platform_as_a_service

Platform-as-a-Service providers abstract a bit further in that they
provide an implementation of platform APIs on top of which applications
can be developed and hosted.

Heroku, AppEngine and AppScale are examples of Platforms-as-a-Service.


.. index:: Infrastructure-as-a-Service
.. index:: IaaS
.. _IaaS:

Infrastructure-as-a-Service
+++++++++++++++++++++++++++++++++++++
https://en.wikipedia.org/wiki/Category:Cloud_infrastructure

Infrastructure-as-a-Service providers provide a bit more than regular
hosting services in that they offer something like virtual datacenter
resources.

Amazon Web Services (AWS), Rackspace, and Google Compute Engine
are examples of
Infrastructure-as-a-Service: they provide servers, networks, and
redundant storage systems on top of which IT systems can be
developed, tested, and deployed.


.. index:: Configuration Management
.. _configuration-management:

Configuration Management
++++++++++++++++++++++++++
https://en.wikipedia.org/wiki/Configuration_management#Software

https://en.wikipedia.org/wiki/Software_configuration_management

https://en.wikipedia.org/wiki/Comparison_of_open-source_configuration_management_software


.. index:: Information Security
.. _information-security:

Information Security
~~~~~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Information_security

Managing risk and uncertainty.

Standards:

* https://en.wikipedia.org/wiki/Statement_on_Auditing_Standards_No._70:_Service_Organizations
* https://en.wikipedia.org/wiki/Evaluation_Assurance_Level
* https://en.wikipedia.org/wiki/Cloud_computing_security


.. index:: Confidentiality
.. _confidentiality:

Confidentiality
++++++++++++++++
https://en.wikipedia.org/wiki/Confidentiality


.. index:: Integrity
.. _integrity:

Integrity
++++++++++
https://en.wikipedia.org/wiki/Data_integrity


.. index:: Availability
.. _availability:

Availability
+++++++++++++
https://en.wikipedia.org/wiki/Availability

https://en.wikipedia.org/wiki/Service-level_agreement


.. index:: Business Continuity
.. _business-continuity:

Business Continuity
~~~~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Business_continuity

https://en.wikipedia.org/wiki/Business_continuity_planning

https://en.wikipedia.org/wiki/Disaster_recovery

See: `Information Security`_ (`Availability`_)


.. index:: Backups
.. _backups:

Backups
++++++++
https://en.wikipedia.org/wiki/Backup


.. index:: Reliability
.. _reliability:

Reliability
+++++++++++
https://en.wikipedia.org/wiki/Reliability_engineering

`<https://en.wikipedia.org/wiki/Redundancy_(engineering)>`_


.. index:: Scenarios
.. _scenarios:

Scenarios
+++++++++++
https://en.wikipedia.org/wiki/Scenario_planning


.. index:: Business Systems
.. _business-systems:

Business Systems
~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Online_office_suite

https://en.wikipedia.org/wiki/Comparison_of_office_suites


.. index:: Google Apps
.. _google-apps:

Google Apps
+++++++++++++

* $5/user/month // $50/user/year
* gmail (e.g. username@example.org)

  * can add aliases (e.g. webmaster@example.org -> username@example.org)
  * can setup forwarding (e.g. username@example.org -> username@gmail.com)

* mail, contacts, chat, calendar, drive, docs, sheets, slides,
  groups, sites

  * drive: online storage
  * sites: (e.g. employees.example.org)

    * update through web interface
    * file sharing (employee handbook pdf)

  * groups: [employee] emailing list

    * don't need accounts for every employee, they can use their
      own email addresses (everything gets relayed)
    * basically like archived emails with always on reply-all

* http://google.com/a
* http://learn.googleapps.com/

* https://www.google.com/enterprise/marketplace/

.. index:: Handling Money
.. index:: Transaction Processing
.. _handling-money:

Handling Money
~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Transaction_processing

https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard


.. index:: Accounting
.. _accounting:

Accounting
+++++++++++
https://en.wikipedia.org/wiki/Accounting

https://en.wikipedia.org/wiki/Double-entry_bookkeeping_system

https://en.wikipedia.org/wiki/Accountant

https://en.wikipedia.org/wiki/Financial_statement

https://en.wikipedia.org/wiki/Business_valuation


.. index:: GNUCash
.. _GNUCash:

GNUCash
`````````
https://en.wikipedia.org/wiki/GnuCash

* Free and Open Source
* Personal Accounting
* Small Business Accounting


.. index:: Quicken
.. _Quicken:

Quicken
`````````
https://en.wikipedia.org/wiki/Quicken

* Personal Accounting
* USA Version
* International Versions


.. index:: QuickBookx
.. _QuickBooks:

QuickBooks
````````````
https://en.wikipedia.org/wiki/QuickBooks

* Small Business Accounting
* Square integrates with QuickBooks
* http://www.google.com/enterprise/marketplace/search?query=quickbooks


.. index:: FreshBooks
.. _freshbooks:

FreshBooks
````````````
https://en.wikipedia.org/wiki/FreshBooks

* Cloud accounting
* Online Invoicing, Accounting & Billing Software
* Time Tracking
* Export to QuickBooks
* http://community.freshbooks.com/addons/


.. index:: Payments
.. _payments:

Payments
++++++++++


.. index:: Amazon Payments
.. _amazon-payments:

Amazon Payments
`````````````````
https://en.wikipedia.org/wiki/Amazon_Payments


.. index:: Apple Pay
.. _apple-pay:

Apple
``````
https://en.wikipedia.org/wiki/Apple_Pay


.. index:: Google Wallet
.. index:: Google Checkout
.. index:: Google Offers
.. _google-wallet:

Google Wallet
``````````````
https://en.wikipedia.org/wiki/Google_Wallet

https://en.wikipedia.org/wiki/Google_Checkout

* http://www.google.com/wallet/business/payments/
* http://www.google.com/wallet/business/offers/index.html

  * similar to Groupon, LivingSocial


.. index:: PayPal
.. _paypal:

PayPal
```````
https://en.wikipedia.org/wiki/PayPal


.. index:: Square
.. _square:

Square
````````
`<https://en.wikipedia.org/wiki/Square,_Inc.>`_

* Square Reader (plugs into headphone jack)
* Square Register (app)


.. index:: Sales Information Systems
.. _sales-information-systems:

Sales
~~~~~~~
* https://en.wikipedia.org/wiki/Sales_process_engineering
* https://en.wikipedia.org/wiki/Group_information_management
* https://en.wikipedia.org/wiki/Personal_information_management
* https://en.wikipedia.org/wiki/Sales_pipeline
* https://en.wikipedia.org/wiki/Sales_intelligence
* https://en.wikipedia.org/wiki/Sales_force_management_system

See: :ref:`CRM <crm>`


.. index:: Customer Relationship Management
.. index:: CRM
.. _crm:

Customer Relationship Management (CRM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Customer_relationship_management

* https://en.wikipedia.org/wiki/Contact_list
* https://en.wikipedia.org/wiki/Address_book
* https://en.wikipedia.org/wiki/Contact_manager
* https://en.wikipedia.org/wiki/Opt-in_email
* https://en.wikipedia.org/wiki/Mailing_list
* https://en.wikipedia.org/wiki/Customer_service#See_also
* https://en.wikipedia.org/wiki/Comparison_of_CRM_systems
* https://en.wikipedia.org/wiki/Customer_intelligence
* https://en.wikipedia.org/wiki/Customer_experience


.. index:: Business Intelligence
.. index:: BI
.. _business-intelligence:

Business Intelligence
~~~~~~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Business_intelligence

See: :ref:`Data Science <data-science>`

See: :ref:`Knowledge Engineering <knowledge-engineering>`