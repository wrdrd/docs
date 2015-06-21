
.. index:: Data Science
.. _data-science:

Data Science
=============
https://en.wikipedia.org/wiki/Data_science

| "The Open Source Data Science Masters"
| http://datasciencemasters.org/
|
| "Ten Simple Rules for Reproducible Computational Research"
| http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1003285


Data, Information, Knowledge, & Wisdom
------------------------------------------
https://en.wikipedia.org/wiki/Data

https://en.wikipedia.org/wiki/Information

https://en.wikipedia.org/wiki/Knowledge
(see: :ref:`knowledge-engineering`)

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
.. _data-science-theory:

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
  (:ref:`Web Standards <web-standards>`,
  :ref:`Semantic Web Standards <semantic-web-standards>`)
* https://en.wikipedia.org/wiki/Open_data

https://en.wikipedia.org/wiki/Peer_review

* https://en.wikipedia.org/wiki/Repeatability
* https://en.wikipedia.org/wiki/Reproducibility


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

https://en.wikipedia.org/wiki/Design_of_experiments

* https://en.wikipedia.org/wiki/Design_of_experiments#Discussion_topics_when_setting_up_an_experimental_design
* https://en.wikipedia.org/wiki/Repeatability
* https://en.wikipedia.org/wiki/Reproducibility

https://en.wikipedia.org/wiki/Meta-analysis

https://en.wikipedia.org/wiki/Systematic_review


.. index:: Math
.. index:: Mathematics
.. _math:

Math
+++++
https://en.wikipedia.org/wiki/Mathematics

https://en.wikipedia.org/wiki/Outline_of_mathematics

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
* :ref:`Information Theory <information-theory>`
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
.. _information-theory:

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
* https://github.com/ULAFF/notebooks/ (:ref:`IPython` notebooks)


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

See: :ref:`Knowledge Engineering <knowledge-engineering>`


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

Tools
-------
https://en.wikipedia.org/wiki/Scientific_workflow_system

https://github.com/josephmisiti/awesome-machine-learning


Techniques
--------------

Automated Workflows
++++++++++++++++++++
Standard, Automated Workflows

* :ref:`Scientific Method <scientific-method>`
* https://en.wikipedia.org/wiki/Repeatability
* https://en.wikipedia.org/wiki/Reproducibility
* https://en.wikipedia.org/wiki/Occam%27s_razor

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


See: :ref:`Knowledge Engineering <knowledge-engineering>`.


.. index:: Data Visualization
.. _data-visualization:

Data Visualization
++++++++++++++++++++
https://en.wikipedia.org/wiki/Data_visualization

* http://drewconway.com/zia/2013/3/26/the-data-science-venn-diagram
* http://datascienceassn.org/content/fourth-bubble-data-science-venn-diagram-social-sciences


.. index:: Data Visualization Tools
.. _data-visualization-tools:

Data Visualization Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~


https://en.wikipedia.org/wiki/Matplotlib

* http://scipy-lectures.github.io/intro/matplotlib/matplotlib.html
* http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb
* http://tonysyu.github.com/mpltools/auto_examples/index.html#style-package
* http://stanford.edu/~mwaskom/software/seaborn/index.html
* http://mpld3.github.io/ (Matplotlib + D3.js)


https://en.wikipedia.org/wiki/MayaVi

* https://github.com/enthought/mayavi
* https://scipy-lectures.github.io/packages/3d_plotting/index.html


http://bokeh.pydata.org/

* https://github.com/bokeh/bokeh

http://vispy.org/ (OpenGL)

* https://github.com/vispy/vispy

http://nbviewer.ipython.org/github/jakevdp/OpenVisConf2014/blob/master/PythonVis.ipynb

https://trifacta.github.io/vega/

* https://github.com/wrobstory/vincent

https://en.wikipedia.org/wiki/Plotly

* https://plot.ly/


https://en.wikipedia.org/wiki/D3.js

* http://d3js.org/

https://en.wikipedia.org/wiki/Three.js

* http://threejs.org/

http://sigmajs.org/

http://www.pyqtgraph.org/ (OpenGL)

http://pandas.pydata.org/pandas-docs/stable/ecosystem.html#visualization

https://github.com/quantopian/qgrid (SlickGrid w/ IPython Notebook (
Jupyter Notebook))

https://westurner.org/tools/

https://github.com/josephmisiti/awesome-machine-learning

See: :ref:`Semantic Web Tools <semantic-web-tools>`,
:ref:`Art & Design <art-design>`
