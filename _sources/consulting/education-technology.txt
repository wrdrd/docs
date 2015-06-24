
.. index:: Education Technology
.. index:: EdTech
.. _education-technology:

######################
Education Technology
######################
| Wikipedia: https://en.wikipedia.org/wiki/Educational_technology

Self Directed Learning
========================
| "Self-Directed Learning with Online Resources:
|  An independent study of challenges, opportunities and
|  strategies for encouraging feedback
|  between tools and resources in online learning systems" (2012)
|
| Source: https://github.com/westurner/self-directed-learning
| HTML: https://westurner.org/self-directed-learning/
| HTML: http://self-directed-learning.readthedocs.org/
| HTML (zip): http://media.readthedocs.org/htmlzip/self-directed-learning/self-directed-learning.zip
| PDF: http://media.readthedocs.org/pdf/self-directed-learning/latest/self-directed-learning.pdf
| ePub: http://media.readthedocs.org/epub/self-directed-learning/latest/self-directed-learning.epub


.. index:: Publishing
.. _publishing:

Publishing
============
https://en.wikipedia.org/wiki/Publishing

* Project Code and Artifact Repositories

  * :ref:`Version Control<vcs>`: :ref:`Git`, :ref:`Mercurial`
  * Project Forge: GitHub, BitBucket, SourceForge
  * Artifacts: built packages, reports, PDFs, data files

* **DOI**-granting repositories ("getting a citable identifier
  which resolves to a :term:`URL`" (~like a shorturl)):

  * https://en.wikipedia.org/wiki/Digital_object_identifier (:term:`URN`)
  * https://guides.github.com/activities/citable-code/
  * https://figshare.com
  * https://zenodo.org/

* Data Hosting (see: :ref:`Web Distribution`):

  * HTTP Object Storage (private/public :ref:`CDN`)
  * :ref:`BitTorrent`

    * BitTorrent + :ref:`HTTP` :term:`Web Seeds <web seeding>`

  * **It is faster to run the code next to the data.**

    * HDFS (Hadoop, Hive, Cassandra, Spark, :ref:`Mesos`), DDFS (Disco)
    * :ref:`SQL` (:ref:`Relational Database <relational-databases>`)
    * :ref:`SPARQL` (:ref:`Linked Data <linked-data>`)

* Publishing Tools

  + :ref:`Sphinx`
  + :ref:`IPython Notebook` / :ref:`Jupyter Notebook`:
    :ref:`nbformat` JSON -> HTML, HTML slides, LaTeX, PDF, ePub, MOBI


.. index:: Online Courses
.. _online courses:

Online Courses
================
* Course Catalogs

  * :ref:`Class Central`

* :ref:`Linked Curricula Graphs` (:ref:`RDF`, :ref:`RDFa`,
  :ref:`schema.org`/Course)


.. index:: Class Central
.. _class central:

Class Central
**************
| Homepage: https://www.class-central.com/
| Source: git https://github.com/dhawalhshah/class-central/
| OpenBadges: [ ]

Class Central aggregates lists of :ref:`Online Courses`.


.. index:: Coursera
.. _coursera:

Coursera
**********
| Wikipedia: https://en.wikipedia.org/wiki/Coursera
| Homepage: https://www.coursera.org/
| Courses: https://www.coursera.org/courses
| OpenBadges: [ ]
| AndroidApp: https://play.google.com/store/apps/details?id=org.coursera.android
| iOSApp: https://itunes.apple.com/us/app/coursera/id736535961
| Source: https://github.com/coursera
| Docs: https://tech.coursera.org/app-platform/

Coursera is a platform for :ref:`Online Courses`.


.. index:: EdX
.. _edx:

edX
****
| Wikipedia:
| Homepage: https://www.edx.org/
| Courses: https://www.edx.org/course
| OpenBadges: [ ]
| Homepage: https://open.edx.org/
| AndroidApp: https://play.google.com/store/apps/details?id=org.edx.mobile
| iOSApp: https://itunes.apple.com/us/app/edx/id945480667
| Source: https://github.com/edx
| Source: git https://github.com/edx/edx-platform
| Docs: http://docs.edx.org/
| Docs: https://edx.readthedocs.org/projects/edx-guide-for-students/en/latest/
| Docs: https://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/
| Docs: https://github.com/edx/edx-platform/wiki
| Docs: https://github.com/edx/edx-platform/wiki/Sites-powered-by-Open-edX
| Docs: https://open.edx.org/open-edx-rest-apis
| Docs: https://open.edx.org/features-roadmap/all
| Twitter: https://twitter.com/edXOnline

edX is an :ref:`Open Source <open-source>` platform for :ref:`Online Courses`
written mostly in :ref:`Python` and :ref:`Javascript`.


.. index:: Jupyter and edX
.. _jupyter and edx:

Jupyter and edX
~~~~~~~~~~~~~~~~~~

* :ref:`Jupyter Notebook` and :ref:`edX` are mostly written in :ref:`Python`
* It's possible to generate an edX course from Jupyter notebooks:

  + http://mail.scipy.org/pipermail/ipython-dev/2015-February/015911.html
  + https://github.com/topocm/topocm_content/


.. index:: Udacity
.. _udacity:

Udacity
*************
| Wikipedia: https://en.wikipedia.org/wiki/Udacity
| Homepage: https://www.udacity.com/
| Courses: https://www.udacity.com/courses/
| OpenBadges: [ ]
| Docs: https://www.udacity.com/wiki/

Udacity is a platform for :ref:`Online Courses`.

* Udacity offers "Nanodegrees": https://www.udacity.com/nanodegree


.. index:: Jupyter and Learning
.. _jupyter and learning:

Jupyter and Learning
=======================
:ref:`Jupyter` Project is great for learning and education.

* :ref:`Jupyter Notebook`, :ref:`JupyterHub <jupyter>`
* Jupyter Notebook supports over 42 languages other than :ref:`Python`.
* Jupyter notebooks can be published as HTML, PDF, ePub, MOBI.
* Jupyter notebooks can be published as reveal.js HTML slide presentations.
* Jupyter notebooks can be published to and served directly from GitHub repos.
* Jupyter notebooks can be published as :ref:`edX` courses
  (:ref:`Jupyter and edX`)
* Jupyter notebooks can be structured into
  per-user, per-class, per-project :ref:`Docker` containers
  (and folders)
* Jupyter notebooks can be saved to and read from Google Drive:

  https://github.com/jupyter/jupyter-drive

* Jupyter notebooks are great for taking notes:

  https://github.com/notablemind/notablemind

* Jupyter notebooks should specify package dependencies
  (see: `Jupyter and Reproducibility`)

  + Jupyter notebooks can utilize code from :ref:`ScipyStack` :ref:`packages`
    (e.g. :ref:`Pip` :ref:`python packages`, :ref:`conda`, :ref:`Anaconda`)

* :ref:`JupyterHub <jupyter>` servers host :ref:`Jupyter Notebook` servers
  for one or more users; with authentication
  and optional Docker integration.

Learning Topics:

* :ref:`Computer Science <computer-science>`
* :ref:`Data Science > Data Learning <data-learning>`
* :ref:`Software Development <software-development>`
* :ref:`Python`
* :ref:`awesome-python-testing`


.. index:: Jupyter and Reproducibility
.. _jupyter and reproducibility:

Jupyter and Reproducibility
*****************************

:ref:`Jupyter Notebook <jupyter notebook>`,
:ref:`Open Science <open-science>`,
and :ref:`Reproducibility`.

| Lecture notes (in :ref:`IPython Notebook` format) on
| Reproducible Science And Modern Scientific Software
| https://github.com/fperez/reprosw

| "Ten Simple Rules for Reproducible Computational Research"
| http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285#s4

    Rule 3: Archive the Exact Versions of All External Programs Used

* [ ] List required :ref:`packages` and extensions

  * watermark: datetime stamp, package versions

    https://github.com/rasbt/watermark

  * version_information: Python interpreter,
    and :ref:`Python Package <python packages>` versions

    https://github.com/jrjohansson/version_information

* [ ] List *instaleld* :ref:`packages` and extensions

  * :ref:`Pip`: ``pip freeze``
  * :ref:`Conda`: ``conda env export``
  * :ref:`Dpkg`: ``dpkg-query -l``, ``dpkg --get-selections``,
    ``wajig list-installed``

* [ ] List reference and other maybe supported :ref:`OS <operating systems>`

  * :ref:`OSX`, :ref:`Linux`: ``uname -a``
  * :ref:`Windows`: ``systeminfo``

* [ ] List reference and other maybe supported platforms

  * CPU: i386, i686, x86-64, ARMv
  * GPU
  * RAM
  * :ref:`osquery`
  * :term:`Salt Grains`

* [ ] Generate complete machine image (Backup, Restore, :ref:`Virtualization`)

  * Machine image process:

    * [ ] Backup: Take snapshot
    * [ ] Post-process: compress, add metadata, test decompression
    * [ ] Archive: share/store/backup/upload/verify

  * Machine Imaging Tools:

    * `clonezilla` (backup and restore partitions from
      CD/DVD, LAN, HTTP, SSH, PXE)
    * `bup` (:ref:`git`-like backups for very many and very large files)
    * `rsync`, `rsnapshot`, `rdiff`

  * :ref:`Virtualization` Machine Imaging Tools

    * :ref:`Docker` :term:`Dockerfile` and image
    * :ref:`Packer` config and image
    * :ref:`Vagrant` :term:`Vagrantfile` and box


.. index:: Jupyter and TDD
.. _jupyter and tdd:

Jupyter and TDD
*****************
* The input/output feedback cycle of IPython and Jupyter notebooks
  captures the essence of :ref:`Test Driven Development <tdd>`
* Jupyter notebooks can be tested with :ref:`runipy` and :ref:`ipython_nose`
* Jupyter notebooks can be tested and graded with :ref:`nbgrader`
* :ref:`awesome-python-testing` links to a number of testing concepts
  and :ref:`Python` tools


.. index:: nbgrader
.. _nbgrader:

nbgrader
~~~~~~~~~
| Source: git https://github.com/jupyter/nbgrader

:ref:`Jupyter notebooks <jupyter notebook>`
can be submitted and centrally graded with nbgrader.

.. note:: While it's possible to run tests of all code cells
   in a Jupyter notebook programmatically with runipy,
   **it's usually preferable to factor
   testable code into a module and a package**
   (e.g. :ref:`Python Package <python packages>`, :ref:`Conda package <conda>`)
   and then reference those tested functions from within
   a :ref:`Jupyter notebook <jupyter notebook>`.


.. index:: JupyterHub Servers
.. _jupyterhub servers:

JupyterHub Servers
********************

* Sharing resources affords many challenges and opportunities

  * Timeshare resource exhaustion (CPU, RAM, Storage)
  * Security

* Principle of least privilege
  ("privilege separation", :ref:`Confidentiality`)

  https://en.wikipedia.org/wiki/Principle_of_least_privilege

* There are :ref:`Docker` containers for :ref:`IPython Notebook`,
  :ref:`Jupyter Notebook`, :ref:`JupyterHub <jupyter>`
  and supporting services.

  * https://github.com/ipython/ipython/wiki/Install:-Docker

* :ref:`JupyterHub <jupyter>` servers spawn and proxy to
  separate instances of :ref:`Jupyter Notebook`;
  which run on different ports, IPs, and/or containers.

  * https://github.com/jupyter/jupyterhub/wiki/Spawners

* :ref:`JupyterHub <jupyter>` servers authenticate users from a number
  of sources (local, OAuth, GitHub)

  * https://github.com/jupyter/jupyterhub/wiki/Authenticators


Knowledge Engineering
=======================
See: :ref:`Knowledge Engineering <knowledge-engineering>`

.. index:: Linked Curricula Graphs
.. _linked curricula graphs:

Linked Curricula Graphs
*****************************************
* https://westurner.org/self-directed-learning/slides.html#knowledge-graph (2012)
* https://westurner.org/redditlog/#comment/ci3c1o3 (2014)

* [ ] Add :ref:`RDFa` to Course Catalog / Index HTML pages

  * [ ] schema.org/Course: https://github.com/schemaorg/schemaorg/issues/195

* [ ] Link each component of the curriculum to a **Concept URI**

  * :ref:`Knowledge Engineering <knowledge-engineering>`
    lists a number of **Wikipedia Concept URIs**

    Wikipedia (-> DBpedia RDF <- :ref:`LODCloud`))

    * https://en.wikipedia.org/wiki/DBpedia -- Wikipedia page for "DBpedia"
    * https://dbpedia.org/page/DBpedia -- DBpedia page for "DBpedia"
    * https://www.wikidata.org/wiki/Q465 -- Wikidata page for DBpedia ("Q465")

  * A more local/structured vocabulary (with #permalink :term:`URIs <uri>`)
    could also defined mppings from local `Concept URIs` to
    one or more `Wikipedia Concept URIs`

    * `Common Core`
    * `LRMI`

* [ ] Write tools to discover curriculum resources
  relevant to one or more concept :term:`URIs <uri>`
* [ ] Write tools to sequence curriculum resources which have
  :term:`URIs <uri>`

  * :ref:`Art & Design > Web Production <web production>`


.. index:: OpenBadges
.. _openbadges:

OpenBadges
************
| Homepage: http://openbadges.org/
| Wikipedia: https://en.wikipedia.org/wiki/Mozilla_Open_Badges
| Standard: https://github.com/openbadges/openbadges-specification
| Docs: https://wiki.mozilla.org/Badges
| Twitter: https://twitter.com/openbadges

* [ ] OpenBadges :ref:`JSON` Web Signatures and :ref:`Schema.org`
  (:ref:`RDFa`, :ref:`JSON-LD`):

  https://github.com/openbadges/openbadges-specification/issues/9

.. index:: OpenBadges Backpack
.. _openbadges-backpack:

OpenBadges Backpack
***********************
| Homepage: https://backpack.openbadges.org/backpack/
| Source: https://github.com/mozilla/openbadges-backpack


See also: :ref:`Team Building <team-building>`, :ref:`Jupyter`
