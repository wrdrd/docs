
.. index:: Data Science
.. _data science:

Data Science
=============
https://en.wikipedia.org/wiki/Data_science


* https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks


datasciencemasters.org
-------------------------
| "The Open Source Data Science Masters"
| http://datasciencemasters.org/
|

Ten Simple Rules
------------------
| Homepage: http://collections.plos.org/ten-simple-rules
| Hashtag: #TenSimpleRules
| Twitter: https://twitter.com/hashtag/TenSimpleRules?src=hash


#TenSimpleRules for Reproducible Computation Research
++++++++++++++++++++++++++++++++++++++++++++++++++++++

| "Ten Simple Rules for Reproducible Computational Research"
| http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1003285
| DOI: 10.1371/journal.pcbi.1003285 Featured in PLOS Collections

    1. For Every Result, Keep Track of How It Was Produced
    2. Avoid Manual Data Manipulation Steps
    3. Archive the Exact Versions of All External Programs Used
    4. Version Control All Custom Scripts
    5. Record All Intermediate Results, When Possible in Standardized Formats
    6. For Analyses That Include Randomness, Note Underlying Random Seeds
    7. Always Store Raw Data behind Plots
    8. Generate Hierarchical Analysis Output, Allowing Layers of Increasing Detail to Be Inspected
    9. Connect Textual Statements to Underlying Results
    10. Provide Public Access to Scripts, Runs, and Results


1. For Every Result, Keep Track of How It Was Produced

   * :ref:`RDF`, :ref:`JSON-LD` (e.g. :ref:`W3C` :ref:`PROV`)
   * :ref:`Workflow`
   * :ref:`Knowledge Engineering` > :ref:`Linked Data`

2. Avoid Manual Data Manipulation Steps

   * :ref:`Workflow`
   * :ref:`Continuous Delivery`
     
     * :ref:`Test Automation` (e.g. :ref:`Test Driven Development <TDD>`)

3. Archive the Exact Versions of All External Programs Used

   * :ref:`Jupyter and Reproducibility` (``%version_information``,
     ``%watermark``) (should be "Reproducibility and Jupyter Notebook")

4. Version Control All Custom Scripts

   * :ref:`Revision Control` (e.g. :ref:`DVCS`)

5. Record All Intermediate Results, When Possible in Standardized Formats

   * :ref:`Linked Data` (e.g. :ref:`5 ★ Linked Open Data <fivestardata2>`)

6. For Analyses That Include Randomness, Note Underlying Random Seeds

   Python random functions:

   .. code:: python

       print(os.environ['PYTHONHASHSEED'])
       RANDOMSEED = 1  # /dev/[x]random

       import random
       random.seed(RANDOMSEED)

       import numpy as np
       np.random.seed(RANDOMSEED)    # Seed
       print(np.random.get_state())  # State
       np.random.rand(4, 2) # (rows, cols, [...])
       np.random.randn(4, 2) # "standard normal" distribution

   * http://docs.scipy.org/doc/numpy/reference/routines.random.html#distributions
   * 

   Python hash randomization and algorithmic determinism:

   | ``python -R``
   | https://docs.python.org/3/using/cmdline.html#cmdoption-R
   | ``PYTHONHASHSEED``
   | https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED

7. Always Store Raw Data behind Plots

   * Or, "Generate all plots from [source-controlled] [transforms-of]
     raw data"
   * :ref:`Data Visualzation Tools` (:ref:`Data Visualization`)

8. Generate Hierarchical Analysis Output,
   Allowing Layers of Increasing Detail to Be Inspected


   * :ref:`Schema.org`: https://schema.org/docs/full.html
   * :ref:`SKOS`:
     
      | http://www.w3.org/TR/skos-reference/
      | http://www.w3.org/TR/skos-reference/skos.html

     ``skos:narrower``, ``skos:narrowerTransitive``,
     ``skos:broader`` , ``skos:broaderTransistive``,
     [...]

   * :ref:`XKOS`: "An SKOS extension for representing
     statistical classifications"
     
     http://rdf-vocabulary.ddialliance.org/xkos.html

   * :ref:`QB`: "The RDF Data Cube Vocabulary"
     
     ``qb:DataSet``,
     ``qb:Dimension``,
     ``qb:ObservationGroup``,
     ``qb:Slice``, [...]

     http://www.w3.org/TR/vocab-data-cube/

9. Connect Textual Statements to Underlying Results

   * :ref:`Linked Data`: :ref:`URIs <URI>`, :ref:`URLs <URL>`, ``#uri-fragments``
   * :ref:`Turtle` / :ref:`Trig`: ``<>`` (this document, this named graph)
   * :ref:`ReStructuredText`

     * http://sphinx-doc.org/rest.html#footnotes #citations #substitutions
     * https://github.com/yoloseem/awesome-sphinxdoc

10. Provide Public Access to Scripts, Runs, and Results

    * :ref:`Jupyter and Reproducibility`
    * https://en.wikipedia.org/wiki/Comparison_of_source_code_hosting_facilities

      * :ref:`GitHub`: Git
      * :ref:`BitBucket`: Hg, Git

#TenSimpleRules for Creating a Good Data Management Plan
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
| "Ten Simple Rules for Creating a Good Data Management Plan"
| http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004525
| DOI: 10.1371/journal.pcbi.1004525

    1. Determine the Research Sponsor Requirements
    2. Identify the Data to Be Collected
    3. Define How the Data Will Be Organized
    4. Explain How the Data Will Be Documented
    5. Describe How Data Quality Will Be Assured
    6. Present a Sound Data Storage and Preservation Strategy
    7. Define the Project’s Data Policies
    8. Describe How the Data Will Be Disseminated
    9. Assign Roles and Responsibilities
    10. Prepare a Realistic Budget

http://journals.plos.org/plosone/s/data-availability

> PLOS journals require authors to make all data underlying the findings described in their manuscript fully available without restriction, with rare exception.


Data, Information, Knowledge, & Wisdom
------------------------------------------
https://en.wikipedia.org/wiki/Data

https://en.wikipedia.org/wiki/Information

https://en.wikipedia.org/wiki/Knowledge
(see: :ref:`knowledge engineering`)

https://en.wikipedia.org/wiki/Wisdom

::

    # Lead -> Gold

* Data is information
* Information is data
* Raw data is not knowledge
* Wisdom compares knowledges

Optimization
+++++++++++++++++++++++++++
https://en.wikipedia.org/wiki/Mathematical_optimization

Find local and global optima (maxima and minima)
within an n-dimensional field which may be
limited by resource constraints.

.. code:: python

   # Global optima of a 1-dimensional list
   points = [10, 20, 100, 20, 10]
   global_max, global_min = max(points), min(points)
   assert global_max == 100
   assert global_min == 10

   # Local optima of a 1-dimensional list
   sample = points[:1]
   local_max, local_min = max(sample), min(sample)
   assert local_max == 20
   assert local_min == 10

   # A 2-dimensional list ...
   points = [(-0.5, 0),
             (0,  0.5),
             (0.5,  0),
             (0, -0.5)]

* `<https://en.wikipedia.org/wiki/Optimization_(disambiguation)>`__
* https://en.wikipedia.org/wiki/Metaheuristic

  + https://en.wikipedia.org/wiki/Receiver_operating_characteristic
  + http://rayli.net/blog/data/top-10-data-mining-algorithms-in-plain-english/
  + http://scikit-learn.org/stable/tutorial/machine_learning_map/
  + https://en.wikipedia.org/wiki/Firefly_algorithm


Smoothies
+++++++++++

**Data**

Inputs, Outputs

Revenue::

   2014-01-01 1200 CDT  $80
   2014-01-01 1210 CDT  $100
   2014-01-01 1500 CDT  $20

Expenses::

   2014-01-01 wages     $256 ($8/hr * 8hrs * 4 people)
   2014-01-01 utilities $100


**Information**

Aggregations, Tendencies

Revenue (gross)::

   2014-01-01  total: $200

Expenses::

   2014-01-01  total: $356

Net::

   2013-01-01  net:  -$200
   2014-01-01  net:  -$156


On Mondays, we usually (on (simple) average) make about $500.


**Knowledge**

* Positive net revenue is good.
* One customer is worth the world to us.


**Wisdom**

We could save money by not being open on New Years Day,
but, our loyal customers would not be happy about that.


Body Temperature
++++++++++++++++++

**Data** ::

   time, body temp, outdoor temp, indoors/outdoors
   time, exercise type, intensity, duration


**Information**

Daily temperature variance is about n degrees


**Knowledge**

* Walking outside when it is warm increases body temperature
* Walking outside when it is cold decreases body temperature
* Exercise increases body temperature


**Wisdom**

If it's 1745, and body temperature is n degrees above baseline,
I'm probably walking outside and it is hot out.





.. index:: Data Science Theory
.. _data science theory:

Theory
--------


.. index:: Science
.. _science:

Science
+++++++++
https://en.wikipedia.org/wiki/Science

https://en.wikipedia.org/wiki/Outline_of_science

https://en.wikipedia.org/wiki/Category:Science


.. index:: Cognitive Bias
.. _cognitive-bias:

Cognitive Biases
~~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Cognitive_bias

https://en.wikipedia.org/wiki/Heuristics_in_judgment_and_decision-making

https://en.wikipedia.org/wiki/List_of_cognitive_biases

* https://en.wikipedia.org/wiki/Confirmation_bias
* https://en.wikipedia.org/wiki/Post_hoc_ergo_propter_hoc
* https://en.wikipedia.org/wiki/Logical_fallacies#See_also
* https://en.wikipedia.org/wiki/List_of_fallacies
* https://en.wikipedia.org/wiki/Controlling_for_a_variable

  * "distance walked per day"
  * "sports played" (sport, years)

https://en.wikipedia.org/wiki/Critical_thinking


.. index:: Open Science
.. _open-science:

Open Science
~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Open_science

* https://en.wikipedia.org/wiki/Open_source
* https://en.wikipedia.org/wiki/Open_standard
  (:ref:`web standards`,
  :ref:`semantic web standards`)
* https://en.wikipedia.org/wiki/Open_data

https://en.wikipedia.org/wiki/Peer_review

* https://en.wikipedia.org/wiki/Repeatability
* https://en.wikipedia.org/wiki/Reproducibility
* :ref:`Reproducibility`


.. index:: Scientific Method
.. _scientific-method:

Scientific Method
~~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Scientific_method

https://en.wikipedia.org/wiki/Argument

https://en.wikipedia.org/wiki/Empirical_evidence

https://en.wikipedia.org/wiki/Hypothesis

* https://en.wikipedia.org/wiki/Statistical_hypothesis_testing
* https://en.wikipedia.org/wiki/Null_hypothesis
* https://en.wikipedia.org/wiki/Alternative_hypothesis
* https://en.wikipedia.org/wiki/Dependent_and_independent_variables


.. index:: Reproducibility
.. _reproducibility:

Reproducibility
``````````````````
https://en.wikipedia.org/wiki/Design_of_experiments

* https://en.wikipedia.org/wiki/Design_of_experiments#Discussion_topics_when_setting_up_an_experimental_design
* https://en.wikipedia.org/wiki/Repeatability
* https://en.wikipedia.org/wiki/Reproducibility

See: :ref:`Jupyter and Reproducibility`


.. index:: Systematic Review
.. index:: Meta-analysis

Systematic Review
```````````````````
https://en.wikipedia.org/wiki/Meta-analysis

https://en.wikipedia.org/wiki/Systematic_review


.. index:: Linked Reproducibility
.. _linked reproducibility:

Linked Reproducibility
`````````````````````````
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

Further Objectives:

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

      * [ ] @schemed

    * [ ] Study, ObservationalStudy, RandomizedControlledTrial, RCT
    * [ ] StudyProtocol
    * [ ] StudyGroup (design, admin, participant, stats)
    * [ ] StudyGroup.masked <bool>, StudyProtocol.url
    * See: https://westurner.org/opengov/us/#personal-health-agenda


.. index:: Math
.. index:: Mathematics
.. _math:

Math
+++++
https://en.wikipedia.org/wiki/Mathematics

https://en.wikipedia.org/wiki/Outline_of_mathematics

https://en.wikipedia.org/wiki/Mathematics_education#Methods

* http://www.iflscience.com/brain/math-gifs-will-help-you-understand-these-concepts-better-your-teacher-ever-did


.. index:: Math Courses
.. _math courses:

Math Courses
~~~~~~~~~~~~~~
* https://www.khanacademy.org/math/arithmetic
* https://www.khanacademy.org/math/pre-algebra
* https://www.khanacademy.org/math/algebra-basics
* https://www.khanacademy.org/math/algebra
* https://www.khanacademy.org/math/basic-geo
* https://www.khanacademy.org/math/geometry
* https://www.khanacademy.org/math/algebra2
* https://www.khanacademy.org/math/trigonometry
* https://www.khanacademy.org/math/probability
* :ref:`Linear Algebra <linear-algebra>`
* :ref:`Calculus`
* :ref:`information theory`
* "Mathematics for Computer Science" (CC-BY-SA 3.0)

  http://courses.csail.mit.edu/6.042/spring14/mcs.pdf
* https://www.khanacademy.org/math/recreational-math
* https://www.khanacademy.org/math/competition-math
* https://www.class-central.com/subject/maths
* https://en.wikipedia.org/wiki/Kaggle#How_Kaggle_competitions_work


.. index:: Project Euler
.. _project euler:

Project Euler
~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Project_Euler

https://projecteuler.net/

Math Algorithm Problems


.. index:: Rosalind
.. _rosalind:

Rosalind
~~~~~~~~~~
http://rosalind.info/

Bioinformatics and Science Algorithm Problems


.. index:: Mathematical Notation
.. _mathematical-notation:

Mathematical Notation
~~~~~~~~~~~~~~~~~~~~~~~
* https://en.wikipedia.org/wiki/Outline_of_mathematics#Mathematical_notation
* https://en.wikipedia.org/wiki/List_of_mathematical_symbols
* https://en.wikipedia.org/wiki/Greek_letters_used_in_mathematics,_science,_and_engineering
* https://en.wikipedia.org/wiki/Latin_letters_used_in_mathematics


.. index:: LaTeX
.. _LaTeX:

LaTeX
~~~~~~
https://en.wikipedia.org/wiki/LaTeX

* https://en.wikipedia.org/wiki/LaTeX#Examples
* http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference
* http://nbviewer.ipython.org/github/ipython/ipython/blob/master/examples/Notebook/Typesetting%20Equations.ipynb

Tools

* http://docs.mathjax.org/en/latest/tex.html
* http://ipython.org/ipython-doc/dev/install/install.html#mathjax
* http://nbviewer.ipython.org/gist/rpmuller/5920182


.. index:: Information Theory
.. _information theory:

Information Theory
~~~~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Information_theory

`<https://en.wikipedia.org/wiki/Entropy_(information_theory)>`_

`<https://en.wikipedia.org/wiki/Signal_(electrical_engineering)>`_

`<https://en.wikipedia.org/wiki/Noise_(signal_processing)>`_

https://en.wikipedia.org/wiki/Signal-to-noise_ratio


https://en.wikipedia.org/wiki/Probability_theory

* https://www.khanacademy.org/math/probability


.. index:: Linear Algebra
.. _linear-algebra:

Linear Algebra
~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Linear_algebra

* https://www.khanacademy.org/math/linear-algebra
* http://www.ulaff.net/
* https://github.com/ULAFF/notebooks/
  (:ref:`Jupyter Notebooks <jupyter notebook>`)


.. index:: Calculus
.. _calculus:

Calculus
~~~~~~~~~~
https://en.wikipedia.org/wiki/Calculus

* https://www.khanacademy.org/math/precalculus
* https://www.khanacademy.org/math/differential-calculus
* https://www.khanacademy.org/math/integral-calculus
* https://www.khanacademy.org/math/multivariable-calculus
* https://www.khanacademy.org/math/differential-equations
* https://en.wikipedia.org/wiki/AP_Calculus
* http://apcentral.collegeboard.com/apc/public/courses/teachers_corner/2178.html
* http://www.sagemath.org/calctut/
* http://boxen.math.washington.edu/home/wdj/teaching/calc1-sage/
* http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-5-Sympy.ipynb
* http://scipy-lectures.github.io/advanced/sympy.html#calculus
* https://www.class-central.com/subject/calculus-and-mathematical-analysis


.. index:: Statistics
.. _statistics:

Statistics
~~~~~~~~~~~
https://en.wikipedia.org/wiki/Statistics

https://en.wikipedia.org/wiki/Outline_of_statistics

https://en.wikipedia.org/wiki/Category:Statistics

* https://en.wikipedia.org/wiki/Notation_in_probability_and_statistics
* http://apcentral.collegeboard.com/apc/public/courses/teachers_corner/2151.html
* https://www.class-central.com/search?q=statistics


.. index:: Parametric Statistics
.. _parametric-statistics:

Parametric Statistics
````````````````````````
https://en.wikipedia.org/wiki/Parametric_statistics


.. index:: Regression Analysis
.. _regression-analysis:

Regression Analysis
^^^^^^^^^^^^^^^^^^^^^
https://en.wikipedia.org/wiki/Regression_analysis

https://en.wikipedia.org/wiki/Template:Regression_bar

* https://en.wikipedia.org/wiki/Simple_linear_regression
* https://en.wikipedia.org/wiki/Ordinary_least_squares


.. index:: Nonparametric Statistics
.. _nonparametric-statistics:

Nonparametric Statistics
```````````````````````````
https://en.wikipedia.org/wiki/Nonparametric_statistics


.. index:: Descriptive Statistics
.. _descriptive-statistics:

Descriptive Statistics
^^^^^^^^^^^^^^^^^^^^^^^^
https://en.wikipedia.org/wiki/Descriptive_statistics


.. index:: Statistical Inference
.. _statistical-inference:

Statistical Inference
^^^^^^^^^^^^^^^^^^^^^^^
https://en.wikipedia.org/wiki/Statistical_inference

* https://en.wikipedia.org/wiki/Statistical_inference#Models_and_assumptions
* https://en.wikipedia.org/wiki/Statistical_inference#Modes_of_inference

* https://en.wikipedia.org/wiki/Multivariate_statistics

  * https://en.wikipedia.org/wiki/Factor_analysis


.. index:: Causality
.. _causality:

Causality
```````````
https://en.wikipedia.org/wiki/Causality

https://en.wikipedia.org/wiki/Correlation_and_dependence

https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation

https://en.wikipedia.org/wiki/Sensitivity_analysis

https://en.wikipedia.org/wiki/Receiver_operating_characteristic

https://en.wikipedia.org/wiki/Post_hoc_ergo_propter_hoc


.. index:: Data Analysis
.. _data-analysis:

Analysis
++++++++++
https://en.wikipedia.org/wiki/Data_analysis

https://en.wikipedia.org/wiki/Big_data

https://en.wikipedia.org/wiki/Data_processing#Data_processing_functions


.. index:: Data Learning
.. _data-learning:

Learning
~~~~~~~~~
https://en.wikipedia.org/wiki/Learning

* http://plato.stanford.edu/entries/learning-formal/
* http://plato.stanford.edu/entries/logic-inductive/

https://en.wikipedia.org/wiki/Autodidacticism

https://en.wikipedia.org/wiki/Perceptual_learning

https://en.wikipedia.org/wiki/Pattern_recognition_(psychology)#False_pattern_recognition

https://en.wikipedia.org/wiki/Rhetoric

https://en.wikipedia.org/wiki/Socratic_method

https://en.wikipedia.org/wiki/Socratic_questioning

https://en.wikipedia.org/wiki/Platonic_dialogue#The_dialogues

https://en.wikipedia.org/wiki/Dialectic

https://en.wikipedia.org/wiki/Dialogue

`<https://en.wikipedia.org/wiki/Perturbation_theory_(quantum_mechanics)>`_

https://en.wikipedia.org/wiki/Validated_learning

https://en.wikipedia.org/wiki/Organizational_learning

See: :ref:`knowledge engineering`


.. index:: Data Mining
.. _data-mining:

Data Mining
~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Data_mining

https://en.wikipedia.org/wiki/Knowledge_extraction

https://en.wikipedia.org/wiki/Extract,_transform,_load


.. index:: Machine Learning
.. _machine-learning:

Machine Learning
~~~~~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Machine_learning

https://en.wikipedia.org/wiki/Online_machine_learning

* https://en.wikipedia.org/wiki/Supervised_learning
* https://en.wikipedia.org/wiki/Unsupervised_learning


.. index:: Deep Learning
.. _deep learning:

Deep Learning
~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Deep_learning

* https://en.wikipedia.org/wiki/Biological_neural_network
* https://en.wikipedia.org/wiki/Artificial_neural_network
* https://en.wikipedia.org/wiki/Recurrent_neural_network
* http://www.scholarpedia.org/article/Recurrent_neural_networks
* https://en.wikipedia.org/wiki/Feedforward_neural_network
* https://en.wikipedia.org/wiki/Perceptron
* https://en.wikipedia.org/wiki/Reservoir_computing
* http://deeplearning.net/

  * http://deeplearning.net/deep-learning-research-groups-and-labs/
  * http://deeplearning.net/datasets/
  * http://deeplearning.net/software_links/



Datasets
++++++++++



awesome-public-datasets
~~~~~~~~~~~~~~~~~~~~~~~~~~~
https://github.com/caesar0301/awesome-public-datasets

* https://github.com/caesar0301/awesome-public-datasets#search-engines



.. _awesome:

Awesome
~~~~~~~~~~~~
https://github.com/bayandin/awesome-awesomeness

* https://github.com/onurakpolat/awesome-bigdata
* https://github.com/josephmisiti/awesome-machine-learning
* https://github.com/caesar0301/awesome-public-datasets



.. index:: Data Science Tools
.. _data science tools:

Tools
-------

.. index:: ETL

ETL
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Extract,_transform,_load

* https://en.wikipedia.org/wiki/Extract,_transform,_load#Real-life_ETL_cycle


Workflow
++++++++++

* :ref:`Scientific Method <scientific-method>`
* :ref:`Project Management <project management>`
* https://en.wikipedia.org/wiki/Checklist
* https://en.wikipedia.org/wiki/Scientific_workflow_system
* :ref:`Units` of measure
* I/O Transforms of :ref:`information(/energy) <information theory>`


"Data Provenance", "Data Lineage"

* https://en.wikipedia.org/wiki/Provenance#Data_provenance
* https://en.wikipedia.org/wiki/Data_lineage#Data_Provenance
* :ref:`W3C PROV <prov>` Provenance Ontology

  * http://www.w3.org/TR/prov-overview/
  * http://www.w3.org/TR/prov-o/


See:

* :ref:`Knowledge Engineering`
* :ref:`Tools`
* :ref:`Education Technology` > :ref:`Jupyter and Reproducibility`
* :ref:`Education Technology` > :ref:`Publishing`


.. index:: Data Science Techniques
.. _data science techniques:

Techniques
--------------

Automated Workflows
++++++++++++++++++++
Standard, Automated Workflows

* :ref:`Scientific Method <scientific-method>`
* :ref:`Reproducibility`
* `<https://en.wikipedia.org/wiki/Occam's_razor>`__

.. pull-quote::

   Q: Is there confirmation bias in starting with
   e.g. simple regression analysis?

   Q: Which factors did we know we were capturing?


.. _fivestardata2:

5 ★ Linked Open Data
+++++++++++++++++++++++++
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


See: :ref:`knowledge engineering`,
:ref:`semantic web standards`


.. index:: Data Visualization
.. _data-visualization:

Data Visualization
++++++++++++++++++++
https://en.wikipedia.org/wiki/Data_visualization


.. index:: Visualizing Data Science
.. _visualizing data science:

Visualizing Data Science
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Data Science Venn Diagram

* http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram
* http://datascienceassn.org/content/fourth-bubble-data-science-venn-diagram-social-sciences

Field representations

+ https://github.com/josephmisiti/awesome-machine-learning
+ http://scikit-learn.org/stable/tutorial/machine_learning_map/
+ :ref:`LODCloud`


.. index:: Data Visualization Tools
.. _data visualization tools:

Data Visualization Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~


https://en.wikipedia.org/wiki/Matplotlib

* http://scipy-lectures.github.io/intro/matplotlib/matplotlib.html
* http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb
* http://tonysyu.github.com/mpltools/auto_examples/index.html#style-package
* http://stanford.edu/~mwaskom/software/seaborn/index.html
* http://mpld3.github.io/ (Matplotlib + D3.js)
** ``conda install matplotlib`` (:ref:`Conda` (:ref:`Anaconda`))


https://en.wikipedia.org/wiki/MayaVi

* https://github.com/enthought/mayavi
* https://scipy-lectures.github.io/packages/3d_plotting/index.html


http://bokeh.pydata.org/

* https://github.com/bokeh/bokeh

http://vispy.org/ (:ref:`OpenGL`)

* https://github.com/vispy/vispy

http://nbviewer.ipython.org/github/jakevdp/OpenVisConf2014/blob/master/PythonVis.ipynb

https://trifacta.github.io/vega/

* https://github.com/wrobstory/vincent

https://en.wikipedia.org/wiki/Plotly

* https://plot.ly/


https://en.wikipedia.org/wiki/D3.js

* http://d3js.org/

https://en.wikipedia.org/wiki/Three.js

* http://threejs.org/ (:ref:`WebGL`)

http://sigmajs.org/

http://www.pyqtgraph.org/ (:ref:`OpenGL`)

http://pandas.pydata.org/pandas-docs/stable/ecosystem.html#visualization

https://github.com/quantopian/qgrid (SlickGrid w/
:ref:`IPython Notebook`
(:ref:`Jupyter Notebook`))

https://github.com/josephmisiti/awesome-machine-learning

See: :ref:`Tools`, :ref:`Semantic Web Tools <semantic web tools>`,
:ref:`Art & Design <art-design>`


.. _datasets:
