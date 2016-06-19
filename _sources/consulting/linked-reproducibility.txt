
.. index:: LinkedReproducibility
.. _linkedreproducibility:

LinkedReproducibility
------------------------
| Hashtag: ``#LinkedReproducibility``
| Twitter: https://twitter.com/hashtag/LinkedReproducibility

* :ref:`Data Science`
* :ref:`Knowledge Engineering` > :ref:`Linked Data`
* :ref:`Information Systems`

* ELI5: Our data is probably already aware of a cure.

  * Cure: Win/Win solution


StudyGraph: Document Nodes and Link Edges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We should use annotations with typed, reified edges to link between
various studies with comparable and incomparable analyses. (e.g.
:ref:`OpenAnnotation` :ref:`OA` :ref:`RDF` :ref:`OWL` with more data
than threaded comments).

- PDFs are the de-facto standard for scientific publishing
- Many journals also / instead request HTML

  - PLoS, for example

- Then, a "study" is a document

  - title -- `<schema.org/name>`__
  - authors -- lead first (usu.)

    - schema.org/TODO -- author, creator, contributor

  - abstract
  - tags/labels/keywords are **edges** to a tag/label/keyword node

    - hierarchical

      - MESH
      - PyPI Trove Classifiers

    - folksonomy

      - tags

        - tags often require deduplication / part of speech
          normalization / de-pluralization / etc

    - Concept URIs

      - wikipedia, dbpedia, wikidata, etc

  - links to :ref:`Linked Data`

    - https://schema.org/Dataset
    - :ref:`CSVW`
    - :ref:`StructuredPremises`

- What we lack are **edges** between the actual studies

  - confirms, seemsToConfirm -> confirmatoryEdge

    - [strength of association ["magnitude"]]

  - reproduces, seemsToReproduce -> reproducibilityEdge
  - refutes
  - disproves
  - TODO: see the list i brainstormed

  - frameworks for edges:

    - :ref:`networkx`
    - :ref:`rdf`

      - http://patterns.dataincubator.org/book/qualified-relation.html
      - http://patterns.dataincubator.org/book/nary-relation.html

    - OpenCog AtomSpace (strength of association)


* Develop best practices guidelines and
  and/or an :ref:`RDF` schema and vocabulary ("``repro:``)
  for linking between studies, their supporting data,
  and their collection methods with URIs.

  * developing vocabularies:

    + :ref:`semantic web tools`
    + :ref:`Git`, :ref:`GitHub Pages`
    + [ ] :ref:`schema.org` extension vocabularies

  * linked reproduciblity edges:

    + ``similarTo``
    + ``concursWith``
    + ``discordantWith``
    + ``intendedToReproduce``
    + ``reproduces``

  * linked reproducibility classes and properties:

    * [x] schema.org/MedicalStudy, MedicalObservationalStudy, MedicalTrial

      * [ ] https://github.com/twamarc/ScheMed

        + http://schema.org/MedicalTrialDesign
        + http://schema.org/DoubleBlindedTrial
        + http://schema.org/InternationalTrial
        + http://schema.org/MultiCenterTrial
        + http://schema.org/OpenTrial
        + http://schema.org/PlaceboControlledTrial
        + http://schema.org/RandomizedTrial
        + http://schema.org/SingleBlindedTrial
        + http://schema.org/SingleCenterTrial
        + http://schema.org/TripleBlindedTrial

    * See: https://westurner.org/opengov/us/#personal-health-agenda


TODO:
- pandas 3402
-


.. index:: StructuredPremises
.. _StructuredPremises:

StructuredPremises: Premises as structured data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- And then URIs for controls / study design

  - see schema.org/MedicalTrialDesign

    - [ ] these could/should be extended to all of science

- logical premises (sequence of propositions)

- i/o sequences

  - :ref:`nbformat` (IPython / Jupyter notebook format)
  
    - insufficient because we need stable premise permalinks
      (across versioned publishing URIs)

      - ``#premise-1``
      - ``#premise-abc398f``


- conclusions (derivations)

  + this is a computation graph
  + it should have links (edges) to the datasets

    + https://schema.org/Dataset
    + "ENH: Linked Datasets (RDF)"
      https://github.com/pydata/pandas/issues/3402

  + figures should have links (edges) to the datasets

    + permalinks to premises

  - #TenSimpleRules for Reproducibile Computational Research
    | http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1003285
    | https://wrdrd.com/docs/consulting/data-science#tensimplerules-for-reproducible-computational-research
    


- further questions

- "downstream" studies / implementations

  - retraction management
  - decisions / policy predicated on said conclusions


LinkedMetaAnalyses
~~~~~~~~~~~~~~~~~~~~
- You evaluated 10, I evaluated (the same / a different) 10 studies

  - PRISMA

    - | Homepage: http://www.prisma-statement.org/
    - http://www.prisma-statement.org/PRISMAStatement/
    - Checklist: http://www.prisma-statement.org/documents/PRISMA%202009%20checklist.pdf
    - Flow Diagram: http://www.prisma-statement.org/documents/PRISMA%202009%20flow%20diagram.pdf

  - evaluation of controls

    - "the URI says they did a Triple Blind Study, but it doesn't sound
      like they had groups named just e.g. X, Y, and Z"

      - disqualified / questionable / etc
      - schema.org/MedicalTrial -> schema.org/ScientificTrial

  - C = Class (RDFS)
  - P = Property (RDFS)
  - :ref:`schema.org/ <schemaorg>`

    - [ ] C: MetaAnalysis

      - [ ] C: CriteriaBase type

        - [ ] C: Criterion

      - [ ] C: ScientificStudy
      
        - [x] C: MedicalStudy
        
          - [ ] C: MedicalObservationalStudy <- ScientificObservationalStudy
          - [ ] C: MedicalTrial <- ScientificTrial

      - [x] C: Dataset

- When do we show?

  - Deadline
  - Only if you also produce your own meta-analyses
  - Only if we're doing Open Access (as required by stipulations of
    federal funding)


RDF Example
~~~~~~~~~~~~~

:ref:`linked data` + :ref:`Reproducibility` => :ref:`Linked Reproducibility`

::

    Reproducibility ---\___  Linked Reproducibility
    Linked Data     ---/


In :ref:`turtle` :ref:`rdf` syntax:
::

    :LinkedData rdf:type skos:Concept ;
        rdfs:label "Linked Data"@en ;
        schema:name "Linked Data"@en ;
        owl:sameAs <https://en.wikipedia.org/wiki/Linked_data> ;
        owl:sameAs <http://dbpedia.org/page/Linked_data> ;

        owl:sameAs <http://ja.dbpedia.org/resource/Linked_data>
        owl:sameAs <http://es.dbpedia.org/resource/Datos_enlazados> ;
        owl:sameAs <http://fr.dbpedia.org/resource/Web_des_donn%C3%A9es> ;
        owl:sameAs <http://nl.dbpedia.org/resource/Linked_data>
        owl:sameAs <http://ko.dbpedia.org/resource/링크드_데이터> ;
        owl:sameAs <http://wikidata.org/entity/Q515701> ;
        .

    :Reproducibility a skos:Concept ;
        rdfs:label "Reproducibility"@en ;
        schema:name "Reproducibility"@en ;
        owl:sameAs <https://en.wikipedia.org/wiki/Reproducibility> ;
        owl:sameAs <http://dbpedia.org/page/Reproducibility> ;
        .

    :LinkedReproducibility a skos:Concept ;
        rdfs:label "Linked Reproducibility"@en ;
        schema:name "Linked Reproducibility"@en ;
        skos:related [ :LinkedData, :Reproducibility ] ;
        .


References
~~~~~~~~~~~~~

- TODO: @westurner

  - reddit
  - twitter
  - hackernews
