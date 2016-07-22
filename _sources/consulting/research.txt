
.. index:: Research
.. _research:

Research
==========


.. index:: Folders and Labels
.. _folders and labels:

Folders and Labels
--------------------
- Folders are exclusive.
- Labels are inclusive.
- #Hashtags are labels.
- Folders form a tree which may be flat.
- Labels can form a tree but are otherwise flat.
- Folder path: a/b/c
- Nested label: a.b.c


.. index:: Citation Metadata
.. _citation metadata:

Citation Metadata
-------------------
Bibliographic citations can take many forms.

Citations are most useful in a structured form
(with a **schema**).

- :ref:`DCMI`
- :ref:`OAI-PMH`
- :ref:`Schema.org` CreativeWork

Citations in the bibliography or references
or resources section of a textual document
must be parsed in order to derived a
**citation graph**.

- :ref:`Zotero`
- :ref:`Mendeley`
- http://citationstyles.org/

Many *impact statistics* are derived from :ref:`graph <graphs>` metricsa
according to citation frequency (and, by implication, things like
centrality).

See:

- :ref:`Knowledge Engineering` > :ref:`graphs`
- :ref:`linkedreproducibility` > :ref:`studygraph`
- :ref:`Zotero and Schema.org RDFa`


.. index:: Search engines
.. _search engines:

Search engines
--------------------
- :ref:`knowledge engineering` > :ref:`search engine indexing`
- Query syntax
- Case sensitivity
- :ref:`Unicode` symbols (Zero, Zerö, Zerø, Ƶero)
- Stemming & Spelling Correction

  - "walking" -> walk -> walk, walking, walkers, walked

- Fuzzy matching

  - :ref:`elasticsearch`
    
    - "Typoes and Mispelings" > "Fuzziness"
      https://www.elastic.co/guide/en/elasticsearch/guide/current/fuzziness.html

      - String distance (*hamming distance*)
      - Substitution, Insertion, Deletion
        (see also: :ref:`Operational Transformation`)

- Regional language variants

  + `<https://en.wikipedia.org/wiki/American_and_British_English_spelling_differences#-our.2C_-or>`__

    + "Colour", "Couleur", and "Color"

  + https://en.wikipedia.org/wiki/Romanization

    + "寿司", "壽司", and "Sushi"


- String prefixes

  - Does "Apple" also return e.g. "Grapple"; or just
    e.g. "apples", "appleton", "apple pie"

- Stop words

  - a, and\*, the, or\*, not\*

- Logical Term grouping

  - "Quoting", (Parentheses), Logical terms (:ref:`Logic`)
  - "This one" AND "That one"
  - "This one" AND ("that one")
  - this one AND that one
  - -this one AND that one
  - -("this one") AND "that one"
  - (NOT "this one") AND ("that one")
  
- Search algorithms:
 
  - :ref:`search engine indexing`
  - :ref:`data structures`
  - :ref:`natural language`
  - Full table scan (match every row every time) [very slow]
  - Document-Term graph / tree
    
    - "index" non-stop words *and phrases* as graph edges
  
    - "entity recognition" / "entity extraction" / "phrase extraction"

      - OpenNLP (Java), NLTK (Python), Watson
      - Mark Twain grew up not in Hannibal, Missouri
        but in St Louis, Missouri.

        - grew up
        - Mark Twain (Mark, Twain, Mark Twain)
        - Hannibal
        - Hannibal, Missouri
        - St Louis
        - St Louis, Missouri

    - Manual Index

      - "biased"
      - https://wrdrd.com/docs/genindex



.. index:: Research Tools

Research Tools
----------------

.. index:: Mendeley
.. _mendeley:

Mendeley
~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Mendeley


- :ref:`Zotero` is similar to Mendeley.


.. index:: Zotero
.. _zotero-:

Zotero
~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Zotero

See:

- :ref:`Zotero`
- :ref:`Zotero and Schema.org RDFa`
- :ref:`Mendeley` is similar to Zotero.


.. index:: CKAN
.. _ckan:

CKAN
~~~~~~~
| Src: https://github.com/ckan
| Src: git https://github.com/ckan/ckan

:ref:`CKAN` (*Comprehensive Knowledge Archive Network*) is an open
source web application
for cataloging data
written in :ref:`Python`.

- There are a number of extensions for CKAN:
  http://extensions.ckan.org/

  - ckanext-extractor can automatically extract text and metadata
    from datasets (including :ref:`PDF`).
    http://extensions.ckan.org/extension/extractor/

    see also:
    
    - :ref:`linkedreproducibility`
    - :ref:`OAI-PMH`, :ref:`Fedora Commons`

  - ckanext-datajson can generate data.gov JSON for datasets:
    http://extensions.ckan.org/extension/datajson/


.. index:: DSpace
.. _dspace:

DSpace
~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/DSpace
| Homepage: http://www.dspace.org/

DSpace is an open source
web application
for creative works and their :ref:`XML` metadata
written in :ref:`Java`.

- DSpace supports :ref:`OAI-PMH`.
- DSpace and :ref:`Fedora Commons` are now both part of DuraSpace.


.. index:: Fedora Commons
.. _fedora commons:

Fedora Commons
~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Fedora_Commons
| Homepage: http://fedorarepository.org/
| Docs: http://fedorarepository.org/features
| Docs: https://wiki.duraspace.org/
| Docs: https://wiki.duraspace.org/display/FEDORA4x/Fedora+4.x+Documentation

Fedora Commons (*Fedora Repository*, *Fedora*) is an open source
web application
for creative works and their :ref:`XML` metadata
written in :ref:`Java`.

- http://fedorarepository.org/features
- Fedora supports :ref:`OAI-PMH`.
- Fedora can index metadata with other search engines
  (e.g. :ref:`Apache Solr`, :ref:`Elasticsearch`)

- There are additional frontend web applications for Fedora:

  - :ref:`Hydra`
  - :ref:`Islandora`

- Fedora Commons is the database for a number of well-known
  institutional repositories
  (e.g. book and digital asset library catalogs).

.. note:: Fedora Commons ("Fedora", "Fedora Repository") is distinct
   from the :ref:`Fedora` Linux operating system.

   Fedora Commons is a :ref:`Java` web application
   which runs in a WAR container on many operating systems.


.. index:: Hydra
.. _hydra:

Hydra
~~~~~~~~
| Homepage: https://projecthydra.org/
| Src: https://github.com/projecthydra
| Docs: https://wiki.duraspace.org/display/hydra/The+Hydra+Project

Hydra is an open source web application
frontend for :ref:`Fedora Commons` written in :ref:`Ruby`

- :ref:`Apache Solr`
- :ref:`Blacklight`


.. index:: Blacklight
.. _blacklight:

Blacklight
~~~~~~~~~~~~
| Homepage: http://projectblacklight.org/
| Src: git https://github.com/projectblacklight/blacklight
| Docs: https://github.com/projectblacklight/blacklight/wiki

Blacklight is an open source web application
written in :ref:`Ruby`
for providing a search interface to :ref:`Apache Solr`.

- :ref:`Hydra` indexes :ref:`Fedora Commons` metadata
  with :ref:`Apache Solr`; which can be displayed with Blacklight.


.. index:: Islandora
.. _islandora:

Islandora
~~~~~~~~~~~
| Homepage: http://islandora.ca/about
| Src: https://github.com/Islandora
| Docs: http://islandora.ca/documentation

Hydra is an open source web application
frontend for :ref:`Fedora Commons` written in :ref:`PHP`

- :ref:`Apache Solr`
- Drupal (:ref:`PHP`)
- :ref:`Islandora` indexes :ref:`Fedora Commons` metadata
  with :ref:`Apache Solr`; which can be displayed with the Islandora
  Drupal application.


.. index:: OAI-PMH
.. _oai-pmh:

OAI-PMH
~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Protocol_for_Metadata_Harvesting

OAI-PMH (Open Metadata Institute Protocol for Metadata Harvesting)
is an :ref:`XML` over :ref:`HTTP`
standard for sharing metadata about creative works
with Dublin Core (:ref:`DCMI` dcterms) and other schema.

- :ref:`Fedora Commons` supports OAI-PMH.
- :ref:`DSpace` supports OAI-PMH.

