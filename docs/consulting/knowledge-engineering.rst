
.. index:: Knowledge Engineering
.. _knowledge-engineering:

Knowledge Engineering
========================
https://en.wikipedia.org/wiki/Knowledge_engineering

https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning

https://en.wikipedia.org/wiki/Knowledge#Communicating_knowledge

https://en.wikipedia.org/wiki/Category:Knowledge

https://en.wikipedia.org/wiki/Category:Graph_theory

https://en.wikipedia.org/wiki/Schema

https://en.wikipedia.org/wiki/Category:Ontology

`<https://en.wikipedia.org/wiki/Category:Ontology_(information_science)>`_


Logic, Reasoning, and Inference
---------------------------------
https://en.wikipedia.org/wiki/Epistemology

* https://en.wikipedia.org/wiki/Truth
* https://en.wikipedia.org/wiki/Belief
* https://en.wikipedia.org/wiki/Theory_of_justification

.. contents::
   :local:


.. index:: Logic
.. _logic:

Logic
+++++++
https://en.wikipedia.org/wiki/Logic

https://en.wikipedia.org/wiki/Category:Logic

https://en.wikipedia.org/wiki/List_of_logic_symbols


.. index:: Set Theory
.. _set-theory:

Set Theory
````````````
https://en.wikipedia.org/wiki/Set_theory


.. index:: Boolean Algebra
.. _boolean-algebra:

Boolean Algebra
````````````````
https://en.wikipedia.org/wiki/Boolean_algebra


.. index:: Many-valued Logic
.. _many-valued-logic:

Many-valued Logic
````````````````````
https://en.wikipedia.org/wiki/Many-valued_logic


.. index:: Three-valued Logic
.. _three-valued-logic:

Three-valued Logic
~~~~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Three-valued_logic

::

    { True, False, Unknown }

    { T, F, NULL }  # SQL
    { T, F, None }  # Python
    { T, F, nil }   # Ruby
    { 1, 0, -1 }    #


.. index:: Fuzzy Logic
.. _fuzzy-logic:

Fuzzy Logic
~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Fuzzy_logic


.. index:: Probabilistic Logic
.. _probabilistic-logic:

Probabilistic Logic
~~~~~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Probabilistic_logic


.. index:: Propositional Logic
.. _propsitional-logic:

Propositional Logic
`````````````````````
https://en.wikipedia.org/wiki/Propositional_logic


.. index:: First-order Logic
.. index:: FOL
.. _FOL:

First-order Logic
```````````````````
https://en.wikipedia.org/wiki/First-order_logic (FOL)


.. index:: Description Logic
.. index:: DL
.. _DL:

Description Logic
```````````````````
https://en.wikipedia.org/wiki/Description_logic (DL; DLP (Description Logic Programming))

* https://en.wikipedia.org/wiki/Description_logic#Notation
* https://en.wikipedia.org/wiki/Description_logic#Relationship_with_other_logics

Knowledge Base = TBox + ABox

* https://en.wikipedia.org/wiki/TBox (Schema: Class/Property Ontology)
* https://en.wikipedia.org/wiki/ABox (Facts / Instances)

See:

* :ref:`OWL`, :ref:`entailment`
* :ref:`Semantic-web`
* :ref:`N3` for ``=>`` implies

.. index:: Reasoning
.. _reasoning:

Reasoning
++++++++++
https://en.wikipedia.org/wiki/Deductive_reasoning

https://en.wikipedia.org/wiki/Category:Reasoning

https://en.wikipedia.org/wiki/Semantic_reasoner

See: :ref:`DL`

.. index:: Inference
.. _inference:

Inference
```````````
* https://en.wikipedia.org/wiki/Inference
* https://en.wikipedia.org/wiki/Rule_of_inference (Logic)
* https://en.wikipedia.org/wiki/Category:Statistical_inference (Logic + Math)


.. index:: Entailment
.. _entailment:

Entailment
~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Entailment

* http://www.w3.org/TR/owl2-profiles/#Introduction

See: :ref:`Data Science <data-science>`


.. index:: File Structures
.. _file structures:

File Structures
-----------------
https://en.wikipedia.org/wiki/File_format

`<https://en.wikipedia.org/wiki/Record_(computer_science)>`_

`<https://en.wikipedia.org/wiki/Field_(computer_science)>`_

https://en.wikipedia.org/wiki/Index#Computer_science

* :ref:`tar` and :ref:`zip` are file structures
  that have a *manifest* and a *payload*

  * :ref:`file systems` often have redundant manifests
    (and/or deduplication according to a hash table manifest
    with an interface like a :ref:`dht`)


.. index:: File Systems
.. _file systems:

File Systems
--------------
| Wikipedia:


.. index:: Compression Algorithms
.. _compression algorithms:

Compression Algorithms
-------------------------

.. index:: bzip2
.. _bzip2:

bzip2
+++++++
| Wikipedia: https://en.wikipedia.org/wiki/Bzip2
| File Extension: ``.bz2``
| Homepage: http://bzip.org/

bzip2 is an :ref:`Open Source <open-source>` lossless compression algorithm
based upon the ``Burrows-Wheeler`` algorithm.

* bzip2 is usually slower than :ref:`gzip` or :ref:`zip`,
  but more space efficient


.. index:: gzip
.. _gzip:

gzip
++++++
| Wikipedia: https://en.wikipedia.org/wiki/Gzip
| Homepage: https://www.gnu.org/software/gzip/
| File Extension: ``.gz``
| Source: http://ftp.gnu.org/gnu/gzip/
| Docs: https://www.gnu.org/software/gzip/manual/
| Docs: https://www.gnu.org/software/gzip/manual/gzip.html

gzip is a compression algorithm
based on ``DEFLATE`` and ``LZ77``.

* gzip is similar to :ref:`Zip`, in that both are based upon
  ``DEFLATE``


.. index:: tar
.. _tar:

tar
++++
| Wikipedia: `<https://en.wikipedia.org/wiki/Tar_(computing)>`__
| File Extension: ``.tar``

:ref:`tar` is a file archiving format
for storing a manifest of records of
a set of files with paths and attributes
at the beginning of the actual files
all concatenated into one file.

* TAR = ( table of contents + data stream )
* ``.tar.gz`` is :ref:`tar` + :ref:`gzip`
* ``.tar.bz2`` is :ref:`tar` + :ref:`bzip2`

TAR and :ref:`gzip` or :ref:`bzip2` can be streamed over SSH::

    # https://unix.stackexchange.com/a/95994
    tar czf - . | ssh remote "( cd ~/ ; cat > file.tar.gz )"
    tar bzf - . | ssh remote "( cd ~/ ; cat > file.tar.bz2 )"

See also: :ref:`zip` (:ref:`windows`)


.. index:: ZIP
.. _zip:

zip
++++
| Wikipedia: `<https://en.wikipedia.org/wiki/Zip_(file_format)>`__

zip is a lossless file archive compression


.. index:: Data Structures
.. _data structures:

Data Structures
----------------
https://en.wikipedia.org/wiki/Data_structure

https://en.wikipedia.org/wiki/List_of_data_structures

* http://rosettacode.org/wiki/Category:Programming_Tasks

  * http://rosettacode.org/wiki/Greatest_common_divisor
  * http://rosettacode.org/wiki/Go_Fish


.. index:: Arrays
.. _arrays:

Arrays
++++++++
https://en.wikipedia.org/wiki/Array_data_structure

* https://en.wikipedia.org/wiki/List_of_data_structures#Arrays
* `<https://en.wikipedia.org/wiki/Matrix_(computer_science)>`_


.. index:: Lists
.. _lists:

Lists
+++++++
https://en.wikipedia.org/wiki/Linked_list

* https://en.wikipedia.org/wiki/List_of_data_structures#Lists


.. index:: Trees
.. _trees:

Trees
+++++++
https://en.wikipedia.org/wiki/Tree_data_structure

* https://en.wikipedia.org/wiki/List_of_data_structures#Trees
* https://en.wikipedia.org/wiki/B-tree
* https://en.wikipedia.org/wiki/Trie
* https://en.wikipedia.org/wiki/Abstract_syntax_tree
* https://en.wikipedia.org/wiki/Parse_tree
* https://en.wikipedia.org/wiki/Decision_tree
* https://en.wikipedia.org/wiki/Minmax
* https://en.wikipedia.org/wiki/Database_index


.. index:: Databases
.. _databases:

Databases
-----------
https://en.wikipedia.org/wiki/Database

https://en.wikipedia.org/wiki/Database_schema

https://en.wikipedia.org/wiki/Create,_read,_update_and_delete

https://en.wikipedia.org/wiki/CRUD

https://en.wikipedia.org/wiki/ACID

https://en.wikipedia.org/wiki/Query_plan

https://en.wikipedia.org/wiki/Database_index

https://en.wikipedia.org/wiki/Search_engine_indexing

https://en.wikipedia.org/wiki/Category:Database_software_comparisons

* http://db-engines.com/en/ranking


.. index:: ORM
.. index:: Object Relational Mapping
.. _orm:

Object Relational Mapping
+++++++++++++++++++++++++++
https://en.wikipedia.org/wiki/Object-relational_mapping

* https://en.wikipedia.org/wiki/Data_mapper_pattern
* https://en.wikipedia.org/wiki/Active_record_pattern

https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch

https://en.wikipedia.org/wiki/List_of_object-relational_mapping_software


.. index:: Relational Databases
.. index:: SQL Databases
.. _relational-databases:

Relational Databases
+++++++++++++++++++++
https://en.wikipedia.org/wiki/Relational_database

https://en.wikipedia.org/wiki/Relational_model

https://en.wikipedia.org/wiki/Relational_algebra

* `<https://en.wikipedia.org/wiki/Projection_(relational_algebra)>`_
* https://en.wikipedia.org/wiki/Relational_algebra#Joins_and_join-like_operators
* https://en.wikipedia.org/wiki/Relational_algebra#Common_extensions

https://en.wikipedia.org/wiki/Database_normalization

* https://en.wikipedia.org/wiki/Referential_integrity
* https://en.wikipedia.org/wiki/Functional_dependency
* https://en.wikipedia.org/wiki/Dangling_pointer
* https://en.wikipedia.org/wiki/Natural_key
* https://en.wikipedia.org/wiki/Surrogate_key
* https://en.wikipedia.org/wiki/Foreign_key
* https://en.wikipedia.org/wiki/Denormalization

https://en.wikipedia.org/wiki/Relational_database_management_system

* https://en.wikipedia.org/wiki/Comparison_of_relational_database_management_systems
* http://db-engines.com/en/ranking/relational+dbms
* https://en.wikipedia.org/wiki/SQLite
* https://en.wikipedia.org/wiki/MySQL
* https://en.wikipedia.org/wiki/PostgreSQL
* https://en.wikipedia.org/wiki/Virtuoso_Universal_Server
* https://en.wikipedia.org/wiki/OLAP


.. index:: SQL
.. _sql:

SQL
````
https://en.wikipedia.org/wiki/SQL

* `<https://en.wikipedia.org/wiki/Null_(SQL)#Comparisons_with_NULL_and_the_three-valued_logic_.283VL.29>`_
* `<https://en.wikipedia.org/wiki/Join_(SQL)>`_
* https://en.wikipedia.org/wiki/SQL_injection
* http://cwe.mitre.org/top25/#CWE-89 (#1 Most Prevalent Dangerous
  Security Error (2011))

See: :ref:`Object Relational Modeling <orm>`


.. index:: NoSQL
.. index:: NoSQL Databases
.. _nosql:

NoSQL Databases
+++++++++++++++++
https://en.wikipedia.org/wiki/NoSQL

`<https://en.wikipedia.org/wiki/Keyspace_(distributed_data_store)>`_

`<https://en.wikipedia.org/wiki/Column_(data_store)>`_

* `<https://en.wikipedia.org/wiki/Column_family>`_
* `<https://en.wikipedia.org/wiki/Super_column>`_
* https://en.wikipedia.org/wiki/Apache_Accumulo


.. index:: Distributed Databases
.. _distributed-databases:

Distributed Databases
++++++++++++++++++++++++
https://en.wikipedia.org/wiki/Distributed_database

https://en.wikipedia.org/wiki/Distributed_data_store

https://en.wikipedia.org/wiki/Distributed_computing

https://en.wikipedia.org/wiki/Category:Distributed_computing_problems

* `<https://en.wikipedia.org/wiki/Consensus_(computer_science)>`_
* https://en.wikipedia.org/wiki/Leader_election
* https://en.wikipedia.org/wiki/Distributed_concurrency_control
* https://en.wikipedia.org/wiki/Distributed_lock_manager
*

https://en.wikipedia.org/wiki/Category:Distributed_algorithms

* `<https://en.wikipedia.org/wiki/Paxos_(computer_science)>`_

.. index:: Distributed Hash Table
.. index:: DHT
.. _dht:

Distributed Hash Table
++++++++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Distributed_hash_table

A Distributed Hash Table (*DHT*) is a distributed structure
for storing things based upon a consistent file hash.

* At an API level, a DHT is a key/value store.
* :term:`DNS` is basically a DHT
* :ref:`distributed-databases` all implement some form of
  a structure simiar to a DHT (a replicated *keystore*);
  often for things like bloom filters (for fast search)
* :ref:`browsers` that maintain a local cache could
  implement a DHT (e.g. with :ref:`websockets` or :ref:`webrtc`)

  * https://github.com/feross/webtorrent
    (:ref:`Javascript`, :ref:`WebRTC`)

* :ref:`BitTorrent` :term:`magnet URIs <magnet uri>` (:term:`URNs <urn>`)
  contain a key,
  which is a checksum of a manifest,
  which can be retrieved from the DHT
  (e.g. with ``dht = DHT(); value = dht.get(urn)``)



.. index:: Graph Databases
.. _graph-databases:

Graph Databases
++++++++++++++++++
https://en.wikipedia.org/wiki/Graph_database

https://en.wikipedia.org/wiki/Graph_database#Graph_database_projects

* http://db-engines.com/en/ranking/graph+dbms
* https://en.wikipedia.org/wiki/Virtuoso_Universal_Server
* https://en.wikipedia.org/wiki/AllegroGraph
* https://en.wikipedia.org/wiki/Sqrrl
* https://en.wikipedia.org/wiki/Neo4j

Graph Queries

* https://en.wikipedia.org/wiki/Graph_database#APIs_and_Graph_Query.2FProgramming_Languages
* https://en.wikipedia.org/wiki/SPARQL
* `<https://en.wikipedia.org/wiki/Gremlin_(programming_language)>`__
* https://en.wikipedia.org/wiki/Apache_Spark GraphX


.. index:: RDF Triplestores
.. index:: Triplestores
.. _triplestores:

RDF Triplestores
+++++++++++++++++
https://en.wikipedia.org/wiki/Triplestore

https://en.wikipedia.org/wiki/List_of_subject-predicate-object_databases

* http://db-engines.com/en/ranking/rdf+store
* https://en.wikipedia.org/wiki/Virtuoso_Universal_Server
* `<https://en.wikipedia.org/wiki/Sesame_(framework)>`__
* `<https://en.wikipedia.org/wiki/Jena_(framework)>`__

Graph Pattern Query Results

* :ref:`SPARQL`
* https://en.wikipedia.org/wiki/Redland_RDF_Application_Framework

  * http://librdf.org/notes/contexts.html

* `<https://en.wikipedia.org/wiki/Jena_(framework)>`__
* SAIL (Storage and Inferencing Layer) API
* https://en.wikipedia.org/wiki/CubicWeb
* :ref:`RDFLib`

``rdfs:seeAlso``

* :ref:`Linked Data <linked-data>`
* :ref:`Semantic Web <semantic-web>`
* :ref:`Semantic Web Standards <semantic-web-standards>`
* :ref:`Semantic Web Tools <semantic-web-tools>`
* :ref:`LDP`


.. index:: Data Grid
.. _data-grid:

Data Grid
------------
https://en.wikipedia.org/wiki/Data_grid


.. index:: Linked Data
.. _linked-data:

Linked Data
-------------
https://en.wikipedia.org/wiki/Linked_data

* http://www.w3.org/DesignIssues/LinkedData.html


.. index:: 5 Star Open Data
.. index:: 5 Star Linked Open Data
.. _fivestardata:

5 ★ Linked Data
++++++++++++++++++
http://www.w3.org/TR/ld-glossary/#x5-star-linked-open-data

.. epigraph::

   ☆

   Publish data on the Web in any format (e.g., PDF, JPEG)
   accompanied by an explicit
   `Open License <https://en.wikipedia.org/wiki/Open_content#Licenses>`_
   (expression of rights).

   ☆☆

   Publish `structured data
   <https://en.wikipedia.org/wiki/Structured_data>`_
   on the Web in a machine-readable format
   (e.g. :ref:`XML`).

   ☆☆☆

   Publish structured data on the Web in a documented,
   `non-proprietary data format <https://en.wikipedia.org/wiki/Open_format>`_
   (e.g.
   :ref:`CSV`,
   `KML <https://en.wikipedia.org/wiki/Keyhole_Markup_Language>`_).

   ☆☆☆☆

   Publish structured data on the Web as RDF
   (e.g.
   :ref:`Turtle`,
   :ref:`RDFa`,
   :ref:`JSON-LD`,
   :ref:`SPARQL`.)

   ☆☆☆☆☆

   In your :ref:`RDF`,
   have the
   `identifiers <https://en.wikipedia.org/wiki/Uniform_resource_identifier>`_
   be links
   (`URLs <https://en.wikipedia.org/wiki/Uniform_resource_locator>`_)
   to useful `data <https://en.wikipedia.org/wiki/Data>`_ sources.

   -- http://5stardata.info/


See: :ref:`Semantic Web <semantic-web>`


.. index:: Semantic Web
.. _semantic-web:

Semantic Web
-------------
https://en.wikipedia.org/wiki/Semantic_Web

https://en.wikipedia.org/wiki/Template:Semantic_Web

https://en.wikipedia.org/wiki/Category:Semantic_Web

`<https://en.wikipedia.org/wiki/Semantics_(computer_science)>`_

* http://www.w3.org/2001/sw/wiki/Books
* http://www.w3.org/2001/sw/wiki/Tools


.. index:: Semantic Web Standards
.. _semantic-web-standards:

Semantic Web Standards
-----------------------

`<https://en.wikipedia.org/wiki/Statement_(computer_science)>`_

`<https://en.wikipedia.org/wiki/Resource_(computing)>`_

https://en.wikipedia.org/wiki/Entity-attribute-value_model

https://en.wikipedia.org/wiki/Tuple

* `<https://en.wikipedia.org/wiki/Triple_(mathematics)>`_
* `<https://en.wikipedia.org/wiki/3-tuple>`_
* `<https://en.wikipedia.org/wiki/Quad_(mathematics)>`_
* `<https://en.wikipedia.org/wiki/4-tuple>`_

`<https://en.wikipedia.org/wiki/Reification_(computer_science)#Reification_on_Semantic_Web>`_

https://en.wikipedia.org/w/index.php?title=Eigenclass_model&oldid=592778140#In_RDF_Schema

Representations / Serializations

* :ref:`RDF`: :ref:`N-Triples`, :ref:`RDF/XML`, :ref:`TriX`, :ref:`N3`,
  :ref:`Turtle`, :ref:`TriG`, :ref:`RDFa`, :ref:`JSON-LD`

Vocabularies

* :ref:`RDFS`: :ref:`DCMI`, :ref:`SKOS`, :ref:`Schema.org`

Query APIS

* :ref:`SPARQL`, :ref:`LDP`

Ontologies

* :ref:`OWL`: :ref:`PROV`, :ref:`OA`, :ref:`QUDT`

Reasoners

* See:

  * :ref:`DL`
  * :ref:`OWL` 2 Profiles
  * :ref:`entailment`


.. index:: Web Standards
.. _web-standards:

Web Standards
---------------
https://en.wikipedia.org/wiki/Web_standards



.. index:: Time Zones
.. _time zones:

Time Zones
++++++++++++
https://en.wikipedia.org/wiki/Time_zone

https://en.wikipedia.org/wiki/Daylight_saving_time

https://en.wikipedia.org/wiki/List_of_UTC_time_offsets

https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

* :ref:`iso8601`


.. index:: Long Now Dates
.. _long now dates:

Long Now Dates
````````````````
https://en.wikipedia.org/wiki/Long_Now_Foundation

::

     2015    # ISO8601 date
    02015    # Long Now Date


.. index:: Unix Time
.. _unix time:

Unix Time
```````````
https://en.wikipedia.org/wiki/Unix_time

     Defined as the number of seconds that have elapsed
     since 00:00:00 Coordinated Universal Time (UTC),
     Thursday, 1 January 1970, not counting leap seconds

Unix time is the delta in seconds since
``1970-01-01T00:00:00Z``, not counting leap seconds:

.. code::

    0                       # Unix time
    1970-01-01T00:00:00Z    # ISO8601 timestamp

    1435255816              # Unix time
    2015-06-25T18:10:16Z    # ISO8601 timestamp

.. note:: Unix time does not count leap seconds.

   https://en.wikipedia.org/wiki/Unix_time#Leap_seconds


.. index:: US Time Zones
.. _us time zones:

US Time Zones
`````````````````
https://en.wikipedia.org/wiki/Time_in_the_United_States

https://en.wikipedia.org/wiki/Time_in_the_United_States#Standard_time_and_daylight_saving_time

https://en.wikipedia.org/wiki/History_of_time_in_the_United_States


.. index:: US Daylight Savings Time
.. index:: Daylight Savings Time
.. _daylight savings time:

US Daylight Savings Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://en.wikipedia.org/wiki/Daylight_saving_time_in_the_United_States

    Currently, daylight saving time
    **starts on the second Sunday in March**
    and **ends on the first Sunday in November**,
    with the time changes taking place **at 2:00 a.m. local time**.

    With a mnemonic word play referring to seasons,
    clocks *"spring forward and fall back"* — that is,
    in spring (technically late winter) the clocks are
    moved forward from 2:00 a.m. to 3:00 a.m.,
    and in fall they are
    moved back from 2:00 am to 1:00 am.


Daylight Savings Time Starts and Ends on the following dates
(from https://en.wikipedia.org/wiki/Time_in_the_United_States#Daylight_saving_time):

+----------+--------------------+------------------+
| **Year** | **DST start date** | **DST end date** |
+----------+--------------------+------------------+
| 2015     | 2015-03-08 02:00   | 2015-11-01 02:00 |
+----------+--------------------+------------------+
| 2016     | 2016-03-13 02:00   | 2016-11-06 02:00 |
+----------+--------------------+------------------+
| 2017     | 2017-03-12 02:00   | 2017-11-05 02:00 |
+----------+--------------------+------------------+
| 2018     | 2018-03-11 02:00   | 2018-11-04 02:00 |
+----------+--------------------+------------------+
| 2019     | 2019-03-10 02:00   | 2019-11-03 02:00 |
+----------+--------------------+------------------+
| 2020     | 2020-03-08 02:00   | 2020-11-01 02:00 |
+----------+--------------------+------------------+

Time Zone names, URIs, and :ref:`iso8601` UTC offsets:

+----------------------------------------------------------+----------------+--------------------+
| **Time zone names, URNs, URIs**                          | **UTC Offset** | **UTC DST Offset** |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Coordinated_Universal_Time | -0000 Z        | +0000 Z            |
|                                                          |                |                    |
| Coordinated Universal Time, **UTC**, **Zulu**            |                |                    |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Atlantic_Time_Zone         |                |                    |
|                                                          |                |                    |
| https://en.wikipedia.org/wiki/America/Halifax            |                |                    |
|                                                          |                |                    |
| Atlantic, Antarctica (Palmer), AST, ADT                  | -0400 AST      | -0300 ADT          |
|                                                          |                |                    |
| America/Halifax                                          |                |                    |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/America/St_Thomas          |                |                    |
|                                                          |                |                    |
| America/St_Thomas, America/Virgin                        | -0400          | -0400              |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Eastern_Time_Zone          |                |                    |
|                                                          |                |                    |
| https://en.wikipedia.org/wiki/EST5EDT                    |                |                    |
|                                                          |                |                    |
| Eastern, EST, EDT                                        | -0500 EST      | -0400 EDT          |
|                                                          |                |                    |
| America/New_York                                         |                |                    |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Central_Time_Zone          |                |                    |
|                                                          |                |                    |
| https://en.wikipedia.org/wiki/CST6CDT                    |                |                    |
|                                                          |                |                    |
| Central, CST, CDT                                        | -0600 CST      | -0500 CDT          |
|                                                          |                |                    |
| America/Chicago                                          |                |                    |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Mountain_Time_Zone         |                |                    |
|                                                          |                |                    |
| https://en.wikipedia.org/wiki/MST7MDT                    |                |                    |
|                                                          |                |                    |
| Mountain, MST, MDT                                       | -0700 MST      | -0600 MDT          |
|                                                          |                |                    |
| America/Denver                                           |                |                    |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Pacific_Time_Zone          |                |                    |
|                                                          |                |                    |
| https://en.wikipedia.org/wiki/PST8PDT                    |                |                    |
|                                                          |                |                    |
| Pacific, PST, PDT                                        | -0800 PST      | -0700 PDT          |
|                                                          |                |                    |
| America/Los_Angeles                                      |                |                    |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Alaska_Time_Zone           |                |                    |
|                                                          |                |                    |
| AKST9AKDT                                                |                |                    |
|                                                          |                |                    |
| Alaska, AKST, AKDT                                       | -0900 AKST     | -0800 AKDT         |
|                                                          |                |                    |
| America/Juneau                                           |                |                    |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Hawaii-Aleutian_Time_Zone  |                |                    |
|                                                          |                |                    |
| HAST10HADT                                               |                |                    |
|                                                          |                |                    |
| Hawaii Aleutian, HAST, HADT                              | -1000 HAST     | -0900 HADT         |
|                                                          |                |                    |
| Pacific/Honolulu                                         |                |                    |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Samoa_Time_Zone            |                |                    |
|                                                          |                |                    |
| Samoa Time Zone, SST                                     | -1100 SST      | -1100 SST          |
|                                                          |                |                    |
| Pacific/Samoa                                            |                |                    |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Chamorro_Time_Zone         |                |                    |
|                                                          |                |                    |
| Chamorro, Guam                                           | +1000          | +1000              |
|                                                          |                |                    |
| Pacific/Guam                                             |                |                    |
+----------------------------------------------------------+----------------+--------------------+
| https://en.wikipedia.org/wiki/Time_in_Antarctica         |                |                    |
|                                                          |                |                    |
| Antarctica (Amundsen, McMurdo), South Pole               | +1200          | +1300              |
|                                                          |                |                    |
| Antarctica/South_Pole                                    |                |                    |
+----------------------------------------------------------+----------------+--------------------+

.. index:: Web Names
.. _web names:

Web Names
+++++++++++

* :term:`URL`
* :term:`URI`
* :term:`URN`
* :term:`Magnet URI`


.. index:: IEC
.. _iec:

IEC
+++++
| Wikipedia: https://en.wikipedia.org/wiki/International_Electrotechnical_Commission
| http://www.iec.ch/

IEC ("International Electrotechnical Commission") is a standards body.

List of IEC standards: https://en.wikipedia.org/wiki/List_of_IEC_standards


.. index:: IETF
.. _ietf:

IETF
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force
| Homepage: https://www.ietf.org/

IETF (*Internet Engineering Task Force*) is a standards body.

List of IETF standards: https://tools.ietf.org/html/


.. index:: ISO
.. _iso:

ISO
++++
| Wikipedia: https://en.wikipedia.org/wiki/International_Organization_for_Standardization
| Homepage: http://www.iso.org/

ISO (*International Organization for Standardization*) is a standards
body.

List of ISO standards: http://www.iso.org/iso/home/standards.htm


.. index:: W3C
.. _w3c:

W3C
++++
| Wikipedia: https://en.wikipedia.org/wiki/World_Wide_Web_Consortium
| Homepage: http://www.w3.org/

W3C (*World Wide Web Consortium*) is a standards body.

List of W3C standards: http://www.w3.org/TR/


.. index:: ISO8601
.. index:: iso8601
.. _iso8601:

ISO8601
+++++++++
| Wikipedia: https://en.wikipedia.org/wiki/ISO_8601
| Standard: http://www.iso.org/iso/iso8601

ISO8601 is a standard for specifying Gregorian
dates, times, datetime intervals, durations, and recurring datetimes.

An ISO8601 datetime is specified as:
year, month, day, hour, 'T' or space, minute, second, timezone.

A ``Z`` timezone specifies Universal Coordinated (or "Zulu") time.

* http://www.w3.org/TR/NOTE-datetime

Examples of ISO8601:

::

    2014
    2014-10
    2014-10-23
    20141023
    2014-10-23T20:59:30+Z       # UTC / Zulu
    2014-10-23T20:59:30Z        # UTC / Zulu
    2014-10-23T20:59:30-06:00   # CST
    2014-10-23T20:59:30-06      # CST
    2014-10-23T20:59:30-05:00   # CDT
    2014-10-23T20:59:30-05      # CDT
    20
    20:59
    2059
    20:59:30
    205930
    2014-10-23T20:59:30Z/2014-10-23T21:00:00Z
    2014-10-23T20:59:30-05:00/2014-10-23T21:00:00-06
    PT1H
    PT1M
    P1M
    P1Y1M1W1DT1H1M1S


.. note::
    AFAIU, ISO8601 does not specify standards for
    milliseconds, microseconds, nanoseconds, picoseconds, femtoseconds,
    or attoseconds.


.. index:: HTTP
.. _HTTP:

HTTP
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
| Standard: https://tools.ietf.org/html/rfc2616
| Standard: http://tools.ietf.org/html/rfc7230#page-5
| URI Scheme: ``http://``
| URI Scheme: ``https://``

HTTP (*HyperText Transfer Protocol*) is an :ref:`Open Source <open-source>`
text-based request-response
TCP/IP protocol for data interchange.

HTTPS (*Secure HTTP*) wraps HTTP in SSL/TLS to secure HTTP.

* https://www.mnot.net/blog/2014/06/07/rfc2616_is_dead


.. index:: HTTP in RDF
.. _httprdf:

HTTP in RDF
`````````````
| Standard: http://www.w3.org/TR/HTTP-in-RDF10/
| Namespace: `<http://www.w3.org/2011/http#>`__
| xmlns: ``@prefix http: <http://www.w3.org/2011/http#> .``
| xmlns: ``@prefix http-headers: <http://www.w3.org/2011/http-headers> .``
| xmlns: ``@prefix http-methods: <http://www.w3.org/2011/http-methods> .``
| xmlns: ``@prefix http-statusCodes: <http://www.w3.org/2011/http-statusCodes> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/http

HTTP-in-RDF is a standard for representing :ref:`HTTP` as :ref:`RDF`.


.. index:: RTMP
.. _rtmp:

RTMP
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Real_Time_Messaging_Protocol

RTMP is a TCP/IP protocol for streaming audio, video, and data
originally for Flash which is now :ref:`Open Source <open-source>`.

* https://en.wikipedia.org/wiki/Real_Time_Messaging_Protocol#Client_software

  * Adobe Flash Player
  * :ref:`VLC`

* https://en.wikipedia.org/wiki/Real_Time_Messaging_Protocol#Server_software

  * Adobe Flash Live Media Server
  * :ref:`AWS` S3 HTTP Object Storage, CloudFront :ref:`CDN`
  * Helix Universal Media Server
  * Red5 (:ref:`Open Source <open-source>`)
  * :ref:`ffmpeg` (:ref:`Open Source <open-source>`)
  * :ref:`nginx-rtmp-module` (:ref:`Open Source <open-source>`)
  * FreeSwitch (:ref:`OpenSource <open-source>`, VoIP, SIP, :ref:`Video Chat`)

* :ref:`WebRTC` solves for all of the RTMP use cases,
  and is becoming as or more widely deployed than Flash Player
  (especially with mobile devices).


.. index:: WebSocket
.. _websockets:

WebSocket
+++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/WebSocket
| URI Scheme: ``ws://``

WebSocket is a full-duplex (two-way) TCP/IP protocol
for audio, video, and data
which can interoperate with :ref:`HTTP` :ref:`Web Servers`.

* WebSockets are often more efficient than other methods
  for realtime HTTP like HTTP Streaming and long polling.
* WebSockets work with many/most HTTP proxies
* WebSockets

https://en.wikipedia.org/wiki/Comparison_of_WebSocket_implementations

* :ref:`Python`: pypi:gevent-websocket,
  pypi:websockets (:ref:`python3` asyncio),
  pypi:autobahn (:ref:`Python 2 <python>` pypi:twisted,
  :ref:`python3` asyncio)

See also: https://en.wikipedia.org/wiki/Push_technology, :ref:`WebRTC`



.. index:: WebRTC
.. _webrtc:

WebRTC
++++++++
| Wikipedia: https://en.wikipedia.org/wiki/WebRTC
| Homepage: http://www.webrtc.org/
| Standard: http://tools.ietf.org/wg/rtcweb/
| Docs: https://webrtc.github.io/samples/

WebRTC is a :ref:`web standard <web-standards>` for
decentralized or centralized
streaming of audio, video, and data
in :ref:`browser <browsers>`,
without having to download any plugins.


.. note:: WebRTC is supported by a growing number of browsers:
   http://iswebrtcreadyyet.com/

   Notably, :ref:`Internet Explorer` and :ref:`Safari` still require
   a plugin to handle :ref:`WebRTC`.


.. index:: HTTP/2
.. index:: HTTP2
.. index:: HTTP2.0
.. _http2:

HTTP/2
++++++
| Wikipedia: https://en.wikipedia.org/wiki/HTTP/2
| Homepage: https://http2.github.io/
| Standard: https://http2.github.io/http2-spec/
| Standard: https://http2.github.io/http2-spec/compression.html
| Standard: https://tools.ietf.org/html/draft-ietf-httpbis-http2

HTTP/2 (*HTTP 2.0*) is the newest standard for :ref:`HTTP`.

HTTP/2 is largely derived from the SPDY protocol.

* https://github.com/http2/http2-spec/wiki/Implementations


.. index:: HTML
.. _HTML:

HTML
+++++
| Wikipedia: https://en.wikipedia.org/wiki/HTML

HTML (*HyperText Markup Language*) is a :ref:`Open Source <open-source>`
standard for representing
documents with tags, attributes, and **hyperlinks**.

Recent HTML standards include :ref:`HTML4`, :ref:`XHTML`, and :ref:`HTML5`.


.. index:: HTML4
.. _HTML4:

HTML4
```````
| Standard: http://www.w3.org/TR/html4/

HTML4 is the fourth generation :ref:`HTML` standard.


.. index:: XHTML
.. _XHTML:

XHTML
``````
| Wikipedia: https://en.wikipedia.org/wiki/XHTML
| Standard: http://www.w3.org/TR/xhtml2/

XHTML is an :ref:`XML`-conforming :ref:`HTML` standard
which is being superseded by :ref:`HTML5`.

Compared to :ref:`HTML4`,
XHTML requires closing tags, suports additional namespace declarations,
and expects things to be wrapped in ``CDATA`` blocks,
among a few other notable differences.

XHTML has not gained the widespread adoption of :ref:`HTML4`,
and is being largely superseded by :ref:`HTML5`.


.. index:: HTML5
.. _HTML5:

HTML5
``````
| Standard: http://www.w3.org/TR/html5/

HTML5 is the fifth generation :ref:`HTML` standard
with many new (and removed) features.

Like its predecessors, HTML5 is not case sensitive,
but it is recommended to use lowercased tags and attributes.

**Differences Between HTML4 and HTML5**

https://html-differences.whatwg.org/

* HTML5 does not require closing tags
  (many browsers had already implemented routines for auto-closing broken
  markup).
* Frames have been removed
* Presentational attributes have been removed (in favor of CSS)

**HTML 5.1**

HTML 5.1 is in the works:

* http://www.w3.org/html/wg/drafts/html/master/


.. index:: XML
.. _XML:

XML
++++
| Wikipedia: https://en.wikipedia.org/wiki/XML
| Standard: http://www.w3.org/TR/xml/

XML (*Extensible Markup Language*) is a standard for representing data
with tags and attributes.

Like PDF, XML is derived from SGML.


.. index:: XSD
.. _XSD:

XSD
++++
| Wikipedia: `<https://en.wikipedia.org/wiki/XML_Schema_(W3C)>`__
| Standard: http://www.w3.org/TR/xmlschema11-2/
| Namespace: `<http://www.w3.org/2001/XMLSchema#>`__
| xmlns: ``@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/xsd

XSD (*XML Schema Datatypes*) are standard datatypes for things like
strings, integers, floats, and dates for :ref:`XML` and also :ref:`RDF`.


.. index:: JSON
.. _JSON:

JSON
+++++
| Wikipedia: https://en.wikipedia.org/wiki/JSON
| Standard: https://tools.ietf.org/html/rfc7159
| Homepage: http://json.org/

JSON (*JavaScript Object Notation*) is a standard for representing
data in a JavaScript compatible way; with a restricted set of
data types.

Conforming JSON does not contain JavaScript code, only data.
It is not safe to ``eval`` JSON, because it could contain code.

There are many parsers for JSON.

:ref:`JSON-LD` adds :ref:`RDF` Linked Data support to JSON
with ``@context``.


.. index:: CSV
.. _CSV:

CSV
++++
| Wikipedia: https://en.wikipedia.org/wiki/Comma-separated_values
| Standard: https://tools.ietf.org/html/rfc4180
| Extension: ``.csv``
| MIME Type: ``text/csv``

CSV (*Comma Separated Values*) as a flat file representation
for columnar data with rows and columns.

Most spreadsheet tools can export (raw and computed) data
from a sheet into a CSV file, for use with many other tools.

CSVW
`````
| Homepage: https://w3c.github.io/csvw/
| Standard: http://www.w3.org/TR/tabular-data-model/
| Standard: http://www.w3.org/TR/tabular-metadata/
| Standard: http://www.w3.org/TR/csv2json/
| Standard: http://www.w3.org/TR/csv2rdf/
| Namespace: `<http://www.w3.org/ns/csvw#>`__
| xmlns: ``@prefix csvw: <http://www.w3.org/ns/csvw#> .``
| @context: http://www.w3.org/ns/csvw.jsonld

CSVW (*CSV on the Web*) is a set of relatively new standards
for representing :ref:`CSV` rows and columns
as :ref:`RDF` (and :ref:`JSON` / :ref:`JSON-LD`)
along with *metadata*.

* URIs for datatypes (:ref:`XSD`, ...)
* URIs for columns (:ref:`RDF`)
* Document Metadata
* :ref:`CSV` -> :ref:`JSON` ( -> :ref:`JSON-LD` -> :ref:`RDF` )
* :ref:`CSV` -> :ref:`RDF`


.. index:: RDF
.. _RDF:

RDF
++++
| Wikipedia: https://en.wikipedia.org/wiki/Resource_Description_Framework
| xmlns: ``@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/rdf

RDF (*Resource Description Framework*) is a standard data model
for representing data as triples.

**Primer**

* http://www.w3.org/TR/rdf-primer/
* http://www.w3.org/TR/rdf11-primer/
* ** `<http://www.w3.org/TR/rdf11-primer/#section-Introduction>`__ **
* http://www.w3.org/TR/rdf11-primer/#section-vocabulary
* http://www.w3.org/TR/rdf11-primer/#section-data-model

**Concepts**

* http://www.w3.org/TR/rdf-concepts/
* http://www.w3.org/TR/rdf11-concepts/
* http://www.w3.org/TR/rdf11-concepts/#data-model
* http://www.w3.org/TR/rdf11-concepts/#change-over-time
* http://www.w3.org/TR/rdf11-concepts/#entailment
* http://www.w3.org/TR/rdf11-concepts/#section-blank-nodes
* http://www.w3.org/TR/rdf11-concepts/#xsd-datatypes
* http://www.w3.org/TR/rdf11-concepts/#section-html

**Useful Resources**

* "Linked Data Patterns:
  A pattern catalogue for modelling, publishing, and
  consuming Linked Data"
  http://patterns.dataincubator.org/book/


.. index:: N-Triples
.. _N-Triples:

N-Triples
```````````
| Wikipedia: https://en.wikipedia.org/wiki/N-Triples
| Standard: http://www.w3.org/TR/n-triples/
| Extension: ``.nt``
| MIME Type: ``application/n-triples``

N-Triples is a standard for serializing :ref:`RDF` triples to text.


.. index:: RDF/XML
.. _RDF/XML:

RDF/XML
````````
| Wikipedia: https://en.wikipedia.org/wiki/RDF/XML
| Standard: http://www.w3.org/TR/rdf-syntax-grammar/
| Extension: ``.rdf``
| MIME Type: ``application/rdf+xml``

RDF/XML is a standard for serializing :ref:`RDF` as :ref:`XML`.


.. index:: TriX
.. _TriX:

TriX
`````
| Wikipedia: `<https://en.wikipedia.org/wiki/TriX_(syntax)>`_

* http://www.w3.org/2004/03/trix/rdfg-1/

TriX is a standard which extends
the :ref:`RDF/XML` :ref:`RDF` serialization standard
with named graphs.

.. index:: N3
.. index:: Notation3
.. _n3:

N3
````
| Wikipedia: https://en.wikipedia.org/wiki/Notation3
| Standard: http://www.w3.org/TeamSubmission/n3/
| Extension: ``.n3``
| MIME Type: ``text/n3``

N3 (*Notation3*) is a standard which extends
the :ref:`Turtle` :ref:`RDF` serialization standard
with a few extra features.

* ``=>`` implies (useful for specifying production rules)


.. index:: Turtle
.. _turtle:

Turtle
````````
| Wikipedia: `<https://en.wikipedia.org/wiki/Turtle_(syntax)>`_
| Standard: http://www.w3.org/TR/turtle/
| Extension: ``.ttl``
| MIME type: ``text/turtle``

Turtle is a standard for serializing :ref:`RDF` triples
into human-readable text.

.. index:: TriG
.. _TriG:

TriG
`````
| Wikipedia: `<https://en.wikipedia.org/wiki/TriG_(syntax)>`_
| Standard: http://www.w3.org/TR/trig/
| Extension: ``.trig``
| MIME Type: ``application/trig``

TriG (...) extends the :ref:`Turtle` :ref:`RDF` standard
to allow multiple named graphs to be expressed in one file
(as triples with a named graph IRI ("quads")).

Triples without a specified named graph are, by default,
part of the "Default Graph".


.. index:: RDFa
.. _RDFa:

RDFa
``````
| Wikipedia: https://en.wikipedia.org/wiki/RDFa
| Homepage: http://www.w3.org/2001/sw/wiki/RDFa
| Standard: http://www.w3.org/TR/rdfa-core/
| Standard: http://www.w3.org/TR/rdfa-lite/
| Standard: http://www.w3.org/TR/html-rdfa/
| Docs: http://www.w3.org/TR/rdfa-primer/

RDFa (*RDF in attributes*) is a standard for storing
structured data (:ref:`RDF` triples) in :ref:`HTML`,
(:ref:`XHTML`, :ref:`HTML5`) attributes.

:ref:`Schema.org` structured data can be included in an HTML page as
RDFa.


.. index:: JSON-LD
.. _JSON-LD:

JSON-LD
````````
| Wikipedia: https://en.wikipedia.org/wiki/JSON-LD
| Homepage: http://json-ld.org/
| Standard: http://www.w3.org/TR/json-ld/

JSON-LD (*JSON Linked Data*) is a standard for expressing
:ref:`RDF` :ref:`Linked Data <linked-data>` as :ref:`JSON`.

JSON-LD specifies a ``@context`` for regular JSON documents
which maps JSON attributes to URIs with datatypes and, optionally, languages.

* http://json-ld.org/playground/


.. index:: RDFS
.. index:: RDF Schema
.. _RDFS:

RDFS
+++++
| Wikipedia: https://en.wikipedia.org/wiki/RDF_Schema
| Standard: http://www.w3.org/TR/rdf-schema/
| Namespace: `<http://www.w3.org/2000/01/rdf-schema#>`__
| xmlns: ``@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/rdfs

RDFS (*RDF Schema*) is an :ref:`RDF` standard for classes
and properties.

A few notable RDFS classes:

* ``rdfs:Resource`` (everything in RDF)
* ``rdfs:Literal`` (strings, integers)
* ``rdfs:Class``

A few notable / frequently used properties:

* ``rdfs:label``
* ``rdfs:comment``
* ``rdfs:seeAlso``

* ``rdfs:domain``
* ``rdfs:range``
* ``rdfs:subPropertyOf``

:ref:`OWL` builds upon many RDFS concepts.


.. index:: dcterms
.. index:: dctypes
.. index:: DCMI
.. _DCMI:

DCMI
`````
| Wikipedia: https://en.wikipedia.org/wiki/Dublin_Core
| Wikipedia: https://en.wikipedia.org/wiki/Dublin_Core#DCMI_Metadata_Terms
| Namespace: http://purl.org/dc/terms
| xmlns: ``@prefix dcterms: <http://purl.org/dc/terms> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/dcterms
| Namespace: http://purl.org/dc/dcmitype/
| xmlns: ``@prefix dctypes: <http://purl.org/dc/dcmitype/> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/dctype

DCTYPES (*Dublin Core Types*) and DCTERMS (*Dublin Core Terms*)
are standards for common types, classes, and properties
that have been mapped to :ref:`XML` and :ref:`RDF`.



.. index:: RDF Data Cube
.. index:: QB
.. _QB:

RDF Data Cubes
```````````````
| Standard: http://www.w3.org/TR/vocab-data-cube/
| Namespace: `<http://purl.org/linked-data/cube#>`__
| xmlns: ``@prefix qb: <http://purl.org/linked-data/cube#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/qb

RDF Data Cubes vocabulary is an :ref:`RDF` standard vocabulary for expressing
linked multi-dimensional statistical data and aggregations.

* Data Cubes have dimensions, attributes, and measures
* Pivot tables and crosstabulations can be expressed with
  RDF Data Cubes vocabulary


.. index:: SKOS
.. index:: Simple Knowledge Organization System
.. _SKOS:

SKOS
`````
| Wikipedia: https://en.wikipedia.org/wiki/Simple_Knowledge_Organization_System
| Standard: http://www.w3.org/TR/skos-reference/
| Standard: http://www.w3.org/TR/skos-reference/skos.html
| Namespace: `<http://www.w3.org/2004/02/skos/core#>`_
| xmlns: ``@prefix skos: <http://www.w3.org/2004/02/skos/core#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/skos

SKOS (*Simple Knowledge Organization System*) is an :ref:`RDF` standard
vocabulary for linking concepts and vocabulary terms.


.. index:: XKOS
.. index:: Extended Knowledge Organization System
.. _XKOS:

XKOS
``````
| Homepage: http://www.ddialliance.org/Specification/RDF/XKOS
| Standard: http://rdf-vocabulary.ddialliance.org/xkos.html
| Source: https://github.com/linked-statistics/xkos
| Namespace: `<http://rdf-vocabulary.ddialliance.org/xkos#>`__
| xmlns: ``@prefix xkos: <http://rdf-vocabulary.ddialliance.org/xkos#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/xkos

XKOS (*Extended Knowledge Organization System*) is an :ref:`RDF`
standard which extends :ref:`SKOS`
for linking concepts and statistical measures.


.. index:: FOAF
.. index:: Friend of a Friend
.. _FOAF:

FOAF
`````
| Wikipedia: `<https://en.wikipedia.org/wiki/FOAF_(ontology)>`__
| Homepage: http://www.foaf-project.org/
| Standard: http://xmlns.com/foaf/spec/
| Namespace: `<http://xmlns.com/foaf/0.1/>`__
| xmlns: ``@prefix foaf: <http://xmlns.com/foaf/0.1/> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/foaf

FOAF (*Friend of a Friend*) is an :ref:`RDF` standard vocabulary for
expressing social networks and contact information.


.. index:: SIOC
.. index:: Semantically Interlinked Online Communities
.. _SIOC:

SIOC
``````
| Wikipedia: https://en.wikipedia.org/wiki/Semantically-Interlinked_Online_Communities
| Homepage: http://www.sioc-project.org/
| Namespace: `<http://rdfs.org/sioc/ns#>`__
| xmlns: ``@prefix sioc: <http://rdfs.org/sioc/ns#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/sioc

SIOC (*Semantically Interlinked Online Communities*) is an :ref:`RDF`
standard for online social networks and resources
like blog, forum, and mailing list posts.


.. index:: OA
.. index:: OpenAnnotation
.. _OA:

OA
````
| Homepage: http://www.openannotation.org/
| Standard: http://www.openannotation.org/spec/core/
| Namespace: `<http://www.w3.org/ns/oa#>`__
| xmlns: ``@prefix oa: <http://www.w3.org/ns/oa#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/oa

OA (*Open Annotation*) is an :ref:`RDF` standard for
commenting on anything with a URI.

Features:

* Web Annotation: https://en.wikipedia.org/wiki/Web_annotation
* Comment on any resource with a (stable) URI
* Comment on text fragments
* Comment on SVG items

Implementations:

* https://github.com/hypothesis/h (Python, Pyramid)
* https://github.com/openannotation/annotator (http://annotatorjs.org/)


.. index:: Schema.org
.. _Schema.org:

Schema.org
+++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Schema.org
| Homepage: http://schema.org/
| Source: https://github.com/rvguha/schemaorg

Schema.org is a vocabulary for expressing structured data on the web.

Schema.org can be expressed as microdata, :ref:`RDF`, :ref:`RDFa`,
and :ref:`JSON-LD`.

* http://schema.org/docs/full.html
* http://schema.org/docs/schemas.html
* http://schema.org/docs/releases.html
* http://www.w3.org/wiki/WebSchemas
* http://www.w3.org/wiki/WebSchemas/SchemaDotOrgProposals


.. index:: Schema.org RDF
.. _schema.org-rdf:

Schema.org RDF
````````````````
| xmlns: ``@prefix schema: <http://schema.org/> .``
| xmlns: ``@prefix schemax: <http://topbraid.org/schemax/> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/schema

TopBraid maintains more complete :ref:`OWL` :ref:`RDF`
transformations of :ref:`Schema.org`.

* http://topbraid.org/schema/
* http://topbraid.org/schema/schema.rdf
* http://topbraid.org/schema/schema.ttl
* http://topbraid.org/schema/schema-single-range.ttl

Tools and Mappings

* https://github.com/mhausenblas/schema-org-rdf
* http://schema.rdfs.org/tools.html
* http://schema.rdfs.org/mappings.html



.. index:: SPARQL
.. _SPARQL:

SPARQL
+++++++
| Wikipedia: https://en.wikipedia.org/wiki/SPARQL
| Standard: http://www.w3.org/TR/sparql11-overview/
| Standard: http://www.w3.org/TR/sparql11-query/
| Standard: http://www.w3.org/TR/sparql11-update/
| Standard: http://www.w3.org/TR/sparql11-entailment/
| Standard: http://www.w3.org/TR/sparql11-federated-query/

SPARQL is a text-based query and update language
for :ref:`RDF` triples (and quads).

* http://www.w3.org/wiki/SparqlImplementations
* http://www.w3.org/2009/sparql/implementations/#sparql11-entailment

Challenges:

* SPARQL query requests and responses are over HTTP;
  however, it's best -- and often required --
  to build SPARQL queries with a server application,
  on behalf of clients.
* SPARQL default ``LIMIT`` clauses and paging windows
  could allow for more efficient caching
* See: :ref:`LDP` for more of a resource-based RESTful API
  that can be implemented on top of
  the graph pattern queries supported by SPARQL.


.. index:: Linked Data Platform
.. index:: LDP
.. _LDP:

LDP
++++
| Spec http://www.w3.org/TR/ldp/
| xmlns: ``@prefix ldp: <http://www.w3.org/ns/ldp#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/ldp

LDP (*Linked Data Platform*) is a standard for building :ref:`HTTP` REST APIs
for :ref:`RDF` :ref:`Linked Data <linked-data>`.

* http://www.w3.org/TR/ldp/#terms

Features:

* :ref:`HTTP` REST API for *Linked Data Platform Containers* (LDPC)
  containing Linked Data Plaform **Resources** (LDPR)
* Server-side *Paging*




.. index:: OWL
.. index:: Web Ontology Language
.. _OWL:

OWL
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Web_Ontology_Language
| Standard: http://www.w3.org/TR/owl2-overview/
| Standard: http://www.w3.org/TR/owl2-primer/
| Standard: http://www.w3.org/TR/owl2-quick-reference/
| Standard: http://www.w3.org/TR/owl2-profiles/
| xmlns: ``@prefix owl: <http://www.w3.org/2002/07/owl#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/owl

OWL (*Web Ontology Language*) adds semantics, reasoning, inference,
and entailment capabilities to :ref:`RDF`.


.. index:: PROV
.. _PROV:

PROV
```````
| Homepage: http://www.w3.org/2011/prov/wiki/Main_Page
| Standard: http://www.w3.org/ns/prov.owl
| Standard: http://www.w3.org/TR/prov-overview/
| Standard: http://www.w3.org/TR/prov-primer/
| Standard: http://www.w3.org/TR/prov-o/
| Namespace: `<http://www.w3.org/ns/prov#>`_
| xmlns: ``@prefix prov: <http://www.w3.org/ns/prov#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/prov

PROV (*Provenance*) ontology is an :ref:`OWL` :ref:`RDF` standard
for expressing data provenance (who, what, when, and how, to a certain
extent).

* https://en.wikipedia.org/wiki/Provenance#Data_provenance


.. index:: DBpedia
.. _dbpedia:

DBpedia
``````````
| Homepage: http://wiki.dbpedia.org/Ontology
| Namespace: http://dbpedia.org/ontology/
| xmlns: ``@prefix dbpedia-owl: <http://dbpedia.org/ontology/> .``
| LOVLink: http://dbpedia.org/ontology/

DBpedia is an :ref:`OWL` :ref:`RDF` vocabulary for expressing
structured data from Wikipedia sidebar infoboxes.

DBpedia is currently the most central (most linked to and from)
:ref:`RDF` vocabulary. (see: :ref:`LODCloud`)

Example:

* http://dbpedia.org/page/DBpedia
* http://en.wikipedia.org/wiki/DBpedia
* https://en.wikipedia.org/wiki/DBpedia
* https://en.wikipedia.org/wiki/dbpedia
* https://es.wikipedia.org/wiki/DBpedia
* `<http://ja.dbpedia.org/resource/DBペディア>`__
* `<https://ja.wikipedia.org/wiki/DBペディア>`__
* https://www.wikidata.org/wiki/Q465
* http://sw.cyc.com/concept/Mx4r7PXDuWpqTcmfojZNIu56eQ

DBpedia is generated by batch extraction on a regular basis.


.. index:: QUDT
.. _qudt:

QUDT
``````
| Homepage: http://www.linkedmodel.org/doc/qudt/1.1/
| Standard: http://qudt.org/
| Docs: http://www.linkedmodel.org/catalog/qudt/1.1/
| Namespace: `<http://qudt.org/schema/qudt#>`__
| Namespace: `<http://qudt.org/1.1/schema/qudt#>`__
| xmlns: ``@prefix qudt: <http://qudt.org/schema/qudt#> .``
| xmlns: ``@prefix qudt-1.1:  <http://qudt.org/1.1/schema/qudt#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/qudt

QUDT (*Quantities, Units, Dimensions, and Types*) is an :ref:`RDF` standard
vocabulary for representing physical units.

* QUDT is composed of a number of sub-vocabularies
* QUDT maintains conversion factors for Metric and Imperial Units

Examples:

* ``qudt:SpaceAndTimeUnit``

   .. code:: n3

      qudt:SpaceAndTimeUnit
         rdf:type owl:Class ;
         rdfs:label "Space And Time Unit"^^xsd:string ;
         rdfs:subClassOf qudt:PhysicalUnit ;
         rdfs:subClassOf
                 [ rdf:type owl:Restriction ;
                   owl:hasValue "UST"^^xsd:string ;
                   owl:onProperty qudt:typePrefix
                 ] .

* QUDT Namespaces:

  .. code:: n3

      @prefix qudt:           <http://qudt.org/schema/qudt#> .
      @prefix qudt-1.1:       <http://qudt.org/1.1/schema/qudt#> .
      @prefix qudt-dimension: <http://qudt.org/vocab/dimension#> .
      @prefix qudt-quantity:  <http://qudt.org/vocab/quantity#> .
      @prefix qudt-unit-1.1:  <http://qudt.org/1.1/vocab/unit#> .
      @prefix unit:           <http://qudt.org/vocab/unit#> .

This diagram explains how each of the vocabularies are linked and derived:
http://www.linkedmodel.org/catalog/qudt/1.1/


.. index:: QUDT Quantities
.. _qudt-quantities:

QUDT Quantities
``````````````````
Schema

| Standard: http://qudt.org/1.1/schema/quantity
| Namespace: `<http://qudt.org/1.1/schema/quantity#>`__
| xmlns: ``@prefix quantity: <http://data.nasa.gov/qudt/owl/quantity#> .``
| Turtle: http://qudt.org/1.1/schema/OSG_quantity-(v1.1).ttl

Vocabulary

| xmlns: ``@prefix qudt-quantity: <http://qudt.org/1.1/vocab/quantity#> .``
| Namespace: `<http://qudt.org/1.1/vocab/quantity#>`__
| Turtle: http://qudt.org/1.1/vocab/OVG_quantities-qudt-(v1.1).ttl

:ref:`QUDT` Quantities is an :ref:`RDF` schema and vocabulary for describing
physical quantities.

Examples from http://qudt.org/1.1/vocab/OVG_quantities-qudt-(v1.1).ttl :

* ``qudt-quantity:Time``

  .. code:: n3

      qudt-quantity:Time
          rdf:type qudt:SpaceAndTimeQuantityKind ;
          rdfs:label "Time"^^xsd:string ;
          qudt:description "Time is a basic component of the measuring system used to sequence events, to compare the durations of events and the intervals between them, and to quantify the motions of objects."^^xsd:string ;
          qudt:symbol "T"^^xsd:string ;
          skos:exactMatch <http://dbpedia.org/resource/Time> .
      # ...
      unit:SecondTime
          qudt:quantityKind qudt-quantity:Time .

* ``qudt-quantity:AreaTimeTemperature``

  .. code:: n3

      qudt-quantity:AreaTimeTemperature
          rdf:type qudt:ThermodynamicsQuantityKind ;
          rdfs:label "Area Time Temperature"^^xsd:string .
      # ...
      unit:SquareFootSecondDegreeFahrenheit
          qudt:quantityKind qudt-quantity:AreaTimeTemperature .


.. index:: QUDT Units
.. _qudt-units:

QUDT Units
````````````
| Standard: http://qudt.org/1.1/vocab/unit
| Namespace: `<http://qudt.org/1.1/vocab/unit#>`_
| xmlns: ``@prefix unit: <http://qudt.org/1.1/vocab/unit> .``
| xmlns: ``@prefix qudt-unit-1.1:  <http://qudt.org/1.1/vocab/unit#> .``
| Turtle: http://qudt.org/1.1/vocab/OVG_units-qudt-(v1.1).ttl

The :ref:`QUDT` Units Ontology is an :ref:`RDF` vocabulary
defining many units of measure.

Examples:

* ``unit:SecondTime``

  .. code:: n3

      unit:SecondTime
            rdf:type qudt:SIBaseUnit , qudt:TimeUnit ;
            rdfs:label "Second"^^xsd:string ;
            qudt:abbreviation "s"^^xsd:string ;
            qudt:code "1615"^^xsd:string ;
            qudt:conversionMultiplier
                    "1"^^xsd:double ;
            qudt:conversionOffset
                    "0.0"^^xsd:double ;
            qudt:symbol "s"^^xsd:string ;
            skos:exactMatch <http://dbpedia.org/resource/Second> .
      # ...

  http://www.qudt.org/qudt/owl/1.0.0/unit/Instances.html#SecondTime

* ``unit:HorsepowerElectric``

  http://qudt.org/1.1/vocab/OVG_units-qudt-(v1.1).ttl

  .. code:: n3

      unit:HorsepowerElectric
          rdf:type qudt:NotUsedWithSIUnit , qudt:PowerUnit ;
          rdfs:label "Horsepower Electric"^^xsd:string ;
          qudt:abbreviation "hp/V"^^xsd:string ;
          qudt:code "0815"^^xsd:string ;
          qudt:symbol "hp/V"^^xsd:string .

* ``unit:SystemOfUnits_SI``

  http://qudt.org/1.1/vocab/OVG_units-qudt-(v1.1).ttl

  .. code:: n3

      unit:SystemOfUnits_SI
            rdf:type qudt:SystemOfUnits ;
            rdfs:label "International System of Units"^^xsd:string ;
            qudt:abbreviation "SI"^^xsd:string ;
            qudt:systemAllowedUnit
                    unit:ArcMinute , unit:Day , unit:MinuteTime , unit:DegreeAngle , unit:ArcSecond , unit:ElectronVolt , unit:RevolutionPerHour , unit:Femtometer , unit:DegreePerSecond , unit:DegreeCelsius , unit:Liter , unit:MicroFarad , unit:AmperePerDegree , unit:RevolutionPerMinute , unit:MicroHenry , unit:Kilometer , unit:Revolution , unit:Hour , unit:PicoFarad , unit:Gram , unit:DegreePerSecondSquared , unit:MetricTon , unit:CubicCentimeter , unit:SquareCentimeter , unit:CubicMeterPerHour , unit:KiloPascal , unit:DegreePerHour , unit:UnifiedAtomicMassUnit , unit:MilliHenry , unit:KilogramPerHour , unit:KiloPascalAbsolute , unit:NanoFarad , unit:RadianPerMinute , unit:RevolutionPerSecond ;
            qudt:systemBaseUnit unit:Kilogram , unit:Unitless , unit:Kelvin , unit:Meter , unit:SecondTime , unit:Mole , unit:Candela , unit:Ampere ;
            qudt:systemCoherentDerivedUnit
                    unit:PerCubicMeter , unit:WattPerSquareMeter , unit:Volt , unit:WattPerMeterKelvin , unit:CoulombPerCubicMeter , unit:Becquerel , unit:WattPerSquareMeterSteradian , unit:KelvinPerSecond , unit:Gray , unit:RadianPerSecond , unit:VoltPerMeter , unit:HenryPerMeter , unit:WattPerSteradian , unit:JouleMeterPerMole , unit:CoulombMeter , unit:PerTeslaMeter , unit:Pascal , unit:LumenPerWatt , unit:KilogramMeterPerSecond , unit:SquareMeterKelvin , unit:MoleKelvin , unit:MeterKelvinPerWatt , unit:Steradian , unit:AmperePerMeter , unit:SquareMeterKelvinPerWatt , unit:JouleSecond , unit:MeterPerFarad , unit:KilogramPerSecond , unit:HertzPerTesla , unit:KilogramMeterSquared , unit:WattPerSquareMeterQuarticKelvin , unit:PerMeterKelvin , unit:JoulePerCubicMeterKelvin , unit:JoulePerSquareTesla , unit:JoulePerCubicMeter , unit:MeterPerKelvin , unit:AmperePerSquareMeter , unit:CubicCoulombMeterPerSquareJoule , unit:CoulombPerMeter , unit:Katal , unit:CubicMeter , unit:LumenSecond , unit:Coulomb , unit:MolePerKilogram , unit:CubicMeterPerKilogramSecondSquared , unit:PerMeter , unit:AmperePerRadian , unit:CoulombPerKilogram , unit:QuarticCoulombMeterPerCubicEnergy , unit:Tesla , unit:JoulePerKilogram , unit:MeterKelvin , unit:MeterPerSecond , unit:NewtonMeter , unit:CandelaPerSquareMeter , unit:Siemens , unit:CoulombSquareMeter , unit:KilogramPerCubicMeter , unit:KilogramSecondSquared , unit:Watt , unit:AmperePerJoule , unit:VoltPerSecond , unit:JoulePerKilogramKelvinPerCubicMeter , unit:PascalPerSecond , unit:CubicMeterPerMole , unit:KilogramPerMeter , unit:PascalSecond , unit:Joule , unit:HertzPerVolt , unit:KilogramPerSquareMeter , unit:PerTeslaSecond , unit:MolePerCubicMeter , unit:PerSecond , unit:JoulePerKelvin , unit:RadianPerSecondSquared , unit:Newton , unit:CubicMeterPerKelvin , unit:GrayPerSecond , unit:SquareMeterPerSecond , unit:CubicMeterPerKilogram , unit:KilogramPerMole , unit:SquareMeterPerKelvin , unit:SquareMeterSteradian , unit:TeslaSecond , unit:Ohm , unit:KelvinPerWatt , unit:JoulePerKilogramKelvinPerPascal , unit:WattSquareMeter , unit:MeterKilogram , unit:WattSquareMeterPerSteradian , unit:Hertz , unit:VoltPerSquareMeter , unit:CubicMeterPerSecond , unit:JoulePerMoleKelvin , unit:TeslaMeter , unit:JoulePerMole , unit:Lux , unit:FaradPerMeter , unit:PerMole , unit:JouleSecondPerMole , unit:AmpereTurnPerMeter , unit:VoltMeter , unit:SecondTimeSquared , unit:AmpereTurn , unit:JoulePerKilogramKelvin , unit:CoulombPerSquareMeter , unit:NewtonPerKilogram , unit:JoulePerSquareMeter , unit:Weber , unit:Henry , unit:MeterPerSecondSquared , unit:KilogramKelvin , unit:Sievert , unit:NewtonPerMeter , unit:WattPerSquareMeterKelvin , unit:SquareCoulombMeterPerJoule , unit:Lumen , unit:Farad , unit:HertzPerKelvin , unit:SquareMeter , unit:JoulePerTesla , unit:Radian , unit:KelvinPerTesla , unit:NewtonPerCoulomb , unit:CoulombPerMole ;
            qudt:systemPrefixUnit
                    unit:Hecto , unit:Nano , unit:Tera , unit:Atto , unit:Kilo , unit:Yocto , unit:Yotta , unit:Deci , unit:Zepto , unit:Pico , unit:Femto , unit:Milli , unit:Micro , unit:Zetta , unit:Mega , unit:Centi , unit:Giga , unit:Peta , unit:Deca , unit:Exa ;
            skos:exactMatch <http://dbpedia.org/resource/International_System_of_Units> .


.. index:: Semantic Web Tools
.. _semantic-web-tools:

Semantic Web Tools
---------------------

.. index: Protégé
.. _protege:

Protégé
+++++++++
| Wikipedia: `<https://en.wikipedia.org/wiki/Protégé_(software)>`__
| Homepage: http://protege.stanford.edu/
| Homepage: http://webprotege.stanford.edu/

Protégé is a knowledge management software application with support for
:ref:`RDF`, :ref:`OWL`, and a few different reasoners.

Web Protégé is a web-based version of Protégé with many similar
features.

Protégé is a Free and Open Source software tool.


.. index:: RDFJS
.. _RDFJS:

RDFJS
++++++
| Homepage: http://www.w3.org/community/rdfjs/

RDFJS (:ref:`RDF` Javascript) is an acronym for referring to
tools for working with :ref:`RDF` in the Javascript programming
language.

http://www.w3.org/community/rdfjs/wiki/Comparison_of_RDFJS_libraries


.. index:: RDFHDT
.. _RDFHDT:

RDFHDT
++++++++
| Homepage: http://www.rdfhdt.org/

RDFHDT (:ref:`RDF` Header Dictionary Triples) is an optimized binary
format for storing and working with very many triples in highly compressed
form.

HDT-IT is a software application for working with RDFHDT datasets:

* https://code.google.com/p/hdt-it/
* https://www.youtube.com/watch?v=HMPkc725sMY


.. index:: RDFLib
.. _RDFLib:

RDFLib
+++++++
| Wikipedia: https://en.wikipedia.org/wiki/RDFLib
| Homepage: https://github.com/RDFLib
| Source: https://github.com/RDFLib/rdflib
| Docs: https://rdflib.readthedocs.org/en/latest/

RDFLib is a library (and a collection of companion libraries)
for working with :ref:`RDF` in the Python programming language.

* https://rdflib.readthedocs.org/en/latest/gettingstarted.html
* https://rdflib.readthedocs.org/en/latest/apidocs/examples.html
* https://rdflib.readthedocs.org/en/latest/apidocs/rdflib.html#module-rdflib.resource


.. index:: Semantic Web Schema Resources
.. _semantic-web-schema-resources:

Semantic Web Schema Resources
-------------------------------

.. index:: prefix.cc
.. _prefix.cc:

prefix.cc
++++++++++++
| Homepage: http://prefix.cc
| Docs:

Lookup :ref:`RDF` vocabularies, classes, and properties


.. index:: Linked Open Vocabularies
.. index:: LOV
.. _lov:

LOV
++++
| Homepage: http://lov.okfn.org/
| Source: git https://github.com/pyvandenbussche/lov
| SPARQL: http://lov.okfn.org/dataset/lov/sparql
| Docs: http://lov.okfn.org/dataset/lov/api

LOV ("Linked Open Vocabularies") is a web application
for cataloging and viewing metadata of and links between
vocabularies (:ref:`RDF`, :ref:`RDFS`, :ref:`OWL`)

* All of the vocabularies stored in LOV as a bubble chart:

  http://lov.okfn.org/dataset/lov/

* LOV has a "suggest a vocabulary" feature
* Many of the vocabularies stored in LOV
  can also be searched or looked up from :ref:`prefix.cc`.


.. index:: URIs for Units
.. _uris for units:

URIs for Units
+++++++++++++++++++

* https://lists.w3.org/Archives/Public/public-vocabs/2014Jan/0157.html

  * https://lists.w3.org/Archives/Public/public-vocabs/2015May/
  * https://lists.w3.org/Archives/Public/public-vocabs/2015May/thread.html



.. index:: LODCloud
.. _lodcloud:

LODCloud
+++++++++
| Homepage: http://lod-cloud.net
| Source: git https://github.com/lod-cloud/datahub2void
| Datasets: http://datahub.io/group/lodcloud
| Download: http://lod-cloud.net/data/void.ttl

The LOD ("Linking Open Data") cloud diagram visualizes
the nodes and edges of the *Linked Open Data Cloud*

* http://lod-cloud.net/#history
* http://lod-cloud.net/versions/2014-08-30/lod-cloud.svg


