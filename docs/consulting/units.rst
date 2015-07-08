

.. index:: Units
.. _units:

********
Units
********
| Wikipedia: https://en.wikipedia.org/wiki/Units_of_measurement
| Wikipedia: https://en.wikipedia.org/wiki/System_of_measurement


.. index:: RDF and Units
.. _rdf and units:

RDF and Units
**************
Units of measurement can be expressed with :ref:`RDF`,
:ref:`RDFS`, and :ref:`OWL`.

* :ref:`QUDT` defines :ref:`SI Units` and :ref:`Imperial Units`
  with :ref:`RDF` and :ref:`OWL`.


.. index:: CSVW and Units
.. _csvw and units:

CSVW and Units
++++++++++++++++
See: :ref:`CSVW`, :ref:`Tool Support for Units`


.. index:: Tool Support for Units
.. _tool support for units:

Tool Support for Units
***************************

Spreadsheet tools:

* Specify units in each column heading
  (e.g. ``"time [[s]]","speed [[m/s]]"``)
* Extra column per column for units
  (e.g. ``"time","time unit","speed","speed unit"``)
* :ref:`CSVW`: Columns have URIs, which are objects
  that can have subjects and predicates
  (for :ref:`XSD` types; metadata (author, date,
  ``rdfs:label "time"@en"``),
  and possibly units of measure)


Unit and/or precision-aware calculations:

* pypi:pint is a :ref:`Python` library for physical quantities
  which supports but does not require `NumPy`.

  | PyPI: https://pypi.python.org/pypi/pint
  | Src:  https://github.com/hgrecco/pint
  | Docs: https://pint.readthedocs.org/en/latest/


Storage formats:

* [ ] Spreadsheet formats do not have unit of measure support.
* :ref:`CSV` does not have unit of measure support.
* :ref:`JSON` does not have unit of measure support.
* :ref:`RDF` vocabularies support units of measure:

  * :ref:`CSVW` supports units of measure.
  * :ref:`JSON-LD` supports units of measure.


.. index:: Binary Prefixes
.. _binary prefixes:

Binary Prefixes
******************

.. table:: Table of Binary Prefixes (adapted from:
       https://en.wikipedia.org/wiki/Binary_prefix)
   :class: table-striped table-responsive

   +----------+------------+---------------------------+------------------------+-----------------------+
   | **Text** | **Symbol** | **Scalar (base 10)**      | **Scalar (base 1000)** | **Scalar (base 1e1)** |
   +----------+------------+---------------------------+------------------------+-----------------------+
   | kilo     | k          | 1000                      | 1000**1                | 1e3                   |
   +----------+------------+---------------------------+------------------------+-----------------------+
   | mega     | M          | 1000000                   | 1000**2                | 1e6                   |
   +----------+------------+---------------------------+------------------------+-----------------------+
   | giga     | G          | 1000000000                | 1000**3                | 1e9                   |
   +----------+------------+---------------------------+------------------------+-----------------------+
   | tera     | T          | 1000000000000             | 1000**4                | 1e12                  |
   +----------+------------+---------------------------+------------------------+-----------------------+
   | peta     | P          | 1000000000000000          | 1000**5                | 1e15                  |
   +----------+------------+---------------------------+------------------------+-----------------------+
   | exa      | E          | 1000000000000000000       | 1000**6                | 1e18                  |
   +----------+------------+---------------------------+------------------------+-----------------------+
   | zetta    | Z          | 1000000000000000000000    | 1000**7                | 1e21                  |
   +----------+------------+---------------------------+------------------------+-----------------------+
   | yotta    | Y          | 1000000000000000000000000 | 1000**8                | 1e24                  |
   +----------+------------+---------------------------+------------------------+-----------------------+

See also: :ref:`SI Prefixes`


.. index:: Metric System
.. _metric system:

Metric System
*************
| Wikipedia: https://en.wikipedia.org/wiki/Metric_system
| Wikipedia: https://en.wikipedia.org/wiki/Outline_of_the_metric_system


.. index:: SI Units
.. _si units:

SI Units
++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/International_System_of_Units
| Wikipedia: https://en.wikipedia.org/wiki/SI_base_unit
| Wikipedia: https://en.wikipedia.org/wiki/SI_derived_unit

SI Units (*International System of Units*) are the
standard units of measurement for almost every
country on Earth.

* https://en.wikipedia.org/wiki/SI_derived_unit#Derived_units_with_special_names
* https://en.wikipedia.org/wiki/SI_derived_unit#Examples_of_derived_quantities_and_units
* https://en.wikipedia.org/wiki/Non-SI_units_mentioned_in_the_SI
* :ref:`US Customary Units` do not yet specify :ref:`SI Units`
  because the USA has not yet converted to the :ref:`Metric system`.


.. index:: SI Base Units
.. _si base units:

SI Base Units
++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/International_System_of_Units#Base_units

* :ref:`metre`
* :ref:`kilogram`
* :ref:`second`
* :ref:`ampere`
* :ref:`kelvin`
* :ref:`mole`
* :ref:`candela`

.. index:: SI Prefixes
.. index:: Metric Prefixes
.. _si prefixes:

SI Prefixes
+++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Metric_prefix

.. table:: Table of SI Prefixes
       (adapted from:
        https://en.wikipedia.org/wiki/Template:Common_metric_prefixes
        and https://en.wikipedia.org/wiki/Binary_prefix)
    :class: table-striped table-responsive

    +----------+------------+---------------------------+------------------------+
    | **Text** | **Symbol** | **Scaling Factor**        | **Scaling Factor (e)** |
    +----------+------------+---------------------------+------------------------+
    | pico     | p          | 0.000000000001            | 1e-12                  |
    +----------+------------+---------------------------+------------------------+
    | nano     | n          | 0.000000001               | 1e-9                   |
    +----------+------------+---------------------------+------------------------+
    | micro    | μ          | 0.000001                  | 1e-6                   |
    +----------+------------+---------------------------+------------------------+
    | milli    | m          | 0.001                     | 1e-3                   |
    +----------+------------+---------------------------+------------------------+
    | centi    | c          | 0.01                      | 1e-2                   |
    +----------+------------+---------------------------+------------------------+
    | deci     | d          | 0.1                       | 1e-1                   |
    +----------+------------+---------------------------+------------------------+
    | (none)   | (none)     | 1                         | 1e0                    |
    +----------+------------+---------------------------+------------------------+
    | deca     | da         | 10                        | 1e1                    |
    +----------+------------+---------------------------+------------------------+
    | hecto    | h          | 100                       | 1e2                    |
    +----------+------------+---------------------------+------------------------+
    | kilo     | k          | 1000                      | 1e3                    |
    +----------+------------+---------------------------+------------------------+
    | mega     | M          | 1000000                   | 1e6                    |
    +----------+------------+---------------------------+------------------------+
    | giga     | G          | 1000000000                | 1e9                    |
    +----------+------------+---------------------------+------------------------+
    | tera     | T          | 1000000000000             | 1e12                   |
    +----------+------------+---------------------------+------------------------+
    | peta     | P          | 1000000000000000          | 1e15                   |
    +----------+------------+---------------------------+------------------------+
    | exa      | E          | 1000000000000000000       | 1e18                   |
    +----------+------------+---------------------------+------------------------+
    | zetta    | Z          | 1000000000000000000000    | 1e21                   |
    +----------+------------+---------------------------+------------------------+
    | yotta    | Y          | 1000000000000000000000000 | 1e24                   |
    +----------+------------+---------------------------+------------------------+


See also: :ref:`Binary Prefixes`


.. index:: SI Distance Units
.. _si distance units:

SI Distance Units
++++++++++++++++++++++++

.. index:: SI Meter
.. index:: Meter
.. index:: Metre
.. _metre:

metre
````````
| Wikipedia: https://en.wikipedia.org/wiki/Metre
| Wikipedia: https://en.wikipedia.org/wiki/Meter
| Abbr: ``m``

    The metre is the length of the path travelled by light in vacuum
    during a time interval of 1/299792458 of a second


.. index:: SI Volume Units
.. _si fluid units:

SI Volume Units
++++++++++++++++++++++++

.. index:: SI Litre
.. index:: Liter
.. index:: Litre
.. _litre:

litre
``````
| Wikipedia: https://en.wikipedia.org/wiki/Litre
| Abbr: ``L``

* Conversion: 1 :ref:`litre` == ``10e−3 m**3`` (:ref:`metres <metre>` cubed)
* Conversion: 1 :ref:`litre` == 0.2641720523 US :ref:`gallon` (~ 1/4)


.. index:: SI Mass Units
.. _si mass units:

SI Mass Units
++++++++++++++++++++++++

.. index:: SI Kilogram
.. index:: Kilogram
.. _kilogram:

kilogram
```````````
| Wikipedia: https://en.wikipedia.org/wiki/Kilogram

* A :ref:`kilogram` is the mass of TODO
* :ref:`gram` is defined in terms of a :ref:`kilogram`


.. index:: SI Gram
.. index:: Gram
.. _g:

======
gram
======
| Wikipedia: https://en.wikipedia.org/wiki/Gram
| Abbr: ``g``

* Conversion: 1 :ref:`g` == 1/28 :ref:`oz`
* Conversion: 1 :ref:`g` == 1/1000 kilo- :ref:`gram`


.. index:: SI Time Units
.. _si time units:

SI Time Units
++++++++++++++++

.. index:: SI Second
.. index:: Second
.. _second:

second
````````
| Wikipedia: https://en.wikipedia.org/wiki/Second #TODO
| Abbr: ``sec``
| Abbr: ``s``



.. index:: Microsecond
.. _microsecond:

=============
microsecond
=============
| Wikipedia: https://en.wikipedia.org/wiki/Microsecond #TODO
| Abbr: TODO

* Conversion: 1 :ref:`microsecond` == 1/100000 TODO of a :ref:`second`
* Conversion: 1 :ref:`microsecond` == 1e-1000 TODO :ref:`seconds <second>`


.. index:: Millisecond
.. _millisecond:

=============
millisecond
=============
| Wikipedia: https://en.wikipedia.org/wiki/Millisecond #TODO
| Abbr: ``ms``

* Conversion: 1 :ref:`millisecond` == 1/1000 of a :ref:`second`
* Conversion: 1 :ref:`millisecond` == 1e-3 :ref:`seconds <second>`


.. index:: SI Minute
.. index:: Minute
.. _minute:

========
minute
========
| Wikipedia: https://en.wikipedia.org/wiki/Minute
| Abbr: ``min``
| Abbr: ``m``

* Conversion: 1 :ref:`minute` == 60 :ref:`seconds <second>`


.. index:: Hour
.. _hour:

======
hour
======
| Wikipedia: https://en.wikipedia.org/wiki/Hour
| Abbr: ``hr``
| Abbr: ``hrs``
| Abbr: ``h``

* Conversion: 1 :ref:`hour` == 60 :ref:`minutes <minute>`
* Conversion: 1 :ref:`hour` == 3600 :ref:`seconds <second>`


.. index:: Day
.. _day:

=====
day
=====
| Wikipedia: https://en.wikipedia.org/wiki/Day
| Abbr: ``d``

* Conversion: 1 :ref:`day` == 24 :ref:`hours <hour>`
* Conversion: 1 :ref:`day` == 1440 :ref:`minutes <minute>`
* Conversion: 1 :ref:`day` == 86400 :ref:`seconds <second>`
* Rotational definition: 1 :ref:`day` == one complete planetary rotation


.. index:: Week
.. _week:

======
week
======
| Wikipedia: https://en.wikipedia.org/wiki/Week
| Abbr: ``wk``
| Abbr: ``wks``
| Abbr: ``w``

* Conversion: 1 :ref:`week` == 7 :ref:`days <day>`
* Conversion: 1 :ref:`week` == 168 :ref:`hours <hour>`
* Conversion: 1 :ref:`week` == 10080 :ref:`minutes <minute>`
* Conversion: 1 :ref:`week` == 604800 :ref:`seconds <second>`


.. index:: month
.. _month:

=======
month
=======
| Wikipedia: https://en.wikipedia.org/wiki/Month
| Abbr: ``mon``
| Abbr: ``mons``
| Abbr: ``m``

* A month contains either 28 (Feb; 29 on a leap year),
  30, or 31 :ref:`days <day>`.
* https://en.wikipedia.org/wiki/Thirty_days_hath_September
* Two hands of knuckles with peaks and valleys together:

  * start with an outside knuckle
  * up (peak; knuckle) -- 31 days
  * down (peak; knuckle) -- 30 day (except for February, which has 28/29)


.. index:: year
.. _year:

======
year
======
| Wikipedia: https://en.wikipedia.org/wiki/Year
| Abbr: ``yr``
| Abbr: ``yrs``
| Abbr: ``y``

* Conversion: 1 :ref:`year` == 365.25 :ref:`days <day>` (*1 leap day*/4.0)
* Conversion: 1 :ref:`year` == 365 :ref:`days <day>`
* Conversion: 1 :ref:`year` == 8760 :ref:`hours <hour>`
* Conversion: 1 :ref:`year` == 525600 :ref:`minutes <minute>`
* Conversion: 1 :ref:`year` == 31536000 :ref:`seconds <second>`
* Rotational definition: 1 :ref:`year` == 1 complete revolution around
  our singular planetary star: *the sun*.


.. index:: SI Frequency Units
.. _si frequency units:

SI Frequency Units
++++++++++++++++++++

.. index:: Hertz
.. index:: Hz
.. _hz:

hertz
``````
| Wikipedia: https://en.wikipedia.org/wiki/Hertz
| Abbr: ``Hz``

* TODO: cycles per time
* TODO: em.py


.. index:: SI Electric Current Units
.. _si electric current units:

SI Electric Current Units
++++++++++++++++++++++++++++

.. index:: Ampere
.. index:: Amps
.. _ampere:

ampere
````````
| Wikipedia: https://en.wikipedia.org/wiki/Ampere
| Abbr: ``A``  # TODO
| Abbr: ``amp``

# TODO

.. index:: Volt
.. _volt:

volt
`````
| Wikipedia: https://en.wikipedia.org/wiki/Volt

| Abbr: ``V``  # TODO

# TODO frequency / current relation


.. index:: SI Power Units
.. _si power units:

SI Power Units
++++++++++++++++

.. index:: Joule
.. _joule:

joule
```````
| Wikipedia: https://en.wikipedia.org/wiki/Joule


.. index:: Watt
.. _watt:

watt
``````
| Wikipedia: https://en.wikipedia.org/wiki/Watt


.. index:: SI Temperature Units
.. _si temperature units:

SI Temperature Units
+++++++++++++++++++++++

.. index:: Celsius
.. _celsius:

celsius
`````````
| Wikipedia: https://en.wikipedia.org/wiki/Celsius
| Abbr: ``C``

* Water (H2O) freezes at 0 degrees :ref:`celsius`.
* Water (H20) boils at 100 degrees :ref:`celsius`.
* [ ] celsius / :ref:`kelvin` relation


.. index:: Kelvin
.. _kelvin:

kelvin
````````
| Wikipedia: https://en.wikipedia.org/wiki/Kelvin
| Abbr: ``K``


.. index:: SI Amount Units
.. _si amount units:

SI Amount Units
+++++++++++++++++


.. index:: Mole
.. _mole:

mole
`````
| Wikipedia: `<https://en.wikipedia.org/wiki/Mole_(unit)>`__
| Abbr: ``mol``


.. index:: SI Luminous Intensity Units
.. _si luminous intensity units:

SI Luminous Intensity Units
+++++++++++++++++++++++++++++

.. index:: Candela
.. _candela:

candela
`````````
| Wikipedia: https://en.wikipedia.org/wiki/Candela
| Abbr: ``cd``


.. index:: SI Data Units
.. _si data units:

SI Data Units
++++++++++++++++

.. index:: SI Bit
.. index:: Bit
.. _bit:

bit
`````
| Wikipedia: https://en.wikipedia.org/wiki/Bit
| Abbr: ``b``

A bit can be ``1`` or ``0``.

* A bit may indicate *set containment* (e.g. ``True`` or ``False``,
  ``Black`` or ``White``) [:ref:`set-theory`]
* A bit may be part of an ordered set of bits
  which ascribe left-to-right (*little endian*)
  or right-to-left (*big endian*)
  place values to each binary digit:

  ::

      1 2 4 8   # little endian
      0 1 0 1   # == 0 + 2 + 0 + 8 == 9 (base 10)

      8 4 2 1   # big endian
      0 1 0 1   # == 0 + 4 + 0 + 1 == 5 (base 10)

* See also: :ref:`information-theory` > Shannon bit (*Shannon entropy*)


.. index:: SI Byte
.. index:: Byte
.. _byte:

byte
``````
| Wikipedia: https://en.wikipedia.org/wiki/Byte
| Abbr: ``B``

* Conversion: 1 :ref:`byte` == 8 :ref:`bits <bit>`
* Storage vendors use *powers of ten*
  (e.g. MB, GB, TB) to describe storage capacity;
  and also binary prefixes (kilo, mega, giga, tera, peta, exa, zetta).
* Many/most software programs use *powers of two*
  and binary prefixes
  (e.g. MiB, GiB, TiB) to describe e.g. partition and file sizes.
* On-disk file sizes are often larger than
  the file content because of file allocation tables,
  redundancy, block size and allocation;
  but may be smaller after compression/deduplication.

.. table:: Table of Bytes and Binary Prefixes
    :class: table-striped table-responsive

    +----------------+---------------+----------------------------------------+
    | unit           | derivation    | value                                  |
    +----------------+---------------+----------------------------------------+
    | nibble         | 2**2 bits     | 4 bits                                 |
    +----------------+---------------+----------------------------------------+
    | byte           | 2**3 bits     | 8 bits                                 |
    +----------------+---------------+----------------------------------------+
    | octet          | 2**3 bits     | 8 bits                                 |
    +----------------+---------------+----------------------------------------+
    | word size      | :ref:`CPU`    | 8+, 16, 24, 32, 64 bits                |
    |                |               |                                        |
    |                | register      |                                        |
    |                | width         | 32 bits (:ref:`x86`, :ref:`ARM`)       |
    |                |               |                                        |
    |                | (in bits)     | 64 bits (:ref:`x86_64`, :ref:`ARM` 64) |
    +----------------+---------------+----------------------------------------+
    | kibibyte (KiB) | 2**10 bytes   | 1024 bytes                             |
    |                |               |                                        |
    |                | 1024**1 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | kiloyte (KB)   | 1e3 bytes     | 1000 bytes                             |
    |                |               |                                        |
    |                | 1000**1 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | mebibyte (MiB) | 2**20 bytes   | 1048576 bytes                          |
    |                |               |                                        |
    |                | 1024**2 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | megabyte (MB)  | 1e6 bytes     | 1000000 bytes                          |
    |                |               |                                        |
    |                | 1000**2 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | gibibyte (GiB) | 2**30 bytes   | 1073741824 bytes                       |
    |                |               |                                        |
    |                | 1024**3 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | gigabyte (GB)  | 1e9 bytes     | 1000000000 bytes                       |
    |                |               |                                        |
    |                | 1000**3 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | tebibyte (TiB) | 2**40 bytes   | 1099511627776 bytes                    |
    |                |               |                                        |
    |                | 1024**4 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | terabyte (TB)  | 1e12 bytes    | 1000000000000 bytes                    |
    |                |               |                                        |
    |                | 1000**4 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | pebibyte (PiB) | 2**50 bytes   | 1125899906842624 bytes                 |
    |                |               |                                        |
    |                | 1024**5 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | petabyte (PB)  | 1e15 bytes    | 1000000000000000 bytes                 |
    |                |               |                                        |
    |                | 1000**5 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | exbibyte (EiB) | 2**60 bytes   | 1152921504606846976 bytes              |
    |                |               |                                        |
    |                | 1024**6 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | exabyte (EB)   | 1e18 bytes    | 1000000000000000000 bytes              |
    |                |               |                                        |
    |                | 1000**6 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | zebibyte (ZiB) | 2**70 bytes   | 1180591620717411303424 bytes           |
    |                |               |                                        |
    |                | 1024**7 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | zettabyte (ZB) | 1e21 bytes    | 1000000000000000000000 bytes           |
    |                |               |                                        |
    |                | 1000**7 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | yobibyte (YiB) | 2**80 bytes   | 1208925819614629174706176 bytes        |
    |                |               |                                        |
    |                | 1024**8 bytes |                                        |
    +----------------+---------------+----------------------------------------+
    | yottabyte (YB) | 1e21 bytes    | 1000000000000000000000000 bytes        |
    |                |               |                                        |
    |                | 1000**8 bytes |                                        |
    +----------------+---------------+----------------------------------------+


.. index:: Imperial Units
.. _imperial units:

Imperial units
****************
| Wikipedia: https://en.wikipedia.org/wiki/Imperial_units
| Wikipedia: https://en.wikipedia.org/wiki/English_units

Imperial units may refer to either *English units* (ended in 1824)
or :ref:`US customary units` (e.g. gram, ounce, gallon, pound, foot, mile).

* The UK (*United Kingdom*) (of which England is a part)
  now specifies the :ref:`Metric system` of :ref:`SI units`.
* The USA (*United States of America*)
  :ref:`US customary units` still include
  many :ref:`imperial units`;
  though :ref:`science` disciplines outside of
  food, transportation, and weather
  do now specify the :ref:`Metric system` of :ref:`SI units`.


.. index:: Imperial Distance Units
.. _imperial distance units:

Imperial Distance Units
+++++++++++++++++++++++++

.. index:: Inch
.. _inch:

inch
`````
| Wikipedia: https://en.wikipedia.org/wiki/Inch
| Abbr: ``in``

* Conversion: 1 :ref:`inch` ~== 2.54 `cm` (centi- :ref:`meters <metre>`)


.. index:: Foot
.. _foot:

=====
foot
=====
| Wikipedia: https://en.wikipedia.org/wiki/Foot
| Abbr: ``ft``

* Conversion: 1 :ref:`foot` == 12 :ref:`inches <inch>`


.. index:: Yard
.. _yard:

======
yard
======
| Wikipedia: https://en.wikipedia.org/wiki/Foot
| Abbr: ``yd``

* Conversion: 1 :ref:`yard` == 3 :ref:`feet <foot>`


.. index:: Mile
.. _mile:

======
mile
======
| Wikipedia: https://en.wikipedia.org/wiki/Mile
| Abbr: ``mi``
| Abbr: ``m``

* Conversion 1 :ref:`mile` == 1760 :ref:`yards <yard>`
* Conversion: 1 :ref:`mile` == 5280 :ref:`feet <foot>`
* Conversion: 1 :ref:`mile` == 63360 :ref:`inches <inch>`


.. index:: Imperial Volume Units
.. _imperial volume units:

Imperial Volume Units
++++++++++++++++++++++

.. index:: teaspoon
.. _teaspoon:

teaspoon
``````````
| Wikipedia: https://en.wikipedia.org/wiki/Teaspoon
| Abbr: ``t``
| Abbr: ``tsp.``

* Conversion: 1 US :ref:`teaspoon` == 1/3 of a US :ref:`tablespoon`
* Conversion: 1 US :ref:`teaspoon` == 1/6 US :ref:`fl oz`
* Conversion: 1 US :ref:`teaspoon` == 1 1/3 US :ref:`drams <dram>`
* Conversion: 1 US :ref:`teaspoon` == 4.92892159375 mL
  (milli- :ref:`Litres <litre>`)


.. index:: dram
.. _dram:

dram
``````
| Wikipedia: `<https://en.wikipedia.org/wiki/Dram_(unit)>`__

* Conversion: 1 US :ref:`dram` == 1/8 US :ref:`fl oz`
* Conversion: 1 US :ref:`dram` == 3/4 US :ref:`teaspoon`


.. index:: tablespoon
.. _tablespoon:

tablespoon
``````````
| Wikipedia: https://en.wikipedia.org/wiki/Tablespoon
| Abbr: ``T``
| Abbr: ``Tbsp.``

* Conversion: 1 US :ref:`tablespoon` == 1/6 US :ref:`fl oz`


.. index:: cup
.. _cup:

cup
````
| Wikipedia: `<https://en.wikipedia.org/wiki/Cup_(unit)>`__
| Abbr: ``c``

* Metric cup:
  `<https://en.wikipedia.org/wiki/Cup_(unit)#Metric_cup>`__
* US customary cup:
  `<https://en.wikipedia.org/wiki/Cup_(unit)#United_States_customary_cup>`__
* US legal cup (*serving size*):
  `<https://en.wikipedia.org/wiki/Cup_(unit)#United_States_.22legal.22_cup>`__
* UK cup:
  `<https://en.wikipedia.org/wiki/Cup_(unit)#UK_cup>`__
* Ja cup:
  `<https://en.wikipedia.org/wiki/Cup_(unit)#Japanese_cup>`__
* Gō cup:
  `<https://en.wikipedia.org/wiki/Cup_(unit)#Gō>`__

* Conversion: 1 US customary :ref:`cup` == 8 US :ref:`fl oz`
* Conversion: 1 US legal :ref:`cup` == 8.12 US :ref:`fl oz`
* Conversion: 1 Metric :ref:`cup` == 8.45 US :ref:`fl oz`


.. index:: Fluid Ounce
.. _fl oz:

fluid ounce
```````````
| Wikipedia: https://en.wikipedia.org/wiki/Fluid_ounce
| Abbr: ``fl oz``
| Abbr: ``oz``

* Serving size: 1 US can of e.g. soda == 12 US :ref:`fl oz`
* Conversion: 1 :ref:`fl oz` == 29.573 mL



.. index:: Pint
.. _pint:

pint
``````
| Wikipedia: https://en.wikipedia.org/wiki/Pint
| Abbr: ``pt``

* Conversion: 1 US :ref:`pint` == 16 US :ref:`fl oz`
* Conversion: 1 Imperial :ref:`pint` == 1.2009499255 US :ref:`pints <pint>`
* Conversion: 1 US :ref:`pint` = 0.85936700738 Imperial :ref:`pints <pint>`


.. index:: Quart
.. _quart:

quart
```````
| Wikipedia: https://en.wikipedia.org/wiki/Quart
| Abbr: ``qt``

* Conversion: 1 US liquid :ref:`quart` == 32 :ref:`fl oz`
* Conversion: 1 :ref:`quart` == 4 :ref:`cups <cup>`
* Conversion: 1 :ref:`quart` == 2 :ref:`pints <pint>`
* Conversion: 1 :ref:`quart` == 1/4 :ref:`gallon`
* Conversion: 1 US liquid quart == 0.946352946 :ref:`litres <litre>`


.. index:: Gallon
.. _gallon:

gallon
```````
| Wikipedia: https://en.wikipedia.org/wiki/Gallon
| Abbr: ``gal``

* Conversion: 1 :ref:`gallon` == 128 :ref:`oz <fl oz>`
* Conversion: 1 :ref:`gallon` == 8 :ref:`pints <pint>`


.. index:: Keg
.. _keg:

keg
`````
| Wikipedia: https://en.wikipedia.org/wiki/Keg

* Conversion: 1 :ref:`keg` == 124 US :ref:`pints <pint>`
* Conversion: 1 :ref:`keg` == 1984 US :ref:`fl oz`


.. index:: Imperial Mass Units
.. _imperial mass units:

Imperial Mass Units
++++++++++++++++++++++

.. index:: Gram
.. _gram:

gram
``````
| Wikipedia: https://en.wikipedia.org/wiki/Gram
| Abbr: ``g``


.. index:: Ounce
.. _oz:

ounce
```````
| Wikipedia: https://en.wikipedia.org/wiki/Ounce
| Abbr: ``oz``


.. index:: Pound
.. _lb:

pound
```````
| Wikipedia: https://en.wikipedia.org/wiki/Pound
| Abbr: ``lb``
| Abbr: ``lbm``

* Conversion: 1 :ref:`lb` == 16 :ref:`ounces <ounce>`
* Conversion: 1 :ref:`lb` == 448 :ref:`grams <gram>`
* Conversion: 1 :ref:`lb` == 0.45359237 kg (kilo- :ref:`grams <gram>`)


.. index:: Ton
.. _ton:

ton
`````
| Wikipedia: https://en.wikipedia.org/wiki/Ton

* Conversion: 1 :ref:`ton` == 2000 :ref:`pounds <lb>`
* Conversion: 1 kilo- :ref:`ton` == 1000 :ref:`tons <ton>`
* Colloqial: *half ton truck* refers to a
  minimum towing or hauling capacity;
  not the curb weight of a vehicle.
* Conversion: 1 *tonne* (*metric ton*) == 1000 kg == 2204 :ref:`lb`
* Conversion: 1 *long ton* == 2240 :ref:`lb`
* Conversion: 1 *short ton* == 2000 :ref:`lb`


.. index:: US customary units
.. _us customary units:

US customary units
********************
| Wikipedia: https://en.wikipedia.org/wiki/United_States_customary_units

Common US Fluid Conversions:

* Fluid serving size: 8 :ref:`fl oz`
* 1 :ref:`pint` = 16 :ref:`fl oz`
* 1 :ref:`gallon` = 128 :ref:`fl oz`
* 1 :ref:`keg` = 124 US :ref:`pints <pint>`


.. index:: Industry Units
.. _industry units:

Industry Units
*****************

Freight
++++++++
* US: :ref:`lb`, :ref:`ton`, cubic :ref:`inches <inch>`, :ref:`mile`,
  :ref:`second`
* World: :ref:`g`, cubic :ref:`metres <metre>` (:ref:`litre`),
  :ref:`metre`, :ref:`second`

Fuel
+++++
* US: :ref:`gallon`
* World: :ref:`litre`
