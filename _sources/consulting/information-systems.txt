
.. index:: IS
.. index:: Information Systems
.. _information systems:

Information Systems
---------------------
| Wikipedia: https://en.wikipedia.org/wiki/Information_systems

* https://en.wikipedia.org/wiki/Information_systems#Types_of_information_systems
* https://en.wikipedia.org/wiki/List_of_collaborative_software


.. index:: Information Systems Glossary
.. _information systems glossary:

Information Systems Glossary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. glossary::

   System
      An interconnected graph of nodes linked with edges through which
      flow produces predictable and unpredictable behaviors.

      https://en.wikipedia.org/wiki/System

   Infrastructure
      Core :term:`system` components.

   Information
      Not noise.

      See: :ref:`data science` > :ref:`information theory`,
      :ref:`knowledge engineering`

   Information System
      A :term:`system` with :term:`information` inputs and outputs
      designed to solve a problem.

      https://en.wikipedia.org/wiki/Information_system

   Information Technology
      Hardware and software :term:`information systems <information
      system>`
      for solving business problems.

      https://en.wikipedia.org/wiki/Information_technology

   Application
      An application of technology for a particular domain.

   App
      See :term:`Application`

   Operating System
      Software for running :term:`applications <application>`
      and working with devices.

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
      (e.g. :ref:`HTTP`) components.

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

   Webhook
      A webhook is an HTTP message for an event.

      :term:`web services <web service>` and :term:`applications
      <application>` can send webhooks when e.g. a change occurs.

      For example, when GitHub, ReadTheDocs, and Travis-CI
      are configured (with webhooks) a change pushed to a
      GitHub repository branch or pull request
      enqueues a build at e.g. ReadTheDocs and/or Travis-CI
      (and GitHub can show the build status as a linked icon).

      In terms of :term:`web services <web service>`,
      a webhook is usually just a :ref:`JSON` ``POST``
      to a :term:`URL`; with an access token.

   RESTful API
      A RESTful API (*REST API*) is a
      :term:`Web API` that abides by best-practice guidelines
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

Units: Hours, Units, Dollars (see: :ref:`qudt`)

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
.. index:: Cloud Computing
.. _clouds:

Clouds
~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Cloud_computing

https://en.wikipedia.org/wiki/Cloud_computing#Service_models


Cloud Questions
++++++++++++++++

* Why would I want to run my business "in the cloud"?
* What are our core competencies?
* Do we need/want to run this all ourselves?
* Would it be more safe/secure to outsource the management of these
  business systems?


.. index:: Cloud Application Layers
.. _cloud application layers:

Cloud Application Layers
++++++++++++++++++++++++++

* :term:`Applications <application>` Layer

  * https://github.com/wrdrd/wrd/blob/master/app.yaml
    (AppEngine/AppScale)

* Platform Layer

  * :ref:`PaaS` APIs (:ref:`AppEngine`, :ref:`AppScale`, :ref:`Heroku`)
  * :ref:`Databases`
    (:ref:`relational databases`,
    :ref:`sql`,
    :ref:`nosql`,
    :ref:`graph databases`,
    :ref:`triplestores`,
    :ref:`sparql`)
  * Authz: Authentication, Authorization

    * Servers: OpenLDAP, 389, FreeIPA, ActiveDirectory, Samba4
    * Standards: WebID, OAuth, SASL, SAML, LDAP
    * Infrastructure Layer: :ref:`OpenStack` Keystone

  * Email

    * AppEngine/AppScale Email API

  * Logging / Monitoring

    * AppEngine/AppScale Logging
    * Sentry, Raven (POST JSON)
    * :ref:`FireLogger`

  * Message Queue (Task Queue, Channels, :ref:`WebSockets <websockets>`, AMQP,
    Worker Pools)

    * Celery: https://celery.readthedocs.org/en/latest/getting-started/brokers/
    * AppEngine/AppScale Tasks API
    * :ref:`Mesos` schedulers (Aurora, Chronos, Marathon)

  * Search Indexing (:ref:`JSON`, :ref:`json-ld-`, :ref:`json-ld`)

    * :ref:`ElasticSearch` (:ref:`Lucene`), :ref:`Solr`
    * AppEngine/AppScale Search API

  * Big Data storage and data local iterators:

    * :ref:`MapReduce`, :ref:`BSP`
    * :ref:`HDFS`, :ref:`DDFS`
    * :ref:`Hadoop`, :ref:`Spark`, :ref:`Cassandra`, :ref:`Accumulo`
    * :ref:`Mesos`
    * :ref:`Ibis`

  * HTTP Object Storage

    * :ref:`libcloud` (https://libcloud.readthedocs.org/en/latest/storage/)
    * Amazon :ref:`AWS` :ref:`S3`
    * :ref:`OpenStack` Swift (:ref:`Swift`, :ref:`S3` APIs)
    * :ref:`Linux`: :ref:`Ceph` RADOS Gateway (:ref:`Swift`, :ref:`S3` APIs)
    * :ref:`Linux`, :ref:`OSX`, :ref:`POSIX`:  :ref:`GlusterFS` (:ref:`Swift`, :ref:`S3` APIs)

* Infrastructure Layer ("provisioning")

  * Resource Pool ("instances" of {virtual machines, containers, task workers})

    * :ref:`Cobbler` (:ref:`libvirt` :ref:`virtualization`)
    * :ref:`Docker` Swarm
    * :ref:`Kubernetes` :ref:`Docker` pods
    * :ref:`Kubernetes-Mesos`: :ref:`Mesos` schedulers and
      :ref:`Kubernetes` :ref:`Docker` pods
    * :ref:`Mesos` schedulers (Aurora, Chronos, Marathon)
    * :ref:`OpenStack`

  * Inventory / Monitoring

    * #ConfigMgmt: :ref:`Packages`
    * #ConfigMgmt: :ref:`Ansible`, :ref:`Puppet`, :ref:`Salt`, :ref:`configuration management`
    * #ConfigMgmt #Instances: :ref:`Cobbler` Web Dashboard
    * #ConfigMgmt #Instances: :ref:`OpenStack` Horizon Dashboard
    * #Inventory: Cobbler JSON, Salt Grains, Puppet Facts, :ref:`osquery` SQL tables
    * #Monitoring: #ConfigMgmt events
    * #Monitoring: Nagios, Shinken, Icinga
    * #Monitoring: Monitd, Collectd, RRD
    * #Logging: Syslog, LogStash, Heka (logtailers)
    * #Logviz: Kibana, Grafana, Graphite, RRD (:ref:`data visualization tools`)
    * #PRF: http://www.brendangregg.com/linuxperf.html
    * Docs: https://www.opsschool.org/en/latest/

  * Physical and Virtual Servers ("servers", "racks", "machines")

    * #ConfigMgmt: :ref:`configuration-management`
      ("infrastructure as code",
      shell-escaping,
      task queues / :ref:`ESBs <ESB>`,
      :ref:`distributed computing protocols`,
      #Logging,
      worker pools)
    * :ref:`Virtualization` (full / para-virtualization)
    * :ref:`Operating Systems` ("OS")
    * Manual Testing -- PEBKAM (*Between Keyboard and Monitor*)
    * :ref:`Computer Engineering` ("computer", #power AC/DC, BIOS, :ref:`NIC`,
      :ref:`ethernet`, USB, RS232 Serial Console, KVM switch)

  * Physical and Software Networks

    + Internet connections
    + VLANs, IPv6 6to4 tunnels
    + SDN --- Software Defined Networking
        
      * :ref:`OpenStack` Neutron
      * :ref:`Docker` networking
      * :ref:`Docker` Swarm networking
      * :ref:`Vagrant` networking
      * :ref:`Virtualbox` networking

    + :term:`DNS` (BIND, dnsmasq, :ref:`Cobbler`, :ref:`OpenStack`,
      :ref:`Vagrant`, :ref:`Docker`)

  * Physical and Virtual Storage

    + Virtual storage:

      - Central file storage (:ref:`NFS`, :ref:`CIFS`, :ref:`WebDAV`)
      - distributed file storage: (:ref:`Ceph`, :ref:`GlusterFS`)
      - persistent block storage: (:ref:`AWS` S3, :ref:`OpenStack` Cinder)
      - on-disk filesystems: (ref:`ext4 <ext>`, :ref:`LVM`, :ref:`BTRFS`,
        :ref:`NTFS`, :ref:`FAT`, :ref:`HFS+`)

    + Physical storage

      - SAN -- Storage Area Network (iSCSI, :ref:`fibre channel`, persistent block storage)
      - NAS -- Network Attached Storage (FreeNAS, Synology,
        :ref:`Network Filesystems`, iSCSI)
      - :ref:`data device bus`: (:ref:`USB`, :ref:`SATA`, :ref:`SCSI`, :ref:`IDE <ide drive>`,
        :ref:`ATA <PATA>` :ref:`hard drives`)

    + Power, HVAC, Fire Suppression

      - #HVAC: Cooling (Active / Passive)
      - #HVAC: Heating (Active / Passive)
      - #Fire: Extinguishers
      - #Fire: Sprinklers: ~**"do not pour water on an
        #lectrical fire"** --- 20,000 Leagues Under the Sea
      - #Fire: Halon
      - #Power: Power supplies (AC --> DC conversion)
      - #Power: Batteries  (AC --> DC --> Batteries --> AC/DC)
      - #Power: Generators
      - #Power: Generator fuel for the generators
      - #Power: Renewable energy, Clean Energy, Sustainable Energy


.. index:: Software-as-a-Service
.. index:: SaaS
.. _SaaS:

SaaS
+++++++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Software_as_a_service
| Wikipedia: https://en.wikipedia.org/wiki/Application_service_provider

SaaS (*Software-as-a-Service*) is a service provision,
application lifecycle,
and recurring billing model
for providing hosted applications.

Examples of SaaS:

* :ref:`ReadTheDocs` is a :ref:`SaaS` which can integrate with
  GitHub (also a :ref:`SaaS` offering) through :term:`Webhooks <webhook>`:

* Travis-CI is a :ref:`SaaS` :ref:`continuous integration` service
  which pulls and builds from a
  GitHub repository upon receipt of a :term:`Webhook`,
  that is free for :ref:`open source` projects

  https://en.wikipedia.org/wiki/Travis_CI

* Google Gmail is a :ref:`SaaS` webmail service:

  https://en.wikipedia.org/wiki/Gmail

* Many :ref:`CRM` software applications are offered as
  :ref:`SaaS` subscription services

* See: :ref:`business-modeling`

  :ref:`SaaS` is distinct from e.g. subscription software licensing;
  because :ref:`SaaS` applications are usually
  *hosted* by the service provider


.. index:: Platform-as-a-Service
.. index:: PaaS
.. _PaaS:

PaaS
++++++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Platform_as_a_service

PaaS (*Platform-as-a-Service*) platforms
offer platform APIs
on top of which applications
can be developed and marginally scaled
if designed and developed for concurrency and asynchronicity.

Examples of PaaS Platforms:

* :ref:`AppEngine`
* :ref:`AppScale`
* :ref:`Deis`
* https://github.com/progrium/dokku
  -- dokku is an extremely minimal (no firewall, etc.)
  ":ref:`Docker` powered mini-Heroku in around 100 lines of :ref:`Bash`"
  (see also: bashreduce)

  * https://news.ycombinator.com/item?id=9054503
    -- The original dokku developer now works with :ref:`Deis`
  * https://github.com/dokku-alt/dokku-alt -- dokku-alt is a fork of dokku

* https://github.com/flynn/flynn
* :ref:`Heroku`


.. index:: AppEngine
.. _appengine:

AppEngine
```````````
| Wikipedia: https://en.wikipedia.org/wiki/Google_App_Engine
| Homepage: https://cloud.google.com/appengine/
| Twitter: https://twitter.com/googlecloud
| Project: https://code.google.com/p/googleappengine/
| Source: svn http://googleappengine.googlecode.com/svn/trunk/python appengine
| Source: svn http://googleappengine.googlecode.com/svn/trunk/java appenginejava
| Source: hg https://code.google.com/p/appengine-go/
| Source: git https://github.com/GoogleCloudPlatform/appengine-php
| Docs: https://developers.google.com/appengine/
| Docs: https://cloud.google.com/appengine/docs
| Docs: https://cloud.google.com/appengine/docs/python/
| Docs: https://cloud.google.com/appengine/docs/java/
| Docs: https://cloud.google.com/appengine/docs/go
| Docs: https://cloud.google.com/appengine/docs/php
| Docs: https://code.google.com/p/googleappengine/issues/list
| Docs: https://cloud.google.com/nodejs/
| Docs: https://cloud.google.com/docs/

Google AppEngine is an :ref:`PaaS` platform
for developing and scaling web applications written in
:ref:`Python`, :ref:`Java`, :ref:`Go`, and `PHP`.

* AppEngine applications can interface with
  Google Cloud Platform :term:`Web APIs <Web API>`


.. index:: AppScale
.. _appscale:

AppScale
``````````
| Wikipedia: https://en.wikipedia.org/wiki/AppScale
| Homepage: http://www.appscale.com/
| Twitter: https://twitter.com/appscalecloud
| Download: https://github.com/AppScale/appscale/releases
| Source: git https://github.com/AppScale/appscale
| Source: https://github.com/AppScale/appscale/tree/master/AppDB/cassandra
| Docs: https://github.com/appscale/appscale/wiki
| Docs: https://github.com/AppScale/appscale/wiki/Installing-AppScale-from-source-on-GitHub
| Docs: https://github.com/AppScale/appscale/wiki/AppScale-on-Google-Compute-Engine
| Docs: https://github.com/AppScale/appscale/wiki/AppScale-on-Amazon-EC2
| Docs: https://github.com/AppScale/appscale/wiki/AppScale-on-Eucalyptus
| Docs: https://github.com/AppScale/appscale/wiki/AppScale-on-Eucalyptus
| Docs: https://github.com/AppScale/appscale/wiki/AppScale-on-VirtualBox
| Docs: https://github.com/AppScale/appscale/wiki/AppScale-on-KVM
| Docs: https://github.com/AppScale/appscale/wiki/Virtualized-Cluster
| Docs: https://github.com/AppScale/appscale/wiki/Autoscaling-Triggers
| Docs: https://github.com/AppScale/appscale/wiki/Adding-Support-for-a-New-Database
| Docs: https://github.com/AppScale/appscale/wiki/Search-API-in-AppScale
| Docs: https://github.com/AppScale/appscale/wiki/Logging-in-AppScale
| Docs: https://github.com/AppScale/appscale/wiki/Managing-Users

AppScale is a completely :ref:`open source`
:ref:`PaaS` platform for developing and scaling web applications
written in
:ref:`Python`, :ref:`Java`, :ref:`Go`, and `PHP`.

* AppScale Python apps deploy applications from ``app.yaml`` :ref:`YAML`
  files; just like :ref:`AppEngine`
* AppScale development supporters include Google and NSF:
  http://googlecloudplatform.blogspot.com/2015/05/AppScale-and-App-Engine-Work-Together-to-Provide-Infrastructure-Flexibility.html

* AppScale applications can interface with
  AppScale implementations of :ref:`AppEngine`
  Google Cloud Platform :term:`Web APIs <Web API>`

.. table:: adapted from https://github.com/AppScale/appscale/wiki/How-AppScale-implements-the-Google-App-Engine-APIs
   :class: table-striped

   +----------------------+-----------------------------------------------+
   | :ref:`AppEngine` API | :ref:`AppScale` implementation                |
   +----------------------+-----------------------------------------------+
   | Datastore            | AppDB { Cassandra, Thrift, Protocol Buffers } |
   +----------------------+-----------------------------------------------+
   | Memcache             | memcached                                     |
   +----------------------+-----------------------------------------------+
   | URL Fetch            | urllib2                                       |
   +----------------------+-----------------------------------------------+
   | Blobstore API        | custom server built on Tornado                |
   +----------------------+-----------------------------------------------+
   | XMPP                 | ejabberd                                      |
   +----------------------+-----------------------------------------------+
   | Channel API          | ejabberd and strophejs                        |
   +----------------------+-----------------------------------------------+
   | Mail                 | sendmail                                      |
   +----------------------+-----------------------------------------------+
   | Images               | Python Imaging Library (PIL)                  |
   +----------------------+-----------------------------------------------+
   | Task Queue           | RabbitMQ                                      |
   +----------------------+-----------------------------------------------+
   | Cron                 | Vixie Cron                                    |
   +----------------------+-----------------------------------------------+
   | Search               | SOLR                                          |
   +----------------------+-----------------------------------------------+
   | CloudSQL             | MySQL                                         |
   +----------------------+-----------------------------------------------+
   | Users                | AppScale Dashboard                            |
   +----------------------+-----------------------------------------------+


.. index:: Deis
.. _deis:

Deis
`````
| Homepage: http://deis.io/
| Source: git https://github.com/deis/deis
| Source: https://github.com/deis/deis/blob/master/Makefile
| Source: https://github.com/deis/deis/blob/master/Vagrantfile
| Docs: http://docs.deis.io/en/latest/
| Docs: http://docs.deis.io/en/latest/toctree/#toctree
| Docs: http://docs.deis.io/en/latest/installing_deis/
| Docs: http://docs.deis.io/en/latest/installing_deis/aws/
| Docs: http://docs.deis.io/en/latest/installing_deis/baremetal/
| Docs: http://docs.deis.io/en/latest/installing_deis/gce/
| Docs: http://docs.deis.io/en/latest/installing_deis/openstack/
| Docs: http://docs.deis.io/en/latest/installing_deis/rackspace/
| Docs: http://docs.deis.io/en/latest/installing_deis/vagrant/
| Docs: http://docs.deis.io/en/latest/understanding_deis/concepts/
| Docs: http://docs.deis.io/en/latest/understanding_deis/architecture/
| Docs: http://docs.deis.io/en/latest/understanding_deis/components/
| Docs: http://docs.deis.io/en/latest/using_deis/deploy-application/
| Docs: http://docs.deis.io/en/latest/using_deis/using-buildpacks/

Deis is an :ref:`open source` :ref:`PaaS`
platform built on :ref:`Docker` and :ref:`CoreOS`
written in :ref:`Python` and :ref:`Go`.

* Apps are deployed to Deis with :ref:`git` (``git push``) or
  the ``deis`` CLI client.

* :ref:`configuration management` is useful but not necessary
  for provisioning Deis
  (e.g. creating and managing custom deis images and containers
  with extra libraries and configuration).
* Deis builds with :ref:`Make`, :ref:`Docker`
  :term:`Dockerfiles <dockerfile>`, and :ref:`CoreOS`.

  * https://github.com/deis/deis/blob/master/controller/Dockerfile
  * https://github.com/deis/deis/blob/master/controller/requirements.txt
  * https://github.com/deis/deis/blob/master/database/Dockerfile
  * https://github.com/deis/deis/blob/master/store/Makefile
  * https://github.com/deis/deis/tree/master/tests

* Deis can work with the :ref:`Linux` Ceph filesystem.

  * Deis supports :ref:`Heroku` Buildpacks:
    http://docs.deis.io/en/latest/using_deis/using-buildpacks/#included-buildpacks

    + :ref:`Ruby`, :ref:`Node.js`, :ref:`java`, Gradle, Grails, Play,
      :ref:`Python`, PHP, Clojure, :ref:`Scala`, :ref:`Go`
    + buildpacks are composable: https://github.com/heroku/heroku-buildpack-multi

* Deis can scale to ``n`` instance of containers per process (e.g. ``web``)::

    deis scale web=3

See also: :ref:`Heroku`, :ref:`Kubernetes`, :ref:`Kubernetes-Mesos`


.. index:: Heroku
.. _heroku:

Heroku
````````
| Wikipedia: https://en.wikipedia.org/wiki/Heroku
| Homepage: https://www.heroku.com/
| Twitter: https://twitter.com/heroku
| Source: https://github.com/heroku
| Docs: https://devcenter.heroku.com/articles/git

Heroku is a :ref:`PaaS` Platform.

:ref:`Deis` supports :ref:`Heroku` Buildpacks.


.. index:: Infrastructure-as-a-Service
.. index:: IaaS
.. _IaaS:

IaaS
++++++++++++
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Cloud_infrastructure

Infrastructure-as-a-Service providers provide a bit more than regular
hosting services in that they offer something like virtual datacenter
resource pools: servers, networks, and
redundant storage systems on top of which IT systems can be
developed, tested, and deployed.

Examples of IaaS:

* :ref:`Amazon AWS <aws>`
* :ref:`Google Cloud`
* :ref:`Rackspace Cloud`
* :ref:`libcloud` implements a :ref:`Python` :term:`language api`
  over very many :ref:`IaaS` and :ref:`PaaS` clouds:
  https://libcloud.readthedocs.org/en/latest/supported_providers.html


.. index:: AWS
.. _aws:

Amazon AWS
`````````````
| Wikipedia: https://en.wikipedia.org/wiki/Amazon_Web_Services
| Wikipedia: https://en.wikipedia.org/wiki/Amazon_Elastic_Compute_Cloud
| Wikipedia: https://en.wikipedia.org/wiki/Amazon_Elastic_Block_Store
| Wikipedia: https://en.wikipedia.org/wiki/Amazon_S3
| Wikipedia: https://en.wikipedia.org/wiki/Amazon_Relational_Database_Service
| Wikipedia: https://en.wikipedia.org/wiki/Amazon_CloudFront
| Homepage: https://aws.amazon.com/
| Twitter: https://twitter.com/awscloud
| Docs: https://aws.amazon.com/products/
| Docs: https://aws.amazon.com/ec2/pricing/
| Docs: https://aws.amazon.com/ebs/pricing/
| Docs: https://aws.amazon.com/s3/pricing/
| Docs: https://aws.amazon.com/rds/pricing/
| Docs: https://aws.amazon.com/cloudfront/pricing/
| Docs: https://aws.amazon.com/cloudformation/

* EC2 -- Elastic Compute Cloud (CPU/GPU/RAM instances)
* EBS -- Elastic Block Store (persistent block storage)
* S3 -- Simple Storage Service (HTTP object storage)
* SQS -- Simple Queue Server
* CloudFormation -- EC2 [auto-]scaling
* CloudFront -- CDN
* RDS: Managed MySQL, Oracle, SQL Server, PostgreSQL
* DynamoDB: :ref:`nosql` supercolumn cloud datastore

:ref:`Python` and AWS

* boto, :ref:`libcloud`


.. index:: Google Cloud
.. _google cloud:

Google Cloud
```````````````
| Wikipedia: https://en.wikipedia.org/wiki/Google_Cloud_Platform
| Wikipedia: https://en.wikipedia.org/wiki/Google_Compute_Engine
| Wikipedia: https://en.wikipedia.org/wiki/Google_Cloud_Messaging
| Homepage: https://cloud.google.com/
| Twitter: https://twitter.com/googlecloud
| Docs: https://cloud.google.com/products/
| Docs: https://cloud.google.com/compute/
| Docs: https://cloud.google.com/container-engine/
| Docs: https://cloud.google.com/dns/
| Docs: https://cloud.google.com/datastore/
| Docs: https://cloud.google.com/storage/
| Docs: https://cloud.google.com/sql/
| Docs: https://cloud.google.com/bigquery/
| Docs: https://cloud.google.com/dataflow/

Google Cloud Platform (GCP) is an :ref:`Iaas` cloud platform.

* :ref:`AppEngine` -- :ref:`PaaS`
* Compute Engine (GCE) -- :ref:`IaaS`

  * :ref:`KVM`, SDN

* Container Engine (GCE)  -- :ref:`IaaS`

  * :ref:`kubernetes`, :ref:`docker`

* CloudSQL (MySQL)

:ref:`Python` and Google Cloud

* :ref:`libcloud`
* https://cloud.google.com/compute/docs/tutorials/python-guide
* https://github.com/westurner/dotfiles/blob/master/etc/bash/08-bashrc.gcloud.sh


.. index:: Rackspace Cloud
.. _rackspace cloud:

Rackspace Cloud
````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Rackspace_Cloud
| Homepage: https://www.rackspace.com/cloud
| Twitter: https://twitter.com/Rackspace
| Docs: http://docs.rackspace.com/

Rackspace Cloud is an :ref:`IaaS` cloud platform
built with :ref:`OpenStack`.

* Rackspace CloudFiles is now :ref:`OpenStack` Swift.
* Rackspace Cloud is powered by :ref:`OpenStack`.
* Cloud Servers -- :ref:`OpenStack` Compute
* Cloud Load Balancers
* Cloud DNS
* Cloud Networks
* Cloud Block Storage -- :ref:`OpenStack` Cinder
* Cloud Files -- :ref:`OpenStack` Swift
* CDN
* Cloud Databases (MySQL)
* Cloud Big Data (Hadoop)
* Cloud Queues
* Rackspace Auto Scale
* Rackspace Private Cloud v4, v9, v10 (:ref:`OpenStack`)

Python and Rackspace Cloud

* :ref:`libcloud`
* https://developer.rackspace.com/sdks/python/
* https://github.com/rackspace/pyrax


.. index:: Configuration Management
.. _configuration-management:

Configuration Management
~~~~~~~~~~~~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Configuration_management#Software
| Wikipedia: https://en.wikipedia.org/wiki/Software_configuration_management

https://en.wikipedia.org/wiki/Comparison_of_open-source_configuration_management_software

See: :ref:`Tools > Configuration Managment <configuration management>`


.. index:: Information Security
.. _information security:

Information Security
~~~~~~~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Information_security

Managing risk and uncertainty.

Standards:

* https://en.wikipedia.org/wiki/Statement_on_Auditing_Standards_No._70:_Service_Organizations
* https://en.wikipedia.org/wiki/Evaluation_Assurance_Level
* https://en.wikipedia.org/wiki/Cloud_computing_security

See: :ref:`WebSec`


.. index:: Confidentiality
.. _confidentiality:

Confidentiality
++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Confidentiality


.. index:: Integrity
.. _integrity:

Integrity
++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Data_integrity


.. index:: Availability
.. _availability:

Availability
+++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Availability

https://en.wikipedia.org/wiki/Service-level_agreement


.. index:: Business Continuity
.. _business-continuity:

Business Continuity
~~~~~~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Business_continuity

https://en.wikipedia.org/wiki/Business_continuity_planning

https://en.wikipedia.org/wiki/Disaster_recovery

See: `Information Security`_ (`Availability`_)


.. index:: Backups
.. _backups:

Backups
++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Backup


.. index:: Reliability
.. _reliability:

Reliability
+++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Reliability_engineering

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
| Wikipedia: https://en.wikipedia.org/wiki/Accounting

https://en.wikipedia.org/wiki/Double-entry_bookkeeping_system

https://en.wikipedia.org/wiki/Accountant

https://en.wikipedia.org/wiki/Financial_statement

https://en.wikipedia.org/wiki/Business_valuation


.. index:: GNUCash
.. _GNUCash:

GNUCash
`````````
| Wikipedia: https://en.wikipedia.org/wiki/GnuCash

* Free and Open Source
* Personal Accounting
* Small Business Accounting


.. index:: Quicken
.. _Quicken:

Quicken
`````````
| Wikipedia: https://en.wikipedia.org/wiki/Quicken

* Personal Accounting
* USA Version
* International Versions


.. index:: QuickBookx
.. _QuickBooks:

QuickBooks
````````````
| Wikipedia: https://en.wikipedia.org/wiki/QuickBooks

* Small Business Accounting
* Square integrates with QuickBooks
* http://www.google.com/enterprise/marketplace/search?query=quickbooks


.. index:: Payments
.. _payments:

Payments
++++++++++


.. index:: Amazon Payments
.. _amazon-payments:

Amazon Payments
`````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Amazon_Payments


.. index:: Apple Pay
.. _apple-pay:

Apple Pay
``````````
| Wikipedia: https://en.wikipedia.org/wiki/Apple_Pay


.. index:: Google Wallet
.. index:: Google Checkout
.. _google-wallet:

Google Wallet
``````````````
| Wikipedia: https://en.wikipedia.org/wiki/Google_Wallet

* https://en.wikipedia.org/wiki/Google_Checkout


.. index:: PayPal
.. _paypal:

PayPal
```````
| Wikipedia: https://en.wikipedia.org/wiki/PayPal


.. index:: Square
.. _square:

Square
````````
| Wikipedia: `<https://en.wikipedia.org/wiki/Square,_Inc.>`__

https://squareup.com/

* Square Reader (plugs into headphone jack)
* Square Stand (point of sale)
* Square Register (iOS & Android app)
* Square Market (online store)
* Square Appointments (online scheduling)
* Square Feedback (customer feedback)
* Square Analytics (sales reporting)
* Square Capital (business funding)
* Square Invoices (online invoicing)
* Square Payroll (employee payroll)


.. index:: Sales Information Systems
.. _sales information systems:

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

See: :ref:`data science`

See: :ref:`knowledge engineering`
