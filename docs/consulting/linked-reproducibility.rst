
.. index:: Linked Reproducibility
.. _linked reproducibility:

Linked Reproducibility
------------------------

* :ref:`Data Science`
* :ref:`Knowledge Engineering` > :ref:`Linked Data`
* :ref:`Information Systems`


StudyGraph: Document Nodes and Link Edges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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



TODO:
- pandas 3402
-

StructuredPremises: Premises as structured data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- And then URIs for controls / study design

  - see schema.org/MedicalTrialDesign

    - [ ] these could/should be extended to all of science

- logical premises (sequence of propositions)

- i/o sequences

- conclusions

  - #TenSimpleRules for reproducibile TODO: link back to the data

    - this is a computation graph

- further questions

- "downstream" studies / implementations

  - retraction management
  - policy predicated on said conclusions


LinkedMetaAnalyses
~~~~~~~~~~~~~~~~~~~~
- You evaluated 10, I evaluated (the same / a different) 10 studies

  - PRISMA
  - evaluation of controls

    - "the URI says they did a Triple Blind Study, but it doesn't sound
      like they had groups named just e.g. X, Y, and Z"

      - disqualified / questionable / etc

  - a MetaAnalysis type

- When do we show?

  - Deadline
  - Only if you also produce your own meta-analyses
  - Only if we're doing Open Access (as required by stipulations of
    federal funding)


References
~~~~~~~~~~~~~

- TODO: @westurner

  - reddit
  - twitter
  - hackernews
