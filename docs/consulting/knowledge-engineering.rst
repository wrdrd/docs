
.. index:: Knowledge Engineering
.. _knowledge engineering:

Knowledge Engineering
========================
| Wikipedia: https://en.wikipedia.org/wiki/Knowledge_engineering
| Wikipedia: https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Knowledge
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Graph_theory
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Ontology
| WikipediaCategory: `<https://en.wikipedia.org/wiki/Category:Ontology_(information_science)>`_


* https://en.wikipedia.org/wiki/Knowledge#Communicating_knowledge

* https://en.wikipedia.org/wiki/Schema



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
| Wikipedia: https://en.wikipedia.org/wiki/Logic
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Logic

https://en.wikipedia.org/wiki/List_of_logic_symbols


.. index:: Set Theory
.. _set-theory:

Set Theory
````````````
| Wikpedia: https://en.wikipedia.org/wiki/Set_theory


.. index:: Boolean Algebra
.. _boolean-algebra:

Boolean Algebra
````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Boolean_algebra


.. index:: Many-valued Logic
.. _many-valued-logic:

Many-valued Logic
````````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Many-valued_logic


.. index:: Three-valued Logic
.. _three-valued-logic:

Three-valued Logic
~~~~~~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Three-valued_logic

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
| Wikipedia: https://en.wikipedia.org/wiki/Fuzzy_logic


.. index:: Probabilistic Logic
.. _probabilistic-logic:

Probabilistic Logic
~~~~~~~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Probabilistic_logic


.. index:: Propositional Logic
.. _propsitional-logic:

Propositional Logic
`````````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Propositional_logic


.. index:: First-order Logic
.. index:: FOL
.. _FOL:

First-order Logic
```````````````````
| Wikipedia: https://en.wikipedia.org/wiki/First-order_logic

First-order (*FOL*)


.. index:: Description Logic
.. index:: DL
.. _DL:

Description Logic
```````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Description_logic

Description Logic (*DL*; DLP (Description Logic Programming))

* https://en.wikipedia.org/wiki/Description_logic#Notation
* https://en.wikipedia.org/wiki/Description_logic#Relationship_with_other_logics

Knowledge Base = TBox + ABox

* https://en.wikipedia.org/wiki/TBox (Schema: Class/Property Ontology)
* https://en.wikipedia.org/wiki/ABox (Facts / Instances)

See:

* :ref:`OWL`, :ref:`entailment`
* :ref:`Semantic web`
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
| Inference: https://en.wikipedia.org/wiki/Inference

* https://en.wikipedia.org/wiki/Rule_of_inference (Logic)
* https://en.wikipedia.org/wiki/Category:Statistical_inference (Logic + Math)


.. index:: Entailment
.. _entailment:

Entailment
~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Entailment

* http://www.w3.org/TR/owl2-profiles/#Introduction

See: :ref:`data science`


.. index:: Data Engineering
.. _data engineering:

Data Engineering
-----------------

Data Engineering is about the 5 Ws (who, what, when, where, why)
and **how** data are stored.

| Who:   schema:author         ``@westurner`` ;
| What:  schema:name           "WRD R&D Documentation"@en ;
| When:  schema:codeRepository <`<https://github.com/wrdrd/docs/commits/master>`__> ;
| Where: schema:codeRepository <`<https://github.com/wrdrd/docs>`__> ;
| Why:   schema:description    "Documentation purposes"@en ;
| How:   schema:programmingLanguage :ReStructuredText ;
| How:   schema:runtimePlatform [ :Python, :CPython, :Sphinx ] ;

.. contents::
   :local:


.. index:: File Structures
.. _file structures:

File Structures
+++++++++++++++++
https://en.wikipedia.org/wiki/File_format

`<https://en.wikipedia.org/wiki/Record_(computer_science)>`_

`<https://en.wikipedia.org/wiki/Field_(computer_science)>`_

https://en.wikipedia.org/wiki/Index#Computer_science

* :ref:`tar` and :ref:`zip` are file structures
  that have a *manifest* and a *payload*

  * :ref:`filesystems` often have redundant manifests
    (and/or deduplication according to a hash table manifest
    with an interface like a :ref:`dht`)

* :ref:`web standards` and :ref:`semantic web standards` which define
  file structures (and stream protocols):

  * :ref:`XML`
  * :ref:`RDF` (:ref:`RDF/XML`, :ref:`Turtle`, :ref:`n3`, :ref:`rdfa`,
    :ref:`json-ld`)
  * :ref:`JSON` (:ref:`json-ld`)
  * :ref:`HTTP`


.. index:: Git File Structures
.. _git file structures:

Git File Structures
``````````````````````
:ref:`Git` specifies a number of file structures:
:ref:`Git Objects <git object>`,
:ref:`Git References <git reference>`,
and :ref:`Git Packfiles <git packfile>`.

Git implements something like **on-disk** *shared snapshot objects*
with commits, branching, merging, and multi-protocol push/pull
semantics: https://en.wikipedia.org/wiki/Shared_snapshot_objects


.. index:: Git Object
.. _git object:

Git Object
~~~~~~~~~~~~~
| Docs: https://git-scm.com/book/en/v2/Git-Internals-Git-Objects


.. index:: Git Reference
.. _git reference:

Git Reference
~~~~~~~~~~~~~~~~
| Docs: https://git-scm.com/book/en/v2/Git-Internals-Git-References


.. index:: Git Packfile
.. _git packfile:

Git Packfile
~~~~~~~~~~~~~~~~
| Docs: https://git-scm.com/book/en/v2/Git-Internals-Packfiles

  "Git is a content-addressable :ref:`filesystem <filesystems>`"


.. index:: Bup
.. _bup:

==========
bup
==========
| Homepage: https://bup.github.io/
| Source: git https://github.com/bup/bup
| Docs: https://github.com/bup/bup/blob/master/README.md
| Docs: https://bup.github.io/man.html
| Docs: https://github.com/bup/bup/blob/master/DESIGN

Bup (*backup*) is a backup system based on :ref:`git packfiles <git packfile>`
and rolling checksums.

    [:ref:`Bup` is a very] efficient backup system
    based on the :ref:`git packfile` format,
    providing fast incremental saves
    and global deduplication
    (among and within files, including virtual machine images).



.. index:: Torrent file structure
.. _torrent file structure:

Torrent file structure
```````````````````````
A :term:`bittorrent torrent file` is an encoded manifest
of tracker, :ref:`DHT`, and :term:`web seed <web seeding>` :term:`URIs <URI>`;
and segment checksum hashes.

* Like :ref:`MPEG-DASH` and :ref:`HTTP Live Streaming`,
  :ref:`bittorrent` downloads file segments
  over :ref:`http`.

See: :ref:`bittorrent`, :ref:`named data networking`, :ref:`web distribution`


.. index:: File Locking
.. _file locking:

File Locking
++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/File_locking

File locking is one strategy for synchronization
with concurrency and parallelism.

* An auxilliary ``<filename>.lock`` file
  is still susceptible to *race conditions*
* :ref:`C` file locking functions: ``fcntl``, ``lockf``, ``flock``
* :ref:`Python` file locking functions: ``fcntl.fcntl``, ``fcntl.lockf``,
  ``fcntl.flock``:
  https://docs.python.org/2/library/fcntl.html
* To lock a file for all processes with :ref:`Linux` requires
  a *mandatory file locking* mount option (`mount -o mand``) and
  per-file setgid and noexec bits (``chmod g+s,g-s``).
* To lock a file (or a range / record of a file) for all processes with
  :ref:`Windows` requires no additional work beyond
  ``win32con.LOCKFILE_EXCLUSIVE_LOCK``,
  ``win32file.LockFileEx``, and ``win32file.UnlockFileEx``.
* CWE-667: Improper Locking:
  https://cwe.mitre.org/data/definitions/667.html#Relationships

  + https://en.wikipedia.org/wiki/File_locking#Problems
  + https://en.wikipedia.org/wiki/Race_condition
  + CWE-833: Deadlock

    https://cwe.mitre.org/data/definitions/833.html

    https://en.wikipedia.org/wiki/Deadlock




.. index:: Data Structures
.. _data structures:

Data Structures
++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Data_structure
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Data_structures
| Docs: https://en.wikipedia.org/wiki/List_of_data_structures

* http://rosettacode.org/wiki/Category:Programming_Tasks

  * http://rosettacode.org/wiki/Greatest_common_divisor
  * http://rosettacode.org/wiki/Go_Fish


.. index:: Arrays
.. _arrays:

Arrays
````````
| Wikipedia: https://en.wikipedia.org/wiki/Array_data_structure
| Docs: https://en.wikipedia.org/wiki/List_of_data_structures#Arrays

An array is a data structure for unidimensional data.

* Arrays must be resized when data grows beyond the initial
  shape of the array.
* Sparse arrays are sparsely allocated.
* A multidimensional array is said to be a :ref:`matrix <matrix>`.


.. index:: Matrix
.. index:: Matrices
.. _matrix:

Matrices
``````````
| Wikipedia: `<https://en.wikipedia.org/wiki/Matrix_(computer_science)>`_

A matrix is a data structure for multidimensional data;
a multidimensional :ref:`array <arrays>`.


.. index:: Lists
.. _lists:

Lists
```````
| Wikipedia: https://en.wikipedia.org/wiki/Linked_list
| Docs: https://en.wikipedia.org/wiki/List_of_data_structures#Lists

A list is a data structure with nodes that link to
a next and/or previous node.


.. index:: Graphs
.. _graphs:

Graphs
````````
| Wikipedia: `<https://en.wikipedia.org/wiki/Graph_(abstract_data_type)>`__
| Wikipedia: `<https://en.wikipedia.org/wiki/Graph_(mathematics)>`__
| Wikipedia: `<https://en.wikipedia.org/wiki/Graph_theory>`__
| Docs: https://en.wikipedia.org/wiki/Conceptual_graph
| WikipediaCategory: `<https://en.wikipedia.org/wiki/Category:Graphs>`__
| WikipediaCategory: `<https://en.wikipedia.org/wiki/Category:Graph_data_structures>`__
| WikipediaCategory: `<https://en.wikipedia.org/wiki/Category:Graph_theory>`__

A graph is a :term:`system` of nodes connected by edges;
an abstract data type for which there are a number of
suitable data structures.

* A node has edges.
* An edge connects nodes.

* Edges of **directed graphs** flow in only one direction;
  and so require two edges with separate attributes
  (e.g. 'magnitude', 'scale'

  | Wikipedia: https://en.wikipedia.org/wiki/Directed_graph

* Edges of an **undirected graph** connect nodes
  in both directions (with the same attributes).

  | Wikipedia: `<https://en.wikipedia.org/wiki/Graph_(mathematics)#Undirected_graph>`__

* Graphs and :ref:`trees` are **traversed** (or *walked*);
  according to a given algorithm (e.g. :ref:`DFS`, :ref:`BFS`).

* Graph nodes can be listed in many different *orders*
  (or with a given *ordering*):

  * Preoder
  * Inorder
  * Postorder
  * Level-order

* There are many :ref:`data structure <data structures>`
  representatations for :ref:`graphs`.

* There are many data serialization/marshalling
  formats for graphs:

  * Graph edge lists can be stored as adjacency :ref:`matrices <matrix>`.
  * :ref:`NetworkX` supports a number of graph storage formats.
  * :ref:`RDF` is a :ref:`standard semantic web <semantic web standards>`
    :ref:`linked data` format for :ref:`graphs`.
  * :ref:`JSON-LD` is a :ref:`standard semantic web <semantic web standards>`
    :ref:`linked data` format for :ref:`graphs`.

* There are many :ref:`Graph Databases` and :ref:`triplestores`
  for storing graphs.

* A cartesian product has an interesting graph representation.
  (See :ref:`compression algorithms`)


.. index:: NetworkX
.. _networkx:

NetworkX
~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/NetworkX
| Homepage: https://networkx.github.io/
| Source: git https://github.com/networkx/networkx
| Docs: https://networkx.github.io/documentation.html
| Docs: https://networkx.github.io/documentation/latest/
| Docs: https://networkx.github.io/documentation/latest/tutorial/
| Docs: https://networkx.github.io/documentation/latest/reference/classes.html
| Docs: https://networkx.github.io/documentation/latest/reference/algorithms.html

NetworkX is an :ref:`open source` graph algorithms library
written in :ref:`Python`.



.. index:: DFS
.. index:: Depth-first search
.. _dfs:

DFS
~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Depth-first_search

DFS (*Depth-first search*) is a :ref:`graph <graphs>` traversal algorithm.

::

    # Given a tree:
    1
      1.1
      1.2
    2
      2.1
      2.2

    # BFS:
    [1, 1.1, 1.2, 2, 2.1, 2.2

See also: :ref:`BSP`, Firefly Algorithm


.. index:: BFS
.. index:: Breadth-first search
.. _bfs:

BFS
~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Breadth-first_search

BFS (*Breadth-first search*) is a :ref:`graph <graphs>` traversal agorithm.

::

    # Given a tree:
    1
      1.1
      1.2
    2
      2.1
      2.2

    # BFS:
    1, 2, 1.1, 1.2, 2.1, 2.2

* [ ] BFS and :ref:`BSP`


.. index:: Topological Sorting
.. _topological sorting:

Topological Sorting
~~~~~~~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Topological_sorting

A DAG (*directed acyclic* :ref:`graph <graphs>`) has a
topological sorting, or is topologically sorted.

* The unix ``tsort`` utility does a topological sorting
  of a space and newline delimited list of edge
  labels:

.. code:: bash

    $ tsort --help
    Usage: tsort [OPTION] [FILE]
    Write totally ordered list consistent with the partial ordering in FILE.
    With no FILE, or when FILE is -, read standard input.

        --help     display this help and exit
        --version  output version information and exit

    GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
    For complete documentation, run: info coreutils 'tsort invocation'

    $ echo -e '1 2\n2 3\n3 4\n2 a' | tsort
    1
    2
    a
    3
    4

* Installing a set of packages with dependencies
  is a topological sorting problem;
  plus e.g. version and platform constraints
  (as solvable with a SAT constraint satisfaction solver
  (see :ref:`conda` (pypi:pycosat)))

* A topological sorting can identify the
  "root" of a **directed acyclic graph**.

  * *Information gain* can be useful
    for less discrete problems.


.. index:: Trees
.. _trees:

Trees
```````
| Wikipedia: https://en.wikipedia.org/wiki/Tree_data_structure
| Docs: http://rosettacode.org/wiki/Tree_traversal

A tree is a directed :ref:`graph <graphs>`.

* A tree is said to have branches and leaves; or just nodes.

There are many types of and applications for trees:

* https://en.wikipedia.org/wiki/List_of_data_structures#Trees
* https://en.wikipedia.org/wiki/B-tree
* https://en.wikipedia.org/wiki/Trie
* https://en.wikipedia.org/wiki/Abstract_syntax_tree
* https://en.wikipedia.org/wiki/Parse_tree
* https://en.wikipedia.org/wiki/Decision_tree
* https://en.wikipedia.org/wiki/Minmax
* https://en.wikipedia.org/wiki/Database_index
* Search: Indexing, Lookup


.. index:: Compression Algorithms
.. _compression algorithms:

Compression Algorithms
+++++++++++++++++++++++++

.. index:: bzip2
.. _bzip2:

bzip2
```````
| Wikipedia: https://en.wikipedia.org/wiki/Bzip2
| File Extension: ``.bz2``
| Homepage: http://bzip.org/

bzip2 is an :ref:`open source` lossless compression algorithm
based upon the ``Burrows-Wheeler`` algorithm.

* bzip2 is usually slower than :ref:`gzip` or :ref:`zip`,
  but more space efficient


.. index:: gzip
.. _gzip:

gzip
``````
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
````
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
````
| Wikipedia: `<https://en.wikipedia.org/wiki/Zip_(file_format)>`__

zip is a lossless file archive compression


.. index:: Checksums
.. index:: Hash Functions
.. _hash function:

Hash Functions
++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Hash_function
| Wikipedia: https://en.wikipedia.org/wiki/Cryptographic_hash_function

Hash functions (or *checksums*) are one-way functions
designed to produce uniquely identifying identifiers for blocks
or whole files in order to verify data :ref:`integrity`.

* A *hash* is the output of a hash function.
* In :ref:`Python`, ``dict`` keys must be *hashable*
  (must have a ``__hash__`` method).
* In :ref:`Java`, :ref:`Scala`, and many other languages
  ``dicts`` are called ``HashMaps``.
* :ref:`MD5` is a checksum algorithm.
* :ref:`SHA` is a group of checksum algorithms.


.. index:: CRC
.. index:: Cyclical Redundancy Check
.. _crc:

CRC
````
| Wikipedia: https://en.wikipedia.org/wiki/Cyclic_redundancy_check

A CRC (*Cyclical Redundancy Check*) is a hash function
for error detection based upon an extra *check value*.

* :ref:`Hard drives` and :ref:`SSDs <ssd>` implement CRCs.
* :ref:`Ethernet` implements CRCs.


.. index:: MD5
.. _md5:

MD5
`````
| Wikipedia: https://en.wikipedia.org/wiki/MD5

MD5 is a 128-bit hash function which is now broken, and deprecated
in favor of :ref:`SHA-2 <sha>` or better.

.. code:: bash

    md5
    md5sums


.. index:: SHA
.. _sha:

SHA
````
| Wikipedia: https://en.wikipedia.org/wiki/Secure_Hash_Algorithm

* SHA-0 --  160 bit (retracted 1993)
* SHA-1 --- 160 bit (deprecated 2010)
* SHA-2 --- sha-256, sha-512
* SHA-3 (2012)

.. code:: bash

    shasum
    shasum -a 1
    shasum -a 224
    shasum -a 256
    shasum -a 384
    shasum -a 512
    shasum -a 512224
    shasum -a 512256


.. index:: Filesystems
.. index:: File Systems
.. _filesystems:

Filesystems
++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/File_system

Filesystems (*file systems*) determine how files are
represented in a persistent physical medium.

* On-disk filesystems determine where and how redundantly data is stored
* On-disk filesystems: :ref:`ext`, :ref:`btrfs`,
  :ref:`FAT`, :ref:`NTFS`, :ref:`HFS+`
* :ref:`network filesystems` link disk storage pools with other resources
  (e.g. :ref:`NFS`, :ref:`Ceph`, :ref:`GlusterFS`)


.. index:: RAID
.. _raid:

RAID
``````
| Wikipedia: https://en.wikipedia.org/wiki/RAID

RAID (*redundant array of independent disks*)
is set of configurations for :ref:`hard drives` and :ref:`SSDs <ssd>`
to *stripe* and/or *mirror* with *parity*.

::

  RAID 0 -- striping,        -,             no parity ... throughput
  RAID 1 -- no striping,  mirroring,        no parity ...
  RAID 2 -- bit striping,    -,             no parity ... legacy
  RAID 3 -- byte striping,   -,      dedicated parity ... uncommon
  RAID 4 -- block striping,  -,      dedicated parity
  RAID 5 -- block striping,  -,    distributed parity ... min. 3; n-1 rebuild
  RAID 6 -- block striping,  -, 2x distributed parity

RAID Implementations:

* RAID may be implemented by a physical controller with
  multiple drive connectors.
* RAID may be implemented as a BIOS setting.
* RAID may be implemented with software e.g. :ref:`lvm`, :ref:`btrfs`.

* https://en.wikipedia.org/wiki/RAID#Software-based
* https://en.wikipedia.org/wiki/RAID#Firmware-_and_driver-based ("*fake RAID*")

* Data Scrubbing
    Data scrubbing is a technique for checking
    for inconsistencies between redundant copies of data

    Data scrubbing is routinely part of RAID
    (with *mirrors* and/or *parity* bits).

    https://en.wikipedia.org/wiki/Data_scrubbing



.. index:: MBR
.. _mbr:

MBR
`````
| Wikipedia: https://en.wikipedia.org/wiki/Master_boot_record

MBR (*Master Boot Record*) is a
boot record format and a
file partition scheme.

* DOS and :ref:`Windows` use MBR partition tables.
* Many/most UNIX variants support MBR partition tables.
* :ref:`Linux` supports MBR partition tables.
* Most PCs since 1983 boot from MBR partition tables.
* When a PC boots, it reads the MBR on the first configured
  drive in order to determine where to find the bootloader.


.. index:: GPT
.. _gpt:

GPT
`````
| Wikipedia: https://en.wikipedia.org/wiki/GUID_Partition_Table

GPT (*GUID Partition Table*) is a
boot record format and a
file partition scheme
wherein partitions are assigned GUIDs (*Globally Unique Identifiers*).

* :ref:`OSX` uses GPT partition tables.
* :ref:`Linux` supports GPT partition tables.
* https://en.wikipedia.org/wiki/GUID_Partition_Table#UNIX_and_Unix-like_operating_systems


.. index:: LVM
.. index:: Logical Volume Manager
.. _lvm:

LVM
``````````````````````
| Wikipedia: `<https://en.wikipedia.org/wiki/Logical_Volume_Manager_(Linux)>`__
| Homepage: https://www.sourceware.org/lvm2/
| Source: ftp://sources.redhat.com/pub/lvm2/
| Docs: https://www.sourceware.org/dm/
| Docs: http://www.tldp.org/HOWTO/LVM-HOWTO/index.html
| Docs: http://www.tldp.org/HOWTO/LVM-HOWTO/anatomy.html

LVM (*Logical Volume Manager*) is an :ref:`open source`
software disk abstraction layer with snapshotting, copy-on-write,
online resize and allocation and a number of additional features.

* In LVM, there are *Volume Groups* (VG),
  *Physical Volumes* (PV), and *Logical Volumes* (LV).
* LVM can do striping and high-availability sofware :ref:`RAID`.
* LVM and ``device-mapper`` are now part of the :ref:`Linux`
  kernel tree
  (the LVM :ref:`linux` kernel modules are built and included
  with most distributions' default kernel build).
* LVM Logical Volumes can be resized online
  (without e.g. rebooting to busybox or a LiveCD);
  but many :ref:`filesystems` support only
  onlize grow (and not online shrink).
* There is feature overlap between :ref:`lvm` and :ref:`btrfs`
  (pooling, snapshotting, copy-on-write).


.. index:: btrfs
.. _btrfs:

btrfs
```````
| Wikipedia: https://en.wikipedia.org/wiki/Btrfs
| Homepage: https://btrfs.wiki.kernel.org/index.php/Main_Page
| Source: https://btrfs.wiki.kernel.org/index.php/Btrfs_source_repositories
| Source: git git://git.kernel.org/pub/scm/linux/kernel/git/mason/btrfs-progs.git
| Docs: https://btrfs.wiki.kernel.org/index.php/Getting_started#Basic_Filesystem_Commands
| Docs: https://btrfs.wiki.kernel.org/index.php/Problem_FAQ
| Docs: https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Storage_Administration_Guide/ch-btrfs.html
| Docs: https://wiki.archlinux.org/index.php/Btrfs
| Docs: https://help.ubuntu.com/community/btrfs

btrfs (:ref:`B-tree <trees>` *filesystem*) is an
:ref:`open source` pooling, snapshotting,
checksumming, deduplicating, union mounting
copy-on-write on-disk :ref:`Linux` filesystem.


.. index:: ext2
.. index:: ext3
.. index:: ext4
.. _ext:

ext
````
| Wikipedia: https://en.wikipedia.org/wiki/Ext2
| Wikipedia: https://en.wikipedia.org/wiki/Ext3
| Wikipedia: https://en.wikipedia.org/wiki/Ext4

ext2, ext3, and ext4 are the ext (*extended filesystem*)
:ref:`open source`
on-disk filesystems.

* ext filesystems are the default filesystems of many
  :ref:`Linux` distributions.
* :ref:`windows` machines can access ext2, ext3, and ext4 filesystems
  with ext2explore and ext2fsd.
* :ref:`OSX` machines can access ext2, ext3, and ext4 filesystems
  with OSXFuse and FUSE-EXT2.


.. index:: FAT
.. index:: FAT12
.. index:: FAT16
.. index:: FAT32
.. _fat:

FAT
`````
| Wikipedia: https://en.wikipedia.org/wiki/File_Allocation_Table

FAT is a group of on-disk filesystem standards.

* FAT is used on cross-platform USB drives.
* FAT is found on older :ref:`Windows` and DOS machines.
* FAT12, FAT16, and FAT32 are all FAT filesystem standards.
* FAT32 has a maximum filesize of 4GB and a maximum volume size of 2 TB.
* :ref:`Windows` machines can read and write FAT partitions.
* :ref:`OSX` machines can read and write FAT partitions.
* :ref:`Linux` machines can read and write FAT partitions.


.. index:: ISO9660
.. _iso9660:

ISO9660
`````````
| Wikipedia: https://en.wikipedia.org/wiki/ISO_9660
| FileExt: ``.iso``

ISO9660 is an :ref:`ISO` standard for :ref:`disc drive <disc drives>` images
which specifies a standard for booting from a filesystem image.

* Many :ref:`Operating System <operating systems>`
  distributions are distributed
  as :ref:`ISO9660` ``.iso`` files.
* ISO9660 and :ref:`Linux`:

  + An ISO9660 ISO can be *loop mounted*::

        mount -o loop,ro -t iso9660 ./path/to/file.iso /mnt/cdrom

  + An ISO8660 CD can be *mounted*::

        mount -o ro -t iso9660 /dev/cdrom /mnt/cdrom

* Most CD/DVD burning utilities support ISO9660 ``.iso``
  files.
* ISO9660 is useful in that it specifies how to encode
  the boot sector (*El Torito*) and partition layout.
* Nowadays, ISO9660 ``.iso`` files are often
  converted to raw drive images and written to
  bootable :ref:`USB` Mass Storage devices
  (e.g. to write a install / recovery disq
  for :ref:`Debian`, :ref:`Ubuntu`, :ref:`Fedora`, :ref:`Windows`)


.. index:: HFS+
.. _hfs+:

HFS+
`````````
| Wikipedia: https://en.wikipedia.org/wiki/HFS_Plus

HFS+ (*Hierarchical Filesystem*) or *Mac OS Extended*,
is the filesystem for Mac OS 8.1+ and :ref:`OSX`.

* HFS+ is required for :ref:`OSX` and Time Machine.

  http://www.cnet.com/how-to/the-best-ways-to-format-an-external-drive-for-windows-and-mac/

* :ref:`Windows` machines can access HFS+ partitions with:
  HFSExplorer (free, :ref:`Java`), Paragon HFS+ for Windows,
  or MacDrive

  http://www.makeuseof.com/tag/4-ways-read-mac-formatted-drive-windows/

* :ref:`Linux` machines can access HFS+ partitions with
  ``hfsprogs`` (``apt-get install hfsprogs``, ``yum install hfsprogs``).


.. index:: NTFS
.. _ntfs:

NTFS
```````
| Wikipedia: https://en.wikipedia.org/wiki/NTFS

NTFS is a proprietary journaling filesytem.

* :ref:`Windows` machines since Windows NT 3.1 and Windows XP
  default to NTFS filesystems.
* Non-Windows machines can access NTFS partitions through
  NTFS-3G: https://en.wikipedia.org/wiki/NTFS-3G


.. index:: FUSE
.. _fuse:

FUSE
`````
| Wikipedia: https://en.wikipedia.org/wiki/Filesystem_in_Userspace
| Homepage: http://fuse.sourceforge.net/
| Download: http://sourceforge.net/projects/fuse/files/fuse-2.X/
| Source: git http://git.code.sf.net/p/fuse/fuse
| Docs: http://fuse.sourceforge.net/doxygen/index.html
| Docs: http://sourceforge.net/p/fuse/wiki/FileSystems/
| Docs: http://sourceforge.net/p/fuse/wiki/LanguageBindings/
| Docs: http://sourceforge.net/p/fuse/wiki/OperatingSystems/

FUSE (*Filesystem in Userspace*) is a userspace filesystem API
for implementing filesystems in userspace.

* FUSE support is included in the :ref:`Linux` kernel since 2.6.14.
* FUSE is available for most :ref:`POSIX` platforms.

Interesting FUSE implementations:

* PyFilesystem is a :ref:`Python` :term:`language api`
  interface which supports `FUSE`:
  http://docs.pyfilesystem.org/en/latest/
* There are FUSE bindings for :ref:`Hadoop` :ref:`HDFS`.
* :ref:`Ceph` can be mounted with/over/through `FUSE`.
* :ref:`GlusterFS` can be mounted with/over/through `FUSE`.
* :ref:`NTFS`-3G mounts volumes with `FUSE`.
* virtualbox-fuse supports mounting of :ref:`virtualbox` VDI images with FUSE.
* :ref:`SSHFS`, GitFS, GmailFS, GdriveFS, WikipediaFS and :ref:`Gnome` GVFS
  are all FUSE filesystems.


.. index:: SSHFS
.. _sshfs:

SSHFS
~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/SSHFS
| Homepage: http://fuse.sourceforge.net/sshfs.html
| Download: http://sourceforge.net/projects/fuse/files/sshfs-fuse/
| Source: git http://git.code.sf.net/p/fuse/sshfs
| Docs: https://wiki.archlinux.org/index.php/Sshfs
| Docs: https://help.ubuntu.com/community/SSHFS
| Docs: https://github.com/osxfuse/osxfuse/wiki/SSHFS

SSHFS is a :ref:`FUSE` filesystem for mounting remote directories over SSH.



.. index:: Network Filesystems
.. index:: Network File Systems
.. _network filesystems:

Network Filesystems
+++++++++++++++++++++
| Wikipedia: `<https://en.wikipedia.org/wiki/Network_filesystem>`__


.. index:: Ceph
.. _ceph:

Ceph
`````
| Wikipedia: `<https://en.wikipedia.org/wiki/Ceph_(software)>`__
| Homepage: http://ceph.com/
| Download: http://ceph.com/resources/downloads/
| Source: git https://github.com/ceph/ceph
| Docs: http://ceph.com/docs/master/
| Docs: http://ceph.com/docs/master/rados/
| Docs: http://ceph.com/docs/master/radosgw/
| Docs: http://ceph.com/docs/master/radosgw/s3/
| Docs: http://ceph.com/docs/master/radosgw/swift/
| Docs: http://ceph.com/docs/master/radosgw/keystone/
| Docs: http://ceph.com/docs/master/rbd/rbd-openstack/

Ceph is an :ref:`open source` network filesystem
(a :ref:`distributed database <distributed databases>`
for files with attributes like owner, group, permissions)
written in :ref:`C++` and :ref:`Perl`
which runs over top of one or more on-disk filesystems.

* Ceph Block Device (*rbd*) -- striping, caching, snapshots, copy-on-write,
  :ref:`kvm`, :ref:`libvirt`, :ref:`OpenStack` Cinder block storage
* Ceph Filesystem (*cephfs*) -- :ref:`POSIX`
  :ref:`filesystem <filesystems>` with
  :ref:`FUSE`, :ref:`NFS`, :ref:`CIFS`, and :ref:`HDFS` APIs
* Ceph Object Gateway (*radosgw*) -- :term:`RESTful API`,
  :ref:`AWS` S3 API, :ref:`OpenStack` Swift API,
  :ref:`OpenStack` Keystone authentication


.. index:: CIFS
.. _cifs:

CIFS
``````
CIFS (*Common Internet File System*) is a centralized network filesystem
protocol.

* Samba ``smbd`` is one implementation of a :ref:`CIFS` network file server.


.. index:: DDFS
.. _ddfs:

DDFS
``````
|

DDFS (*Disco Distributed File System*) is a
distributed network filesystem
written in :ref:`Python` and :ref:`C`.

* DDFS is like a :ref:`python` implementation of :ref:`HDFS`
  (which is written in :ref:`Java`).



.. index:: GlusterFS
.. _glusterfs:

GlusterFS
```````````
| Wikipedia: https://en.wikipedia.org/wiki/GlusterFS
| Homepage: http://www.gluster.org/
| Project: https://forge.gluster.org/glusterfs-core
| Source: git https://git.forge.gluster.org/glusterfs-core/glusterfs.git
| Docs: https://gluster.readthedocs.org/en/latest/
| Docs: https://gluster.readthedocs.org/en/latest/Quick-Start-Guide/Quickstart/
| Docs: https://gluster.readthedocs.org/en/latest/Install-Guide/Setup_virt/
| Docs: https://gluster.readthedocs.org/en/latest/Install-Guide/Setup_Bare_metal/
| Docs: https://gluster.readthedocs.org/en/latest/Install-Guide/Setup_aws/
| Docs: https://gluster.readthedocs.org/en/latest/Administrator%20Guide/GlusterFS%20Cinder/
| Tcp ports: 111, 24007, 24008, 24009, 24010, 24011, 38465:38469

GlusterFS is an :ref:`open source` network filesystem
(a :ref:`distributed database <distributed databases>`
for files with attributes like owner, group, permissions)
which runs over top of one or more on-disk filesystems.

* GlusterFS can serve volumes for :ref:`OpenStack` Cinder block storage


.. index:: Hadoop distributed filesystem
.. index:: HDFS
.. _hdfs:

HDFS
``````````
| Wikipedia: https://en.wikipedia.org/wiki/Apache_Hadoop#HDFS

HDFS (*Hadoop Distributed File System*) is
an :ref:`open source`
distributed network filesystem.

* HDFS runs code next to data;
  rather than streaming data through code across the network.
* HDFS is especially suitable for :ref:`MapReduce`-style
  distributed computation.
* Apache `Hadoop` works with files stored over HDFS, FTP, :ref:`S3`,
  WASB (Azure)
* There are HDFS :term:`language apis <language api>` for
  many languages:
  :ref:`Java`, :ref:`Scala`, :ref:`Go`, :ref:`Python`,
  :ref:`Ruby`, :ref:`Perl`, :ref:`Haskell`, :ref:`C++`
* :ref:`Mesos` can manage distributed HDFS grids.
* :ref:`ElasticSearch`
* It's possible to configure a `Jenkins` :ref:`continuous integration` cluster
  as :ref:`Hadoop` cluster.
* Many databases support storage over HDFS
  (:ref:`HBase`, :ref:`Cassandra`, :ref:`Accumulo`, :ref:`Spark`)
* :ref:`Ceph` can now serve files over :ref:`HDFS`.
* HDFS can be mounted as a :ref:`FUSE` filesystem (e.g. with :ref:`Linux`).
* HDFS can be accessed from the commandline with the
  Hadoop *FS shell*:
  https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html
* HDFS can be browsed with hdfs-du:
  https://github.com/twitter/hdfs-du



.. index:: NFS
.. _nfs:

NFS
``````
| Wikipedia: https://en.wikipedia.org/wiki/NFS

NFS (*Network File System* #TODO) is an :ref:`open source`
centralized network filesystem.


.. index:: S3
.. _s3:

S3
``````````````

* :ref:`AWS` S3
* :ref:`OpenStack` Swift
* :ref:`Ceph`
* :ref:`GlusterFS`


.. index:: Swift
.. _swift:

Swift
```````

* :ref:`OpenStack` Swift
* :ref:`Ceph`
* :ref:`GlusterFS`


.. index:: SMB
.. _smb:

SMB
```````
| Wikipedia: https://en.wikipedia.org/wiki/Server_Message_Block

SMB (*Server Message Block*) is a centralized network filesystem.

* SMB has been superseded by :ref:`CIFS`.


.. index:: WebDAV
.. _webdav:

WebDAV
````````
| Wikipedia: https://en.wikipedia.org/wiki/WebDAV
| Standard: https://tools.ietf.org/html/rfc2518
| Standard: https://tools.ietf.org/html/rfc4918

WebDAV (*Web Distributed Authoring and Versioning*)
is a network filesystem protocol built with :ref:`HTTP`.

* WebDAV specifies a number of unique :ref:`HTTP` methods:

  * ``PROPFIND`` (``ls``, ``stat``, ``getfacl``),
  * ``PROPPATCH`` (``touch``, ``setfacl``)
  * ``MKCOL`` (``mkdir``)
  * ``COPY`` (``cp``)
  * ``MOVE`` (``mv``)
  * ``LOCK`` (:ref:`file locking`)
  * ``UNLOCK`` ()



.. index:: Databases
.. _databases:

Databases
+++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Database

* https://en.wikipedia.org/wiki/Database_schema

* https://en.wikipedia.org/wiki/Create,_read,_update_and_delete

* https://en.wikipedia.org/wiki/CRUD

* https://en.wikipedia.org/wiki/ACID

* https://en.wikipedia.org/wiki/Query_plan

* https://en.wikipedia.org/wiki/Database_index

* :ref:`search engine indexing`

* https://en.wikipedia.org/wiki/Category:Database_software_comparisons

  * http://db-engines.com/en/ranking


.. index:: ORM
.. index:: Object Relational Mapping
.. _orm:

Object Relational Mapping
```````````````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Object-relational_mapping

* https://en.wikipedia.org/wiki/Data_mapper_pattern
* https://en.wikipedia.org/wiki/Active_record_pattern

https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch

* https://en.wikipedia.org/wiki/List_of_object-relational_mapping_software


.. index:: Relational Databases
.. index:: SQL Databases
.. _relational databases:

Relational Databases
`````````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Relational_database

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
* :ref:`mysql`
* :ref:`postgresql`
* :ref:`sqlite`
* :ref:`Virtuoso`
* http://db-engines.com/en/ranking/relational+dbms

What doesn't SQL do?

* :ref:`RDF`, :ref:`OWL`
* https://en.wikipedia.org/wiki/OLAP


.. index:: SQL
.. _sql:

SQL
~~~~
| Wikipedia: https://en.wikipedia.org/wiki/SQL

* `<https://en.wikipedia.org/wiki/Null_(SQL)#Comparisons_with_NULL_and_the_three-valued_logic_.283VL.29>`_
* `<https://en.wikipedia.org/wiki/Join_(SQL)>`_
* https://en.wikipedia.org/wiki/SQL_injection
* http://cwe.mitre.org/top25/#CWE-89 (#1 Most Prevalent Dangerous
  Security Error (2011))

See: :ref:`Object Relational Modeling <orm>`


.. index:: Drizzle
.. _drizzle:

Drizzle
~~~~~~~~~
| Wikipedia: `<https://en.wikipedia.org/wiki/Drizzle_(database_server)>`__
| Homepage: http://www.drizzle.org/
| Project: https://launchpad.net/drizzle
| Download: http://www.drizzle.org/content/download
| Source: bzr lp:drizzle
| Docs: http://www.drizzle.org/content/documentation
| Docs: http://docs.drizzle.org/

Drizzle is an :ref:`open source` relational database "for the cloud"
which was forked from :ref:`MySQL` 6.0.

* Drizzle stores all data as UTF-8.
* Drizzle has a minimal core and a plugin API.


.. index:: MySQL
.. _mysql:

MySQL
~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/MySQL
| Homepage: https://www.mysql.com/
| Download: https://dev.mysql.com/downloads/mysql/
| Source: git https://github.com/mysql/mysql-server
| Doc: https://dev.mysql.com/doc/

MySQL Community Edition is an :ref:`open source` relational database.


.. index:: PostgreSQL
.. _postgresql:

PostgreSQL
~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/PostgreSQL
| Homepage: http://www.postgresql.org/
| Download: http://www.postgresql.org/download/
| Source: git http://git.postgresql.org/git/postgresql.git
| Docs: http://www.postgresql.org/docs/
| Docs: http://www.postgresql.org/docs/9.4/static/index.html
| Docs: http://www.postgresql.org/docs/9.4/static/sql.html

PostgreSQL is an :ref:`open source` relational database.

* PostgreSQL has native support for storing and querying :ref:`JSON`.
* PostgreSQL has support for geographical queries (*PostGIS*).


.. index:: SQLite
.. _sqlite:

SQLite
~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/SQLite
| Homepage: https://www.sqlite.org/
| Download: https://www.sqlite.org/download.html
| Source:
| Docs: https://www.sqlite.org/docs.html
| Docs: https://www.sqlite.org/different.html
| Docs: https://www.sqlite.org/threadsafe.html
| Docs: https://www.sqlite.org/uri.html
| FileExt: ``.sqlite``

SQLite is a serverless :ref:`open source` relational database
which stores all data in one file.

* SQLite is included in the :ref:`Python` standard library.


.. index:: Virtuoso Universal Server
.. index:: Virtuoso
.. _virtuoso:

Virtuoso
~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Virtuoso_Universal_Server
| Homepage: http://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/
| Source: git https://github.com/openlink/virtuoso-opensource
| Docs: http://docs.openlinksw.com/virtuoso/
| Docs: http://docs.openlinksw.com/virtuoso/sqlreference.html
| Docs: http://docs.openlinksw.com/virtuoso/rdfandsparql.html
| Docs: http://docs.openlinksw.com/virtuoso/rdfsparql.html
| Docs: http://docs.openlinksw.com/virtuoso/rdfsparqlrule.html
| Docs: http://docs.openlinksw.com/virtuoso/rdfgraphsecurity.html
| Docs: http://docs.openlinksw.com/virtuoso/virtuososponger.html

Virtuoso :ref:`open source` edition is a multi-paradigm
:ref:`relational database <relational databases>` /
:ref:`XML` document database /
:ref:`RDF triplestore <triplestores>`.

    * Relational Tables Data Management
      (Columnar or Column-Store :ref:`SQL` RDBMS)
    * Relational Property Graphs Data Management
      (:ref:`SPARQL` :ref:`RDF` based Quad Store)
    * Content Management
      (:ref:`HTML`, TEXT, :ref:`TURTLE`, :ref:`RDF/XML`, :ref:`JSON`,
      :ref:`JSON-LD`, :ref:`XML`)
    * Web and other Document File Services (Web Document or File Server)
    * :ref:`Five-Star Linked Open Data <fivestardata>` Deployment
      (:ref:`RDF`-based :ref:`Linked Data` Server)
    * Web Application Server (SOAP or :term:`RESTful <restful api>`
      interaction modes).

* Virtuoso supports ODBC, JDBC, and DB-API relational database access.
* Virtuoso powers :ref:`DBpedia`.


.. index:: NoSQL
.. index:: NoSQL Databases
.. _nosql:

NoSQL Databases
`````````````````
| Wikipedia: https://en.wikipedia.org/wiki/NoSQL

`<https://en.wikipedia.org/wiki/Keyspace_(distributed_data_store)>`_

`<https://en.wikipedia.org/wiki/Column_(data_store)>`_

* `<https://en.wikipedia.org/wiki/Column_family>`_
* `<https://en.wikipedia.org/wiki/Super_column>`_
* https://en.wikipedia.org/wiki/Apache_Accumulo


.. index:: Graph Databases
.. _graph databases:

Graph Databases
``````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Graph_database

https://en.wikipedia.org/wiki/Graph_database#Graph_database_projects

* https://en.wikipedia.org/wiki/AllegroGraph [:ref:`RDF`]
* :ref:`Blazegraph`  [:ref:`RDF`, :ref:`OWL`]
* :ref:`neo4j`
* :ref:`Accumulo` + https://en.wikipedia.org/wiki/Sqrrl
* :ref:`Virtuoso` [:ref:`RDF`, :ref:`OWL`]
* http://db-engines.com/en/ranking/graph+dbms

Graph Queries

* https://en.wikipedia.org/wiki/Graph_database#APIs_and_Graph_Query.2FProgramming_Languages
* :ref:`SPARQL`
* :ref:`Gremlin`
* :ref:`Blueprints`
* :ref:`Spark` GraphX


.. index:: Blazegraph
.. _blazegraph:

Blazegraph
~~~~~~~~~~~~
| Homepage: http://www.blazegraph.com/
| Download: http://www.blazegraph.com/download
| Src: git git://git.code.sf.net/p/bigdata/git
| Docs: http://www.blazegraph.com/learn
| Docs: http://www.blazegraph.com/inference
| Docs: http://www.blazegraph.com/blueprints
| Docs: http://www.blazegraph.com/sesame
| Docs: http://www.blazegraph.com/develop
| Docs: http://www.blazegraph.com/docs/api/
| Docs: https://wiki.blazegraph.com/wiki/index.php/Main_Page

Blazegraph is an :ref:`open source` :ref:`graph database <graph databases>`
written in :ref:`Java`
with support for :ref:`Gremlin`, :ref:`Blueprints`, :ref:`RDF`,
:ref:`RDFS` and :ref:`OWL` inferencing,
:ref:`SPARQL`.

* Blazegraph was formerly known as *Bigdata*.
* Blazegraph 1.5.2 supports :ref:`Solr` (e.g. TF-IDF) indexing.

* Blazegraph will power the :ref:`Wikidata` Query Service (RDF, SPARQL):

  https://lists.wikimedia.org/pipermail/wikidata-tech/2015-March/000740.html

* MapGraph is a set of :ref:`GPU`-accelerations for graph processing.


.. index:: Blueprints
.. _blueprints:

Blueprints
~~~~~~~~~~~
| Wikipedia:
| Homepage:
| Src: git https://github.com/tinkerpop/blueprints
| Docs: https://github.com/tinkerpop/blueprints/wiki

Blueprints is an :ref:`open source`
:ref:`graph database <graph databases>` API
(and reference graph data model).

    Blueprints is a collection of interfaces, implementations,
    ouplementations, and test suites for the property graph data model.

    Blueprints is analogous to the JDBC, but for graph databases.
    As such, it provides a common set of interfaces to allow developers to
    plug-and-play their graph database backend.

    Moreover, software written atop Blueprints works over all
    Blueprints-enabled graph databases.

    Within the TinkerPop software stack, Blueprints serves
    as the foundational technology for:

    * Pipes: A lazy, data flow framework
    * :ref:`Gremlin`: A graph traversal language
    * Frames: An object-to-graph mapper
    * Furnace: A graph algorithms package
    * Rexster: A graph server

* There are many blueprints API implementations
  (e.g. Rexster, :ref:`neo4j`, :ref:`Blazegraph`, :ref:`Accumulo`)


.. index:: Gremlin
.. _gremlin:

Gremlin
~~~~~~~~
| Wikipedia: `<https://en.wikipedia.org/wiki/Gremlin_(programming_language)>`__
| Src: git https://github.com/tinkerpop/gremlin
| Docs: https://github.com/tinkerpop/gremlin/wiki

Gremlin is an :ref:`open source` domain-specific language
for traversing property graphs.

* Gremlin works with databases that implement the :ref:`blueprints`
  graph database API.


.. index:: Neo4j
.. _neo4j:

Neo4j
~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Neo4j
| Homepage: http://neo4j.com/
| Download: http://neo4j.com/download/
| Src: git https://github.com/neo4j/neo4j
| Docs: http://neo4j.com/developer/get-started/
| Docs: http://neo4j.com/docs/
| Docs: http://neo4j.com/docs/2.2.3/
| Docs: http://neo4j.com/developer/cypher/
| Docs: http://neo4j.com/docs/stable/cypher-refcard/
| Docs: https://en.wikipedia.org/wiki/Cypher_Query_Language
| Docs: http://neo4j.com/open-source-project/

Neo4j is an :ref:`Open Source` HA graph database
written in :ref:`Java`.

* Neo4j implements the :ref:`Paxos` distributed algorithm
  for HA (*high availability*).
* Neo4j can integrate with :ref:`Spark` and :ref:`ElasticSearch`.
* Neo4j is widely deployed in production environments.
* There is a :ref:`blueprints` API implementation for Neo4j:

  https://github.com/tinkerpop/blueprints/wiki/Neo4j-Implementation


.. index:: RDF Triplestores
.. index:: RDF Databases
.. index:: Triplestores
.. _triplestores:

RDF Triplestores
`````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Triplestore

https://en.wikipedia.org/wiki/List_of_subject-predicate-object_databases

* :ref:`Blazegraph`
* `<https://en.wikipedia.org/wiki/Jena_(framework)>`__
* `<https://en.wikipedia.org/wiki/Sesame_(framework)>`__
* :ref:`Virtuoso`
* http://db-engines.com/en/ranking/rdf+store

Graph Pattern Query Results

* :ref:`SPARQL`
* https://en.wikipedia.org/wiki/Redland_RDF_Application_Framework

  * http://librdf.org/notes/contexts.html

* `<https://en.wikipedia.org/wiki/Jena_(framework)>`__
* SAIL (Storage and Inferencing Layer) API
* https://en.wikipedia.org/wiki/CubicWeb
* :ref:`RDFLib`

``rdfs:seeAlso``

* :ref:`Linked Data`
* :ref:`Semantic Web`
* :ref:`semantic Web Standards`
* :ref:`Semantic Web Tools`


.. index:: Distributed Databases
.. _distributed databases:

Distributed Databases
````````````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Distributed_database
| Wikipedia: https://en.wikipedia.org/wiki/Distributed_data_store

See: :ref:`distributed algorithms`


.. index:: Accumulo
.. _accumulo:

Accumulo
~~~~~~~~~~
| Wikipedia:
| Homepage: https://accumulo.apache.org/
| Download: https://accumulo.apache.org/downloads/
| Source: git https://github.com/apache/accumulo
| Docs: https://accumulo.apache.org/1.7/accumulo_user_manual.html
| Docs: https://accumulo.apache.org/1.7/accumulo_user_manual.html#_accumulo_design
| Twitter: https://twitter.com/apacheaccumulo

Apache Accumulo is an :ref:`open source` distributed database
key/value store written in :ref:`Java`
based on :ref:`BigTable`
which adds realtime queries, streaming iterators,
row-level ACLs
and a number of additional features.

* Accumulo supports :ref:`MapReduce`-style computation.
* Accumulo supports streaming iterator computation.
* Accumulo supports :ref:`HDFS`.
* Accumulo implements a programmatic :ref:`Java` query API.


.. index:: BigTable
.. _bigtable:

BigTable
~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/BigTable
| Docs: http://research.google.com/archive/bigtable.html

Google BigTable is a open reference design for a distributed key/value
column store
and a proprietary production database system.

* BigTable functionality overlaps with that of the newer Pregel and Spanner
  distributed databases.
* Cloud BigTable is a :ref:`PaaS` / :ref:`SaaS` service
  with :ref:`Java` integration through an adaptation of
  :ref:`HBase` API.


.. index:: Cassandra
.. _cassandra:

Cassandra
~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Apache_Cassandra
| Homepage: https://cassandra.apache.org/
| Download: https://cassandra.apache.org/download/
| Source: git https://github.com/apache/cassandra
| Docs: https://wiki.apache.org/cassandra/FrontPage
| Docs: https://wiki.apache.org/cassandra/GettingStarted
| Docs: http://docs.datastax.com/en/latest-dsc/
| Docs: http://docs.datastax.com/en/cassandra/2.1/cassandra/architecture/architectureIntro_c.html

Apache Cassandra is an :ref:`open source` distributed key/value
super column store written in :ref:`Java`.

* Cassandra is similar to :ref:`AWS` Dynamo and :ref:`BigTable`.
* Cassandra supports :ref:`MapReduce`-style computation.
* Cassandra supports :ref:`HDFS`.
* Facebook is one primary supporter of :ref:`Cassandra` development.


.. index:: Hadoop
.. _hadoop:

Hadoop
~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Apache_Hadoop
| Homepage: https://hadoop.apache.org/
| Download: https://hadoop.apache.org/releases.html
| Source: git git://git.apache.org/hadoop.git
| Source: git https://github.com/apache/hadoop
| Docs: http://hadoop.apache.org/docs/current/
| Docs: http://hadoop.apache.org/docs/stable/

Apache Hadoop is a collection of :ref:`open source`
distributed computing components;
particularly for :ref:`MapReduce`-style computation
over Hadoop :ref:`HDFS` distributed filesystem.


.. index:: HBase
.. _hbase:

HBase
~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Apache_HBase
| Homepage: https://hbase.apache.org/
| Download: https://www.apache.org/dyn/closer.cgi/hbase/
| Source: git git://git.apache.org/hbase.git
| Source: git https://github.com/apache/hbase
| Docs: https://hbase.apache.org/book.html
| Docs: https://hbase.apache.org/book.html#conceptual.view

Apache HBase is an :ref:`open source` distributed key/value
super column store
based on :ref:`BigTable`
written in :ref:`Java`
that does :ref:`MapReduce`-style computation over Hadoop :ref:`HDFS`.

* HBase has a :ref:`Java` API, a :term:`RESTful API`, an `avro` API,
  and a :ref:`Thrift` API


.. index:: Apache Hive
.. index:: Hive
.. _hive:

Hive
~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Apache_Hive
| Homepage: https://hive.apache.org/
| Download: https://hive.apache.org/downloads.html
| Docs: https://cwiki.apache.org/confluence/display/Hive/LanguageManual
| Docs: https://hive.apache.org/javadocs/r1.2.1/api/index.html
| Docs: https://cwiki.apache.org/confluence/display/Hive/Home

Apache Hive is an :ref:`open source` data warehousing platform
written in :ref:`java`.

* Hive can read data from :ref:`HDFS` and :ref:`S3`.
* :ref:`Hive` supports :ref:`Avro`, Parqet.
* HiveQL is a :ref:`SQL`-like language.


.. index:: Apache Parquet
.. index:: Parquet
.. _parquet:

Parquet
~~~~~~~~
| Homepage: https://parquet.apache.org/
| Download: https://parquet.apache.org/downloads/
| Source: git git://git.apache.org/incubator-parquet-mr.git
| Source: git https://github.com/apache/parquet-mr
| Standard: https://github.com/apache/parquet-format
| Docs: https://parquet.apache.org/documentation/latest/

Apache Parqet is an :ref:`open source` columnar storage format
for :ref:`distributed databases`

    Apache Parquet is a columnar storage format available to any project
    in the :ref:`Hadoop` ecosystem,
    regardless of the choice of data processing framework,
    data model or programming language.

* The *Parquet format* and *Parquet metadata* are encoded with :ref:`Thrift`:
* See also: :ref:`CSV`, :ref:`CSVW`


.. index:: Presto
.. _presto:

Presto
~~~~~~~~
| Homepage: https://prestodb.io/
| Source: git https://github.com/facebook/presto
| Docs: https://prestodb.io/docs/current/

Presto is an :ref:`open source` distributed query engine
designed to query multiple datastores at once.

* Presto has connectors for :ref:`Cassandra`, :ref:`Hive`, JMX,
  Kafka, :ref:`MySQL`, and :ref:`PostgreSQL`.
* Presto does not yet support :ref:`SPARQL`.
* Presto does not yet support :ref:`SPARQL` federated query.


.. index:: Apache Spark
.. index:: Spark
.. _spark:

Spark
~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Apache_Spark
| Homepage: https://spark.apache.org/
| Download: https://spark.apache.org/downloads.html
| Source: git git://git.apache.org/spark.git
| Source: git https://github.com/apache/spark
| Docs: https://spark.apache.org/documentation.html
| Docs: https://spark.apache.org/docs/latest/
| Docs: https://spark.apache.org/docs/latest/cluster-overview.html
| Docs: https://spark.apache.org/docs/latest/quick-start.html

Apache Spark is an :ref:`open source` distributed
computation platform.

* Spark is in-memory; and 100x faster than :ref:`MapReduce`.
* Spark can work with data in/over/through
  :ref:`HDFS`, :ref:`Cassandra`, :ref:`OpenStack` :ref:`Swift`,
  :ref:`AWS` :ref:`S3`, and the local filesystem.
* Spark can be provisioned by YARN or :ref:`Mesos`.
* Spark has :ref:`Java`, :ref:`Scala`, :ref:`Python`, and `R`
  :term:`language APIs <language api>`.
* Spark set a world sorting benchmark record in 2014:
  https://spark.apache.org/news/spark-wins-daytona-gray-sort-100tb-benchmark.html


.. index:: GraphX
.. _graphx:

=========
GraphX
=========
| Wikipedia: https://en.wikipedia.org/wiki/Apache_Spark#GraphX
| Homepage: https://spark.apache.org/graphx/
| Docs: https://spark.apache.org/docs/latest/graphx-programming-guide.html

GraphX is an :ref:`open source` graph query framework built with :ref:`Spark`.


.. index:: Distributed Algorithms
.. _distributed algorithms:

Distributed Algorithms
++++++++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Distributed_algorithm
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Distributed_algorithms

:ref:`Distributed Databases` and distributed :ref:`information systems`
implement :ref:`Distributed Algorithms` designed to solve for
:ref:`confidentiality`, :ref:`integrity`, and :ref:`availability`.

As separate records / statements to be ``yield``-ed or emitted:

* :ref:`Distributed Databases`
    implement :ref:`Distributed Algorithms`.
* Distributed :ref:`information systems`
    implement :ref:`Distributed Algorithms`.

See Also:

* https://en.wikipedia.org/wiki/Parallel_computing
* https://en.wikipedia.org/wiki/Supercomputer#Distributed_supercomputing
*


.. index:: Distributed Computing Problems
.. _distributed computing problems:

Distributed Computing Problems
````````````````````````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Distributed_computing
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Distributed_computing_problems

* `<https://en.wikipedia.org/wiki/Consensus_(computer_science)>`_
* https://en.wikipedia.org/wiki/Leader_election
* https://en.wikipedia.org/wiki/Distributed_concurrency_control
* https://en.wikipedia.org/wiki/Distributed_lock_manager
*


.. index:: Non-blocking algorithm
.. _non-blocking algorithm:

Non-blocking algorithm
```````````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Non-blocking_algorithm

* `<https://en.wikipedia.org/wiki/Lock_(computer_science)#Disadvantages>`__
* See: :ref:`file locking`


.. index:: Distributed Hash Table
.. index:: DHT
.. _dht:

DHT
```
| Wikipedia: https://en.wikipedia.org/wiki/Distributed_hash_table

A DHT (Distributed Hash Table*) is a distributed key value store
for storing values under a consistent file checksum hash which can be
looked up with e.g. an exact string match.

* At an API level, a DHT is a key/value store.
* :term:`DNS` is basically a DHT
* :ref:`distributed databases` all implement some form of
  a structure simiar to a DHT (a replicated *keystore*);
  often for things like bloom filters (for fast search)

  * :ref:`Cassandra`, :ref:`Ceph`, :ref:`GlusterFS`

* :ref:`browsers` that maintain a local cache could
  implement a DHT (e.g. with :ref:`websockets` or :ref:`webrtc`)

  * :ref:`webtorrent` (:ref:`Javascript`, :ref:`Node.js`, :ref:`WebRTC`)

* :ref:`BitTorrent` :term:`magnet URIs <magnet uri>` (:term:`URNs <urn>`)
  contain a *key*,
  which is a *checksum* of a manifest,
  which can be retrieved from a :ref:`DHT`::

    # <a href="magnet:?xt=urn:btih:IJBDPDSBT4QZLBIJ6NX7LITSZHZQ7F5I">.</a>
    # key_uri = "IJBDPDSBT4QZLBIJ6NX7LITSZHZQ7F5I"
    dht = DHT(); value = dht.get(key_uri)

* :ref:`named data networking` is also essentially a cached :ref:`DHT`.


.. index:: MapReduce
.. _mapreduce:

MapReduce
````````````
| Wikipedia:  https://en.wikipedia.org/wiki/MapReduce

MapReduce is a :ref:`distributed algorithm <distributed algorithms>`
for distributed computation.

* :ref:`BigTable`, :ref:`Hadoop`, :ref:`HDFS`,
  `Disco`, :ref:`DDFS` all support
  :ref:`mapreduce`-style computation.
* See also: bashreduce


.. index:: Paxos
.. _paxos:

Paxos
```````
| Wikipedia: `<https://en.wikipedia.org/wiki/Paxos_(computer_science)>`__
| Docs: `<https://en.wikipedia.org/wiki/Paxos_(computer_science)#Production_use_of_Paxos>`__

* https://en.wikipedia.org/wiki/Paxos_(computer_science)#Production_use_of_Paxos

  * :ref:`BigTable`, Spanner, Megastore
  * :ref:`Ceph`
  * neo4j


.. index:: BSP
.. index:: Bulk Synchronous Parallel
.. _bsp:

Bulk Synchronous Parallel
````````````````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Bulk_synchronous_parallel

Bulk Synchronous Parallel (*BSP*) is a
:ref:`distributed algorithm <distributed algorithms>`
for distributed computation.

* Google Pregel, Apache Giraph, and Apache :ref:`Spark` are built for
  a :ref:`bsp` model
* :ref:`mapreduce` can be expressed very concisely in terms of
  BSP.



.. index:: Distributed Computing Protocols
.. _distributed computing protocols:

Distributed Computing Protocols
+++++++++++++++++++++++++++++++++

* :ref:`CORBA`
* :ref:`Message Passing`
* :ref:`MPI`
* https://en.wikipedia.org/wiki/XML-RPC
* https://en.wikipedia.org/wiki/Java_Remote_Method_Invocation
* :ref:`ws-`
* :term:`RESTful HTTP <restful api>`
* :ref:`Protocol Buffers`
* :ref:`Thrift`
* :ref:`Avro`
* :ref:`msgpack`
* :ref:`WebSocket <websockets>`
* :ref:`WebRTC`
* :ref:`JSON-WSP`
* :ref:`LDP` (:ref:`Turtle` or :ref:`JSON-LD` :ref:`RDF` over :ref:`HTTP`)
* https://en.wikipedia.org/wiki/List_of_web_service_protocols


.. index:: CORBA
.. _corba:

CORBA
``````
| Wikipedia: https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture

CORBA (*Common Object Request Broker Architecture*) is
a :ref:`distributed computing protocol <distributed computing protocols>`
now defined by :ref:`OMG`
with implementations in many languages.

* CORBA is a distributed object-oriented protocol
  for platform-neutral distributed computing.
* CORBA objects are marshalled and serialized
  according to an IDL
  (*Interface Definition Language*)
  with a limited set of datatypes (see also :ref:`XSD`,
  :ref:`Distributed Computing Protocols`:
  :ref:`Protocol Buffers`, :ref:`Thrift`,
  :ref:`Avro`, :ref:`msgpack`, :ref:`JSON-LD`)
* CORBA ORBs (*Object Request Brokers*)
  route requests for objects (see also :ref:`ESB`)
* CORBA objects are either in
  local address space (see also ``file://`` / ``/dev/mem``)
  or remote address space
  (see also dereferencable :ref:`HTTP`, :ref:`HTTPS`
  :term:`URLs <url>` )
* CORBA objects can be looked up by reference
  (by :term:`URL`, or *NameService* (see also :term:`DNS`))
* "CORBA Objects are passed by reference, while data
  (integers, doubles, structs, enums, etc.) are passed by value"
  -- https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture#Features




.. index:: Message Passing
.. _message passing:

Message Passing
`````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Message_passing
| https://en.wikipedia.org/wiki/Messaging_pattern
| https://en.wikipedia.org/wiki/Message_passing_in_computer_clusters
| https://en.wikipedia.org/wiki/Active_message

* https://en.wikipedia.org/wiki/Message_passing#Synchronous_versus_asynchronous_message_passing

* https://en.wikipedia.org/wiki/Dataflow_programming

  * https://en.wikipedia.org/wiki/Flow-based_programming
  * https://en.wikipedia.org/wiki/Spreadsheet
  * https://en.wikipedia.org/wiki/Reactive_programming

* https://en.wikipedia.org/wiki/Actor_model_implementation
* https://en.wikipedia.org/wiki/Factor_graph#Message_passing_on_factor_graphs
* :ref:`BSP`


.. index:: ESB
.. index:: Enterprise Service Bus
.. _esb:

ESB
````
| Wikipedia: https://en.wikipedia.org/wiki/Enterprise_service_bus

An ESB (*Enterprise Service Bus*) is a centralized
distributed computing component
which relays (or *brokers*) messages
with or as a message queue (*MQ*).

* ESB is generally the name for a message queue / task worker pattern
  in the :ref:`SOA` (particularly :ref:`Java`).
* ESBs host service endpoints for message producers and consumers.
* ESBs can also maintain state, or logging.
* ESB services can often be described with e.g.
  :ref:`WSDL` and/or :ref:`JSON-WSP`.



.. index:: MPI
.. _mpi:

MPI
````
| Wikipedia: https://en.wikipedia.org/wiki/Message_Passing_Interface

MPI (*Message Passing Interface*)
is a distributed computing protocol
for structured data interchange
with implementations in many languages.

* Many supercomputing applications are built with MPI.
* MPI is faster than :ref:`JSON`.
* :ref:`IPython` supports MPI:
  https://ipython.org/ipython-doc/3/parallel/parallel_mpi.html


.. index:: Avro
.. index:: Apache Avro
.. _avro:

Avro
``````
| Wikipedia: https://en.wikipedia.org/wiki/Apache_Avro
| Homepage: https://avro.apache.org/
| Standard: https://avro.apache.org/docs/current/spec.html
| Standard: https://avro.apache.org/docs/current/trevni/spec.html
| Download: https://avro.apache.org/releases.html#Download
| Docs: https://avro.apache.org/docs/current/
| Docs: https://avro.apache.org/docs/current/gettingstartedjava.html
| Docs: https://avro.apache.org/docs/current/api/java/
| Docs: https://avro.apache.org/docs/current/gettingstartedpython.html
| Docs: https://avro.apache.org/docs/current/api/c/
| Docs: https://avro.apache.org/docs/current/api/cpp/html/
| Docs: https://avro.apache.org/docs/current/api/csharp/

Apache Avro is an RPC distributed computing protocol
with implementations in many languages.

* Avro *schemas* are defined in :ref:`JSON`.
* Avro is similar to :ref:`Protocol Buffers` and :ref:`Thrift`,
  but does not require code generation.
* Avro stores *schemas* within the data.



.. index:: Protocol Buffers
.. _protocol buffers:

Protocol Buffers
``````````````````
| Homepage: https://developers.google.com/protocol-buffers/
| Source: git https://github.com/google/protobuf
| Docs:

Protocol Buffers (*PB*) is a standard
for structured data interchange.

* Protocol Buffers are faster than :ref:`JSON`


.. index:: Thrift
.. _thrift:

Thrift
````````
Thrift is a standard
for structured data interchange
in the style of :ref:`Protocol Buffers`.

* Thrift is faster than :ref:`JSON`.


.. index:: SOA
.. _soa:

SOA
``````
| Wikipedia: https://en.wikipedia.org/wiki/Service-oriented_architecture

SOA (*Service Oriented Architecture*) is a collection
of :ref:`web standards` (e.g :ref:`ws-`) and architectural patterns
for distributed computing.


.. index:: WS- Web Services
.. _ws-:

WS-*
~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/List_of_web_service_specifications

There are many web service specifications; many
web service specifications often start with ``WS-``.

* https://en.wikipedia.org/wiki/List_of_web_service_specifications
* Many/most WS-* standards specify :ref:`XML`.
* Some WS-* standards also specify :ref:`JSON`.


.. index:: WSDL
.. _wsdl:

WSDL
~~~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Web_Services_Description_Language

WSDL (*Web Services Description Language*)
is a :ref:`web standard <web standards>`
for describing web services and the schema
of their inputs and outputs.


.. index:: JSON-WSP
.. _json-wsp:

JSON-WSP
``````````
| Wikipedia: https://en.wikipedia.org/wiki/JSON-WSP

JSON-WSP (:ref:`JSON` Web-Service Protocol)
is a :ref:`web standard <web standards>` protocol
for describing services and request and response objects.

* JSON-WSP is similar in function to :ref:`WSDL` and :ref:`CORBA` IDL.

See also: :ref:`Linked Data Platform (LDP) <ldp>`


.. index:: Data Grid
.. _data-grid:

Data Grid
++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Data_grid




.. index:: Search Engine Indexing
.. _search engine indexing:

Search Engine Indexing
+++++++++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Search_engine_indexing

* https://en.wikipedia.org/wiki/Web_search_engine
* :ref:`information retrieval`
* :ref:`semantic web` :ref:`graph <graphs>`
  of :ref:`linked data`, :
  :ref:`RDFa`, :ref:`JSON-LD`, :ref:`Schema.org`.


.. index:: ElasticSearch
.. _elasticsearch:

ElasticSearch
```````````````
| Wikipedia: https://en.wikipedia.org/wiki/Elasticsearch
| Homepage: https://www.elastic.co/products/elasticsearch
| Download: https://www.elastic.co/downloads/elasticsearch
| Source: git https://github.com/elastic/elasticsearch
| Docs: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
| Docs: https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html
| DockerHub: https://registry.hub.docker.com/u/library/elasticsearch/

ElasticSearch is an :ref:`open source` realtime search server
written in :ref:`Java`
built on Apache :ref:`Lucene`
with a :term:`RESTful API` for indexing :ref:`JSON` documents.

* ElasticSearch supports geographical (bounded) queries.
* ElasticSearch can build better indexes for faster
  search response times when
  *ElasticSearch Mappings* are specified.
* ElasticSearch mappings can be (manually) transformed
  to :ref:`JSON-LD` ``@context`` mappings:
  https://github.com/westurner/elasticsearchjsonld


.. index:: Haystack
.. _haystack:

Haystack
``````````
| Homepage: http://haystacksearch.org/
| Source: git https://github.com/django-haystack/django-haystack
| PyPI: https://pypi.python.org/pypi/django-haystack
| Docs: https://django-haystack.readthedocs.org/en/latest/

Haystack is an :ref:`open source`
:ref:`Python` Django API for a number of search
services (e.g. :ref:`solr`, :ref:`elasticsearch`, :ref:`Whoosh`,
:ref:`Xapian`).


.. index:: Apache Lucene
.. index:: Lucene
.. _lucene:

Lucene
````````
| Wikipedia: https://en.wikipedia.org/wiki/Lucene
| Homepage: https://lucene.apache.org/
| Download: https://lucene.apache.org/core/downloads.html
| Source: svn http://svn.apache.org/repos/asf/lucene/dev/trunk
| Docs: https://lucene.apache.org/core/
| Docs: https://lucene.apache.org/core/5_2_0/

Apache Lucene is an :ref:`open source` search indexing service
written in :ref:`java`.

* :ref:`ElasticSearch`, :ref:`Nutch`, and :ref:`Solr`
  are implemented on top of Lucene.


.. index:: ApacheNutch
.. index:: Nutch
.. _nutch:

Nutch
```````
| Wikipedia: https://en.wikipedia.org/wiki/Nutch
| Homepage: https://nutch.apache.org/
| Download: https://nutch.apache.org/downloads.html
| Source: git git://git.apache.org/nutch.git
| Source: git https://github.com/apache/nutch
| Docs: https://nutch.apache.org/apidocs/apidocs-2.3/index.html
| Docs: https://wiki.apache.org/nutch/
| Docs: https://wiki.apache.org/nutch/#Tutorials

Apache Nutch is an :ref:`open source`
distributed web crawler and search engine
written in :ref:`Java`
and implemented on top of :ref:`Lucene`.

* Nutch has a pluggable storage and indexing API with support
  for e.g. :ref:`Solr`, :ref:`ElasticSearch`.


.. index:: Solr
.. index:: Apache Solr
.. _solr:

Solr
```````
| Wikipedia:
| Homepage: https://lucene.apache.org/solr/
| Download: https://lucene.apache.org/solr/mirrors-solr-latest-redir.html
| Docs: https://lucene.apache.org/solr/resources.html
| Docs: https://www.apache.org/dyn/closer.cgi/lucene/solr/ref-guide/
| Docs: https://wiki.apache.org/solr/

Apache Solr is an :ref:`open source` web search platform
written in :ref:`Java`
and implemented on top of :ref:`Lucene`.


.. index:: Whoosh
.. _whoosh:

Whoosh
````````
| Homepage:
| PyPI: https://pypi.python.org/pypi/Whoosh
| Docs: https://pythonhosted.org/Whoosh/

Whoosh is an :ref:`open source` search indexing service
written in :ref:`Python`.


.. index:: Xapian
.. _xapian:

Xapian
````````
| Wikipedia: https://en.wikipedia.org/wiki/Xapian
| Homepage: http://xapian.org/
| Docs: http://xapian.org/docs/
| Docs: http://xapian.org/docs/apidoc/html/inherits.html

Xapian is an :ref:`open source` search library written in :ref:`C++`
with bindings for many languages.


.. index:: Information Retrieval
.. _information retrieval:

Information Retrieval
```````````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Information_retrieval
| Docs: http://nlp.stanford.edu/IR-book/information-retrieval.html

* Christopher D. Manning, Prabhakar Raghavan and Hinrich Schütze,
  *Introduction to Information Retrieval*, Cambridge University Press. 2008.

  http://nlp.stanford.edu/IR-book/


.. index:: Time Standards
.. _time standards:

Time Standards
-----------------


.. index:: International Atomic Time
.. _iat:

International Atomic Time (IAT)
++++++++++++++++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/International_Atomic_Time

International Atomic Time (*IAT*)
is an international standard for
extremely precise
time keeping; which is the basis
for :ref:`UTC` Earth time
and for `Terrestrial Time` (Earth and Space).


.. index:: Long Now Dates
.. _long now dates:

Long Now Dates
++++++++++++++++
| Homepage: https://en.wikipedia.org/wiki/Long_Now_Foundation
| Docs: https://en.wikipedia.org/wiki/Year_10,000_problem

::

     2015    # ISO8601 date
    02015    # 5-digit Y10K date


.. index:: Decimal Time
.. _decimal time:

Decimal Time
++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Decimal_time

* https://en.wikipedia.org/wiki/Decimal_time#Conversions
* https://en.wikipedia.org/wiki/Decimal_time#Fractional_days
* https://en.wikipedia.org/wiki/Leap_year (~365.25 days/yr)
* https://en.wikipedia.org/wiki/Leap_second (rotation time ~= atomic
  time)

.. index:: Unix Time
.. _unix time:

Unix Time
+++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Unix_time

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

See also: `Swatch Internet Time` (`Beat Time`)

.. index:: Year Zero
.. index:: 0 (Year)
.. _year zero:

Year Zero
++++++++++
| Wikipedia: `<https://en.wikipedia.org/wiki/0_(year)>`__

* The Gregorian Calendar
  (e.g. :ref:`Common Era <ce>`, `Julian Calendar`)
  does not include a `year zero`;
  (1 BCE is followed by 1 CE).
* :ref:`Astronomical year numbering` includes a `year zero`.
* :ref:`Before Present <bp>` dates do not specify a `year zero`.
  (because they are relative to the current (or *published*) date).


.. index:: Astronomical year numbering
.. _astronomical year numbering:

Astronomical year numbering
++++++++++++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Astronomical_year_numbering

* Astronomical year numbering includes a year zero:

Tools with support for :ref:`astronomical year numbering`:

* AstroPy is a :ref:`Python` library that supports astronomical year numbering:

  https://astropy.readthedocs.org/en/latest/time/



.. index:: Before Present
.. index:: BP
.. _bp:

Before Present (BP)
++++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Before_Present

Before Present (*BP*) dates are relative to the current date
(or *date of publication*); e.g. "2.6 million years ago".


.. index:: Common Era
.. _ce:

Common Era (CE)
+++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Common_Era
| Docs: https://en.wikipedia.org/wiki/Pax_Romana
| Docs: :ref:`Year Zero`

* BCE (*Before Common Era*) == BC

  * https://en.wiktionary.org/wiki/BCE
  * https://en.wiktionary.org/wiki/BC

* CE (*Common Era*) == **AD** (*Anno Domini*)

  * https://en.wiktionary.org/wiki/CE
  * https://en.wiktionary.org/wiki/AD

Common Era and :ref:`year zero`::

       5000 BCE == -5000 CE
          1 BCE ==    -1 CE
          0 BCE ==     0 CE
          0  CE ==     0 BCE
          1  CE ==     1 CE
       2015  CE ==  2015 CE

.. note:: Are these off by one?

   * :ref:`astronomical year numbering` --
     you must convert from julian/gregorian dates
     to :ref:`astronomical year numbering`.
   * :ref:`year zero` -- they are off by one ("there is no year zero").

Common Era and :ref:`Python` datetime calculations:

.. code:: python

    # Paleolithic Era (2.6m years ago -> 12000 years ago)
    # "2.6m years ago" = (2.6m - (2015)) BCE = 2597985 BCE = -2597985 CE

    2597985 BCE == -2597985 CE

    ### Python datetime w/ scientific notation string formatter
    >>> import datetime
    >>> year = datetime.datetime.now().year
    >>> '{:.6e}'.format(2.6e6 - year)
    '2.597985e+06'

    ### Python datetime supports (dates >= 1 BCE).
    >>> datetime.date(1, 1, 1)
    datetime.date(1, 1, 1)
    >>> datetime.datetime(1, 1, 1)
    >>> datetime.datetime(1, 1, 1, 0, 0)

    ### Python pypi:arrow supports (dates >= 1 BCE).
    >>> !pip install arrow
    >>> arrow.get(1, 1, 1)
    <Arrow [0001-01-01T00:00:00+00:00]>

    ### astropy.time.Time supports (1 BCE <= dates >= 1 CE) and/or *Year Zero*
    ### https://astropy.readthedocs.org/en/latest/time/
    >>> !conda install astropy
    >>> import astropy.time
    >>> # TimeJulianEpoch (Julian date (jd) ~= Common Era (CE))
    >>> astropy.time.Time(-2.6e6, format='jd', scale='utc')
    <Time object: scale='utc' format='jd' value=-2600000.0>


.. index:: Time Zones
.. _time zones:

Time Zones
++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Time_zone

https://en.wikipedia.org/wiki/Daylight_saving_time

https://en.wikipedia.org/wiki/List_of_UTC_time_offsets

https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

* :ref:`iso8601`


.. index:: UTC
.. index:: Coordinated Universal Time
.. _utc:

UTC
`````
| Wikipedia: https://en.wikipedia.org/wiki/Coordinated_Universal_Time

UTC (*Coordinated Universal Time*) is
the primary terrestrial Earth-based clock time.

* Earth :ref:`time zones` are specified as
  offsets from `UTC`.
* UTC time is set determined by :ref:`iat`;
  with occasional leap seconds
  to account for the difference between
  Earth's rotational time and
  the actual passage of time
  according to the decay rate of cesium atoms
  (an :ref:`SI Unit <si units>` calibrated with an *atomic clock*;
  see :ref:`QUDT`).
* Many/most computer systems work with UTC,
  but are not
  exactly synchronized with :ref:`iat`
  (see also: `RTC`, :ref:`NTP` and `time drift`).


.. index:: US Time Zones
.. _us time zones:

US Time Zones
`````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Time_in_the_United_States

https://en.wikipedia.org/wiki/Time_in_the_United_States#Standard_time_and_daylight_saving_time

https://en.wikipedia.org/wiki/History_of_time_in_the_United_States


Time Zone names, URIs, and :ref:`iso8601` UTC offsets:

.. table:: Table of US Time Zones
    :class: table-responsive table-striped

    +----------------------------------------------------------+----------------+--------------------+
    | **Time Zone names, URNs, URIs**                          | **UTC Offset** | **UTC DST Offset** |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Coordinated_Universal_Time |                |                    |
    |                                                          |                |                    |
    | #tz: Coordinated Universal Time, **UTC**, **Zulu**       | -0000 Z        |  +0000 Z           |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Atlantic_Time_Zone         |                |                    |
    |                                                          |                |                    |
    | https://en.wikipedia.org/wiki/America/Halifax            |                |                    |
    |                                                          |                |                    |
    | #tz: Atlantic, Antarctica (Palmer), **AST**, ADT         | -0400 AST      | -0300 ADT          |
    |                                                          |                |                    |
    | America/Halifax                                          |                |                    |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/America/St_Thomas          |                |                    |
    |                                                          |                |                    |
    | #tz: America/St_Thomas, America/Virgin                   | -0400          | -0400              |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Eastern_Time_Zone          |                |                    |
    |                                                          |                |                    |
    | https://en.wikipedia.org/wiki/EST5EDT                    |                |                    |
    |                                                          |                |                    |
    | #tz: Eastern, **EST**, EDT                               | -0500 EST      | -0400 EDT          |
    |                                                          |                |                    |
    | America/New_York                                         |                |                    |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Central_Time_Zone          |                |                    |
    |                                                          |                |                    |
    | https://en.wikipedia.org/wiki/CST6CDT                    |                |                    |
    |                                                          |                |                    |
    | #tz: Central, **CST**, CDT                               | -0600 CST      | -0500 CDT          |
    |                                                          |                |                    |
    | America/Chicago                                          |                |                    |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Mountain_Time_Zone         |                |                    |
    |                                                          |                |                    |
    | https://en.wikipedia.org/wiki/MST7MDT                    |                |                    |
    |                                                          |                |                    |
    | #tz: Mountain, **MST**, MDT                              | -0700 MST      | -0600 MDT          |
    |                                                          |                |                    |
    | America/Denver                                           |                |                    |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Pacific_Time_Zone          |                |                    |
    |                                                          |                |                    |
    | https://en.wikipedia.org/wiki/PST8PDT                    |                |                    |
    |                                                          |                |                    |
    | #tz: Pacific, **PST**, PDT                               | -0800 PST      | -0700 PDT          |
    |                                                          |                |                    |
    | America/Los_Angeles                                      |                |                    |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Alaska_Time_Zone           |                |                    |
    |                                                          |                |                    |
    | AKST9AKDT                                                |                |                    |
    |                                                          |                |                    |
    | #tz: Alaska, **AKST**, AKDT                              | -0900 AKST     | -0800 AKDT         |
    |                                                          |                |                    |
    | America/Juneau                                           |                |                    |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Hawaii-Aleutian_Time_Zone  |                |                    |
    |                                                          |                |                    |
    | HAST10HADT                                               |                |                    |
    |                                                          |                |                    |
    | #tz: Hawaii Aleutian, **HAST**, HADT                     | -1000 HAST     | -0900 HADT         |
    |                                                          |                |                    |
    | Pacific/Honolulu                                         |                |                    |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Samoa_Time_Zone            |                |                    |
    |                                                          |                |                    |
    | #tz: Samoa Time Zone, **SST**                            | -1100 SST      | -1100 SST          |
    |                                                          |                |                    |
    | Pacific/Samoa                                            |                |                    |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Chamorro_Time_Zone         |                |                    |
    |                                                          |                |                    |
    | #tz: Chamorro, Guam                                      | +1000          | +1000              |
    |                                                          |                |                    |
    | Pacific/Guam                                             |                |                    |
    +----------------------------------------------------------+----------------+--------------------+
    | https://en.wikipedia.org/wiki/Time_in_Antarctica         |                |                    |
    |                                                          |                |                    |
    | Antarctica (Amundsen, McMurdo), South Pole               | +1200          | +1300              |
    |                                                          |                |                    |
    | Antarctica/South_Pole                                    |                |                    |
    +----------------------------------------------------------+----------------+--------------------+

.. index:: US Daylight Saving Time
.. index:: Daylight Saving Time
.. _daylight saving time:

US Daylight Saving Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Daylight_saving_time_in_the_United_States

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


.. index:: ISO8601
.. index:: iso8601
.. _iso8601:

ISO8601
+++++++++
| Wikipedia: https://en.wikipedia.org/wiki/ISO_8601
| Standard: http://www.iso.org/iso/iso8601

ISO8601 is an :ref:`ISO` standard for specifying Gregorian
dates, times, datetime intervals, durations, and recurring datetimes.

* The ``date`` command can print :ref:`iso8601` -compatible
  datestrings:

  .. code:: bash

      $ date +'%FT%T%z'
      2016-01-01T22:11:59-0600

      $ date +'%F %T%z'
      2016-01-01 22:11:59-0600

* Roughly, an ISO8601 datetime is specified as:
  year,
  dash
  month,
  dash
  day,
  (``T`` or `` `` [space-character]),
  hour,
  colon,
  minute,
  colon,
  second,
  (``Z`` [for UTC] or a
  :ref:`time zone <time zones>` offset
  (e.g. ``+``/``-`` ``-0000``, ``+0000``));
  where the dashes and colons are optional.

* ISO8601 specifies a standard for absolute time durations:
  start date, forward-slash, end date.

* ISO8601 specifies a standard for relative time durations:
  number of years ``Y``, months ``M``, days ``D``,
  hours ``H``, minutes ``M``, and seconds ``S``.

* A ``Z`` timezone specifies **UTC** (*Universal Coordinated Time*)
  (or "Zulu") time.

* Many/most :ref:`W3C` standards (such as :ref:`XSD`)
  specify :ref:`ISO8601` time formats:
  http://www.w3.org/TR/NOTE-datetime

A few examples of ISO8601:

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


.. index:: Network Time Protocol
.. index:: NTP
.. _ntp:

NTP
++++
| Wikipedia: https://en.wikipedia.org/wiki/Network_Time_Protocol
| Homepage: http://www.pool.ntp.org/en/

NTP (*Network Time Protocol*) is a standard for synchronizing
clock times.

* Most :ref:`Operating Systems` and mobile devices support
  :ref:`NTP`.
* NTP clients calculate *time drift* (or *time skew*)
  and network latency
  and then gradually adjust the local system time
  to the most recently retrieved server time.
* Many OS distributions run their own :ref:`NTP` servers
  (in order to reduce load on the core NTP pool servers).


.. index:: Linked Data
.. _linked data:

Linked Data
-------------
| Wikipedia: https://en.wikipedia.org/wiki/Linked_data

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


See: :ref:`Semantic Web`


.. index:: Semantic Web
.. _semantic web:

Semantic Web
-------------
| Wikipedia: https://en.wikipedia.org/wiki/Semantic_Web
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Semantic_Web

https://en.wikipedia.org/wiki/Template:Semantic_Web

`<https://en.wikipedia.org/wiki/Semantics_(computer_science)>`_

:ref:`W3C` Semantic Web Wiki:

* http://www.w3.org/2001/sw/wiki
* http://www.w3.org/2001/sw/wiki/Books
* http://www.w3.org/2001/sw/wiki/Tools


.. index:: Semantic Web Standards
.. _semantic web standards:

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
.. _web standards:

Web Standards
---------------
| Wikipedia: https://en.wikipedia.org/wiki/Web_standards

.. index:: Web Names
.. _web names:

Web Names
+++++++++++

.. index:: URL
.. _url:

URL
`````
* :term:`URL`


.. index:: URI
.. _uri:

URI
`````
* :term:`URI`
* :term:`Magnet URI`

.. index:: URN
.. _urn:

URN
````
* :term:`URN`


.. index:: IEC
.. _iec:

IEC
+++++
| Wikipedia: https://en.wikipedia.org/wiki/International_Electrotechnical_Commission
| Homepage: http://www.iec.ch/

IEC (*International Electrotechnical Commission*) is a standards body.

* List of IEC standards: https://en.wikipedia.org/wiki/List_of_IEC_standards


.. index:: IETF
.. _ietf:

IETF
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Internet_Engineering_Task_Force
| Homepage: https://www.ietf.org/

IETF (*Internet Engineering Task Force*) is a standards body.

* List of IETF standards: https://tools.ietf.org/html/


.. index:: ISO
.. _iso:

ISO
++++
| Wikipedia: https://en.wikipedia.org/wiki/International_Organization_for_Standardization
| Homepage: http://www.iso.org/

ISO (*International Organization for Standardization*) is a standards
body.

* List of ISO standards: http://www.iso.org/iso/home/standards.htm


.. index:: OMG
.. _omg:

OMG
++++
| Wikipedia: https://en.wikipedia.org/wiki/Object_Management_Group
| Homepage: http://www.omg.org/

OMG (*Object Management Group*) is a standards body.

* UML is an OMG standard.
* :ref:`CORBA` is now an OMG standard.
* List of OMG standards: http://www.omg.org/spec/

  https://en.wikipedia.org/wiki/Object_Management_Group#OMG_Standards


.. index:: W3C
.. _w3c:

W3C
++++
| Wikipedia: https://en.wikipedia.org/wiki/World_Wide_Web_Consortium
| Homepage: http://www.w3.org/

W3C (*World Wide Web Consortium*) is a standards body.

* List of W3C standards: http://www.w3.org/TR/


.. index:: HTTP
.. _HTTP:

HTTP
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol
| Standard: https://tools.ietf.org/html/rfc2616
| Standard: http://tools.ietf.org/html/rfc7230#page-5
| Docs: https://www.mnot.net/blog/2014/06/07/rfc2616_is_dead
| URI Scheme: ``http://``
| URI Scheme: ``https://``

HTTP (*HyperText Transfer Protocol*) is an :ref:`open source`
text-based request-response
TCP/IP protocol for text and binary data interchange.

* :ref:`HTTPS` (*Secure HTTP*) wraps HTTP in SSL/TLS to secure HTTP.


.. index:: HTTP in RDF
.. _http in rdf:

HTTP in RDF
`````````````
| Standard: http://www.w3.org/TR/HTTP-in-RDF10/
| Namespace: `<http://www.w3.org/2011/http#>`__
| Namespace: `<http://www.w3.org/2011/http-headers> .`__
| Namespace: `<http://www.w3.org/2011/http-methods> .`__
| Namespace: `<http://www.w3.org/2011/http-statusCodes> .`__
| xmlns: ``@prefix http: <http://www.w3.org/2011/http#> .``
| xmlns: ``@prefix http-headers: <http://www.w3.org/2011/http-headers> .``
| xmlns: ``@prefix http-methods: <http://www.w3.org/2011/http-methods> .``
| xmlns: ``@prefix http-statusCodes: <http://www.w3.org/2011/http-statusCodes> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/http

HTTP-in-RDF is a standard for representing :ref:`HTTP` as :ref:`RDF`.


.. index:: HTTPS
.. _https:

HTTPS
```````
| Standard: https://tools.ietf.org/html/rfc2818 (2000)
| Wikipedia: https://en.wikipedia.org/wiki/HTTPS
| Wikipedia: https://en.wikipedia.org/wiki/Transport_Layer_Security
| Wikipedia: https://en.wikipedia.org/wiki/Secure_Sockets_Layer

HTTPS (*HTTP over SSL*) is :ref:`HTTP` wrapped in TLS/SSL.

* TLS (*Transport Layer Security*)
* SSL (*Secure Sockets Layer*)


.. index:: HTTP STS
.. index:: HTTP Strict Transport Security
.. _http sts:

HTTP STS
``````````
| Wikipedia: https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security

HTTP STS (*HTTP Strict Transport Security*) is
a standardized extension for notifying browsers
that all requests should be made over :ref:`HTTPS`
indefinitely or for a specified time period.

See also: :ref:`https everywhere`


.. index:: CSS
.. _css:

CSS
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Cascading_Style_Sheets
| Docs: :ref:`CSS`

CSS (*Cascading Style Sheets*) define the presentational
aspects of :ref:`HTML` and a number of mobile and desktop
web framworks.

* CSS is designed to ensure separation of data and presentation.
  With javascript, the separation is then data, code, and presentation.


.. index:: RTMP
.. _rtmp:

RTMP
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Real_Time_Messaging_Protocol

RTMP is a TCP/IP protocol for streaming audio, video, and data
originally for Flash which is now :ref:`open source`.

* https://en.wikipedia.org/wiki/Real_Time_Messaging_Protocol#Client_software

  * Adobe Flash Player
  * :ref:`VLC`

* https://en.wikipedia.org/wiki/Real_Time_Messaging_Protocol#Server_software

  * Adobe Flash Live Media Server
  * :ref:`AWS` S3 HTTP Object Storage, CloudFront :ref:`CDN`
  * Helix Universal Media Server
  * Red5 (:ref:`open source`)
  * :ref:`ffmpeg` (:ref:`open source`)
  * :ref:`nginx-rtmp-module` (:ref:`open source`)
  * FreeSwitch (:ref:`OpenSource <open source>`, VoIP, SIP, :ref:`Video Chat`)

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

https://en.wikipedia.org/wiki/Comparison_of_WebSocket_implementations

* :ref:`Python`: pypi:gevent-websocket,
  pypi:websockets (asyncio),
  pypi:autobahn (pypi:twisted, asyncio)

See also: https://en.wikipedia.org/wiki/Push_technology, :ref:`WebRTC`



.. index:: WebRTC
.. _webrtc:

WebRTC
++++++++
| Wikipedia: https://en.wikipedia.org/wiki/WebRTC
| Homepage: http://www.webrtc.org/
| Standard: http://tools.ietf.org/wg/rtcweb/
| Docs: https://webrtc.github.io/samples/

WebRTC is a :ref:`web standard <web standards>` for
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
.. _http2:

HTTP/2
++++++
| Wikipedia: https://en.wikipedia.org/wiki/HTTP/2
| Homepage: https://http2.github.io/
| Standard: https://http2.github.io/http2-spec/
| Standard: https://http2.github.io/http2-spec/compression.html
| Standard: https://tools.ietf.org/html/rfc7540
| Docs: https://github.com/http2/http2-spec/wiki/Implementations

HTTP/2 (*HTTP2*) is the newest standard for :ref:`HTTP`.

* HTTP/2 is largely derived from the SPDY protocol.



.. index:: HTML
.. _HTML:

HTML
+++++
| Wikipedia: https://en.wikipedia.org/wiki/HTML

HTML (*HyperText Markup Language*) is a :ref:`open source`
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


.. index:: CSVW
.. _csvw:

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

See also: :ref:`triplestores`


.. index:: RDF Interfaces
.. _rdf interfaces:

RDF Interfaces
````````````````
| Standard: http://www.w3.org/TR/rdf-interfaces/
| Docs: http://www.w3.org/TR/rdf-interfaces/#high-level-api

RDF Interfaces is an :ref:`open source` standard
for :ref:`RDF` APIs (e.g. as implemented by RDF libraries
and :ref:`triplestores`.

* ``createBlankNode`` --> ``BlankNode``
* ``createNamedNode`` --> ``NamedNode``
* ``createLiteral`` --> ``Literal``
* ``createTriple`` --> ``Triple``
  (``RDFNode`` s, ``RDFNode`` p, ``RDFNode``, o)
* ``createGraph`` --> ``[]Triple``
* ``createAction`` --> ``TripleAction`` (``TripleFilter``, ``TripleCallback``)
* ``createProfile`` --> ``Profile``
* ``createTermMap`` --> ``TermMap``
* ``createPrefixMap`` --> ``PrefixMap``

Implementations of RDF Interfaces:

* :ref:`Javascript` and/or :ref:`Node.js` implementations of RDF Interfaces:

  http://www.w3.org/community/rdfjs/wiki/Comparison_of_RDFJS_libraries

  + https://github.com/Acubed/node-rdf
  + https://github.com/antoniogarrote/rdfstore-js
  + https://github.com/bergos/rdf-ext

* :ref:`rdflib` (:ref:`python`) mappings to RDF Interfaces:

  + ``BlankNode`` -> ``rdflib.term.BNode``
  + ``NamedNode`` -> ``rdflib.term.URIRef``, ``rdflib.term.Variable`` ? TODO
  + ``Literal`` -> ``rdflib.term.Literal``
  + ``Triple`` ->  ``tuple()``
  + ``Graph`` -> ``rdflib.graph.Graph``,
    ``rdflib.graph.ConjunctiveGraph``,
    ``rdflib.graph.QuotedGraph``, ``list()``
  + ``Action`` -> _____ TODO
  + ``TripleFilter`` / ``TripleCallback`` ->
    ``rdflib.store.TripleAddedEvent`,
    ``rdflib.store.TripleRemovedEvent``

  + https://rdflib.readthedocs.org/en/latest/apidocs/rdflib.html#rdflib.term.Node
  + ``Profile`` -> ______ TODO
  + ``TermMap`` ->  ____ TODO
  + ``PrefixMap`` -> ``rdflib.namespace.NamespaceManager``
    https://rdflib.readthedocs.org/en/latest/apidocs/rdflib.html#rdflib.namespace.NamespaceManager

  .. note:: rdflib is not order-preserving at this time,
     because internally Graphs are represented as ``dict`` and not yet
     ``collections.OrderedDict`` (for which there is a now C-implementation
     in the Python 3.5 standard library);
     so output may not be in the same sequence as input
     (or a ``rdflib.store.Store``, even)
     even when there are no changes made to the graph.

     * It would be preferable to maintain the input source order
       (though, especially for large distributed queries
       which merge triples into one context,
       sorted / source order is not a good assumption to make).
     * ``rdf:List`` are ordered.

       * ``rdf:List`` with :ref:`Turtle` / :ref:`N3`:
         ``:examplePredicate [ "uno"@es, "one"@en ] ;``)

          * http://www.w3.org/TR/rdf-schema/#ch_list
          * ``rdf:first``, ``rdf:rest``, ``rdf:nil``:
            "RDFS does not require that there be only one first element of a list-like structure, or even that a list-like structure have a first element."

       * ``rdf:List`` with :ref:`JSON-LD` ``@context``:

         * http://www.w3.org/TR/json-ld/#lists-and-sets
         * http://www.w3.org/TR/json-ld/#sets-and-lists
         * ``{"@context": {"attr": {"@container": "@list"}}}``
         * ``{"attr": {"@list": ["one", "uno"]}}``


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
| Standard: http://www.w3.org/TR/rdfa-syntax/
| Standard: https://www.w3.org/2011/rdfa-context/rdfa-1.1
| Docs: http://www.w3.org/TR/rdfa-primer/

RDFa (*RDF in attributes*) is a standard for storing
structured data (:ref:`RDF` triples) in :ref:`HTML`,
(:ref:`XHTML`, :ref:`HTML5`) attributes.

:ref:`Schema.org` structured data can be included in an HTML page as
RDFa.


.. index:: RDFa Core Context
.. _rdfa core context:

RDFa 1.1 Core Context
```````````````````````
| Standard: https://www.w3.org/2011/rdfa-context/rdfa-1.1
| Standard:  http://www.w3.org/2013/json-ld-context/rdfa11
| Docs: https://github.com/RDFLib/rdflib/blob/master/rdflib/plugins/parsers/pyRdfa/initialcontext.py

The RDFa 1.1 Core Context defines a number of commonly used
vocabulary namespaces and URIs (*prefix mappings*).

An example :ref:`RDFa` :ref:`HTML5` fragment with vocabularies drawn from
the :ref:`RDFa` 1.1 Core Context:

.. code:: html

   <div vocab="schema: http://schema.org/">
     <div typeof="schema:Thing">
       <span property="schema:name">RDFa 1.1 JSON-LD Core Context</span>
       <a property="schema:url">http://www.w3.org/2013/json-ld-context/rdfa11</a>
     </div>
   </div>

An example :ref:`JSON-LD` document with the :ref:`RDFa` 1.1 Core Context:

.. code:: javascript

   {"@context": "http://www.w3.org/2013/json-ld-context/rdfa11",
    "@graph": [
      {"@type": "schema:Thing"
       "schema:name": "RDFa 1.1 JSON-LD Core Context",
       "schema:url": "http://www.w3.org/2013/json-ld-context/rdfa11"}
    ]}


.. note:: :ref:`Schema.org` is included in the RDFa 1.1 Core Context.

   Schema.org does, in many places, reimplement other vocabularies
   e.g. for consistency with Schema.org/DataType s like schema.org/Number.

   There is also :ref:`Schema.org RDF <schema.org-rdf>`,
   which, for example maps ``schema:name`` to ``rdfs:label``;
   and :ref:`OWL`.


.. index:: JSON-LD
.. _jsonld:
.. _json-ld:

JSON-LD
````````
| Wikipedia: https://en.wikipedia.org/wiki/JSON-LD
| Homepage: http://json-ld.org/
| Standard: http://www.w3.org/TR/json-ld/

JSON-LD (*JSON Linked Data*) is a standard for expressing
:ref:`RDF` :ref:`Linked Data` as :ref:`JSON`.

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


.. index:: EARL
.. _earl:

EARL
``````
| Standard: https://www.w3.org/TR/EARL10/
| Namespace: `<http://www.w3.org/ns/earl#>`__
| xmlns: ``@prefix earl: http://www.w3.org/ns/earl#``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/earl

:ref:`W3C` EARL (*Evaluation and Reporting Language*) is an RDFS
vocabulary for automated, semi-automated, and manual test results.

* The JSON-LD Implementation test results are expressed with EARL:

  | http://json-ld.org/test-suite/
  | http://json-ld.org/test-suite/reports/


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


.. index:: SHACL
.. _shacl:

SHACL
```````
| Standard: https://www.w3.org/TR/shacl/
| Namespace: `<http://www.w3.org/ns/shacl#>`__
| xmlns: ``@prefix sh: <http://www.w3.org/ns/shacl#> .``
| LOVLink:

:ref:`W3C` SHACL (*Shapes Constraint Language*) is a language for describing
:ref:`RDF` and :ref:`RDFS` graph shape constraints.

* SHACL relaxes specific RDFS restrictions:
  https://www.w3.org/TR/shacl/#shacl-rdfs
* Required RDFS / :ref:`OWL` :ref:`entailment` can be specified in SHACL with
  the ``sh:entailment`` property and e.g. :ref:`SPARQL` 1.1 entailment
  IRIs.
  https://www.w3.org/TR/shacl/#entailment
* https://github.com/TopQuadrant/shacl


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
.. _schemaorg:
.. _Schema.org:

Schema.org
+++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Schema.org
| Homepage: https://schema.org
| Download: https://schema.org/version/latest/
| Source: https://github.com/schemaorg/schemaorg
| Source: https://github.com/schemaorg/schemaorg/tree/sdo-phobos/data/releases/2.2
| Docs: http://dataliberate.com/2016/02/evolving-schema-org-in-practice-pt1-the-bits-and-pieces/
| Issues: https://github.com/schemaorg/schemaorg/issues
| IssueLabels: https://github.com/schemaorg/schemaorg/labels

Schema.org is a vocabulary for expressing structured data on the web.

Schema.org can be expressed as microdata, :ref:`RDF`, :ref:`RDFa`,
and :ref:`JSON-LD`.

* http:s//schema.org/docs/full.html
* https://schema.org/docs/schemas.html
* https://schema.org/docs/releases.html
* https://www.w3.org/wiki/WebSchemas
* https://www.w3.org/wiki/WebSchemas/SchemaDotOrgProposals
* https://www.w3.org/wiki/WebSchemas/Accessibility

.

* "Schema.org: Evolution of Structured Data on the Web" (2015)
  https://queue.acm.org/detail.cfm?id=2857276

* "Evolving Schema.org in Practice Pt1: The Bits and Pieces" (2016)
  http://dataliberate.com/2016/02/evolving-schema-org-in-practice-pt1-the-bits-and-pieces/

.. note:: The `<https://schema.org/>`__ site is served over HTTPS,
   but the schema.org terms are HTTP **URIs**

.. index:: Schema.org RDF
.. _schema.org-rdf:
.. _schemaorg rdf:

Schema.org RDF
````````````````
| xmlns: ``@prefix schema: <http://schema.org/> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/schema
| Standard: https://schema.org/docs/schema_org_rdfa.html [:ref:`RDFa`]

Tools and Mappings

* https://github.com/mhausenblas/schema-org-rdf
* http://schema.rdfs.org/tools.html
* http://schema.rdfs.org/mappings.html

.. index:: Schema.org TopBraid RDF
.. _schemaorg topbraid rdf:

Schema.org TopBraid RDF
``````````````````````````````````````````
| Homepage: http://topbraid.org/schema/
| Docs: http://topbraid.org/schema/
| xmlns: ``@prefix schema: <http://schema.org/> .``
| xmlns: ``@prefix schemax: <http://topbraid.org/schemax/> .``

TopBraid maintains more complete :ref:`OWL` :ref:`RDF`
transformations of :ref:`Schema.org`.

* http://topbraid.org/schema/schema.rdf :ref:`rdfxml`
* http://topbraid.org/schema/schema.ttl :ref:`turtle`
* http://topbraid.org/schema/schema-single-range.ttl :ref:`turtle`
  with only one type per range




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
for :ref:`RDF` :ref:`Linked Data`.

* http://www.w3.org/TR/ldp/#terms

Features:

* :ref:`HTTP` REST API for *Linked Data Platform Containers* (LDPC)
  containing Linked Data Plaform **Resources** (LDPR)
* Server-side *Paging*




.. index:: OWL
.. index:: Web Ontology Language
.. _owl:

OWL
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Web_Ontology_Language
| Standard: http://www.w3.org/TR/owl2-overview/
| Standard: http://www.w3.org/TR/owl2-primer/
| Standard: http://www.w3.org/TR/owl2-quick-reference/
| Standard: http://www.w3.org/TR/owl2-profiles/
| xmlns: ``@prefix owl: <http://www.w3.org/2002/07/owl#> .``
| LOVLink: http://lov.okfn.org/dataset/lov/vocabs/owl

OWL (*Web Ontology Language*) layers semantics, reasoning, inference,
and entailment capabilities onto :ref:`RDF` (and general logical set
theory).

* OWL as :ref:`Turtle`: `<http://www.w3.org/2002/07/owl#>`__
* https://www.w3.org/TR/owl2-quick-reference/#Names.2C_Prefixes.2C_and_Notation
* https://www.w3.org/TR/owl2-quick-reference/#OWL_2_constructs_and_axioms

A few notable OWL classes:

* ``owl:Class`` a ``owl:Class`` ;
  ``rdfs:subClassOf`` ``rdfs:Class`` (:ref:`RDFS`)
* ``owl:Thing`` a ``owl:Class`` -- universal class
* ``owl:Nothing`` a ``owl:Class`` -- empty class
* ``owl:Restriction`` a ``rdfs:Class`` ;
  ``rdfs:subClassOf`` ``owl:Class``

A few OWL Property types:

* ``owl:DatatypeProperty``
* ``owl:ObjectProperty``
* ``owl:ReflexiveProperty``
* ``owl:IrreflexiveProperty``
* ``owl:SymmetricProperty``
* ``owl:TransitiveProperty``
* ``owl:FunctionalProperty``
* ``owl:InverseFunctionalProperty``
* ``owl:OntologyProperty``
* ``owl:AnnotationProperty``
* ``owl:AsymmetricProperty``

https://en.wikipedia.org/wiki/Cardinality

* ``owl:minCardinality``
* ``owl:cardinality``
* ``owl:maxCardinality``

.

* ``owl:intersectionOf``
* ``owl:unionOf``
* ``owl:complementOf``
* ``owl:oneOf``

.

* ``owl:allValuesFrom``
* ``owl:someValuesFrom``

.

| `<https://www.w3.org/2002/07/owl#>`__
| https://www.w3.org/TR/owl2-quick-reference/


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


.. index:: Wikidata
.. _wikidata:

Wikidata
`````````
| Wikipedia: https://en.wikipedia.org/wiki/Wikidata
| Homepage: https://www.wikidata.org/

Wikidata is an :ref:`open source` collaboratively edited knowledgebase.

* :ref:`dbpedia` scrapes data from Wikipedia Infoboxes
  periodically. :ref:`wikidata` *is* a database with
  forms, datatypes, and alphanumerical identifiers
  (which do not change or redirect).
* Wikidata :ref:`SPARQL`, :ref:`RDF`, and :ref:`OWL`
  will be powered by :ref:`blazegraph`.


.. index:: Semantic Web Tools
.. _semantic web tools:

Semantic Web Tools
---------------------
| Homepage: http://www.w3.org/2001/sw/wiki/Tools

:ref:`Semantic Web` Tools are designed to work with :ref:`RDF` formats.

See also: :ref:`triplestores`


.. index:: CKAN
.. _ckan:

CKAN
++++++
| Wikipedia: https://en.wikipedia.org/wiki/CKAN
| Homepage: http://ckan.org/
| Source: git https://github.com/ckan/ckan
| Source: git https://github.com/ckan/ckan-docker
| DockerHub: https://registry.hub.docker.com/u/ckan/ckan/
| Docs: http://docs.ckan.org/en/latest/
| Docs: http://docs.ckan.org/en/latest/maintaining/installing/index.html
| Docs: http://docs.ckan.org/en/latest/maintaining/data-viewer.html
| Docs: http://docs.ckan.org/en/latest/maintaining/paster.html
| Docs: http://docs.ckan.org/en/latest/maintaining/linked-data-and-rdf.html
| Docs: http://docs.ckan.org/en/latest/api/

CKAN (*Comprehensive Knowledge Archive Network*)
is an :ref:`open source` data repository :term:`web application`
and API
written in :ref:`python` with support for :ref:`rdf`.

* https://datahub.io is powered by CKAN.
  :ref:`LODCloud` draws from datahub.io datasets.
* Many national data.gov sites are powered by CKAN.
  (e.g https://catalog.data.gov/)
* Many public and private data repositories are powered by CKAN.
* CKAN is currently *not yet*
  built on an :ref:`RDF triplestore <triplestores>`.
* There are :ref:`Docker` :term:`Dockerfiles <dockerfile>`
  for CKAN.


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


