
.. index:: Computer Engineering
.. _computer-engineering:

*********************
Computer Engineering
*********************
| Wikipedia: https://en.wikipedia.org/wiki/Computer_engineering

Computer engineering combines, traditionally, eletrical engineering
and :ref:`computer-science`.

* Computers are made of components with inputs, outputs, and logic tables
* Computer programs may or may not verified using formal methods
* https://en.wikipedia.org/wiki/List_of_emerging_technologies#Electronics
* https://en.wikipedia.org/wiki/List_of_emerging_technologies#IT_and_communications


Processor
==========


.. index:: CPU
.. _cpu:

CPU
-----
| Wikipedia: https://en.wikipedia.org/wiki/Central_processing_unit

A CPU (*Central Processing Unit*) --- or **processor** ---
does variable logic according to
a set of gates
and input instructions.

* A computer has one or more CPUs.
* A CPU has one or more cores.
* A CPU has one or more internal (*L1*, *on-die*) or external (L2) caches.
* A CPU cache buffers addressed memory for CPU instructions.
* A CPU supports an instruction set.
* A CPU may be programmable with microcode.
* A CPU evaluates a stream of instructions (e.g. a *Turing Machine*).


.. index:: ARM
.. _arm:

ARM
~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/ARM_architecture

* Routers
* Smartphones
* Notebooks

  * Chromebooks

* Routers
* Servers


.. index:: PPC
.. _ppc:

PPC
~~~~~
| Wikipedia:  https://en.wikipedia.org/wiki/PowerPC

* https://en.wikipedia.org/wiki/PowerPC#Operating_systems
* `<https://en.wikipedia.org/wiki/Apple's_transition_to_Intel_processors>`__
  (2006)


.. index:: x86
.. _x86:

x86
~~~~~
| https://en.wikipedia.org/wiki/X86

x86 is 32-bit :ref:`CPU` architecture.

* A **PC** by a number of definitions

  * A PC is a computer with a
    :ref:`CPU` that runs :ref:`x86` or :ref:`x86_64` instructions.
  * A PC is a computer running :ref:`windows`

    * e.g. "Mac or PC? PC or Mac?"; where Mac = :ref:`OSX` on :ref:`x86_64`
      and PC = :ref:`Windows` on :ref:`x86` or :ref:`x86_64`;
      and :ref:`Linux` runs on anything.


.. index:: x86_64
.. _x86_64:

x86_64
~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/X86-64

x86_64 (*x64*, *AMD64*) is a 64-bit :ref:`CPU` architecture.

* amd64 is :ref:`x86_64`.
* In 2015, most new computers are either :ref:`x86_64` or :ref:`ARM`.



.. index:: GPU
.. _gpu:

GPU
----
| Wikipedia: https://en.wikipedia.org/wiki/Graphics_processing_unit

A GPU (*Graphics Processing Unit*)
does variable logic according to
a set of gates
and input instructions;
with massive parallelism.

* A computer has zero or more GPUs.
* A GPU may have internal :ref:`RAM`;
  or may use a portion of the system ram (as with many notebooks)
* A GPU is designed for parallel computation.
* GPUs were designed, in particular, for realtime :ref:`3d modeling`
  (vertex pixel shading, physics)
* GPUs have driven demand for faster :ref:`system bus standards <system bus>`.
* GPU-accelerated code is code that has been adapted for
  or just runs faster on a GPU.
* Many GPUs support GPU-accelerated :ref:`OpenGL`.


.. index:: CUDA
.. _cuda:

CUDA
~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/CUDA
| Homepage: http://www.nvidia.com/object/cuda_home_new.html

CUDA (*Compute Unified Device Architecture*) is an API for
:ref:`GPUs <gpu>`

CUDA-accelerated libraries for
:ref:`data-science`, :ref:`machine-learning`, :ref:`deep learning`:

  + Pylearn2 (Theano), Numba
  + Torch
  + cuBLAS (BLAS + CUDA = faster than Intel MKL)

    https://developer.nvidia.com/cuBLAS


.. index:: PhysX
.. _physx:

PhysX
~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/PhysX
| Homepage: https://developer.nvidia.com/gameworks-physx-overview

Physics is a realtime physics engine for :ref:`GPUs <gpu>` by Nvidia.



.. index:: Memory
.. _memory:

Memory
========
| Wikipedia: https://en.wikipedia.org/wiki/Computer_memory

* :ref:`RAM` -- live working area ("desktop", "workspace")
* :ref:`Persistent Storage` -- Hard Drive, CD/DVD, USB drive,
  SSD ("file cabinet")


.. index:: RAM
.. _ram:

RAM
----
| Wikipedia: https://en.wikipedia.org/wiki/Random-access_memory

RAM (*Random Access Memory*) is a category of
volatile storage technologies
which require voltage to remain applied in order to maintain state.

* RAM is hundreds of times faster than many/most other
  :ref:`Persistent Storage` methods.
* It takes seconds for the voltage from RAM to discharge.
* A *cold boot* or *cold reboot* is when the RAM gets a few seconds
  (sometimes 30 or more) to discharge. (**"the magic touch"**)


.. index:: Persistent Storage
.. _persistent storage:

Persistent Storage
-----------------------
Slowest -> Fastest:

* Punch cards
* Tape drives
* Disk drives (*floppy*: 8", 5.25", 3.5")
* :ref:`Disc drives` (*CD*, MiniDisc, *DVD*, *Blu-ray*, [3D-] optical storage)
* :ref:`Hard drives` (*HD*)
* :ref:`SSDs <SSD>`


.. index:: Hard drives
.. _hard drives:

Hard Drives
~~~~~~~~~~~~~
* 5400 RPM -- notebook (energy savings; see also :ref:`SSD`)
* 7200 RPM -- desktop, notebook
* 10000 RPM -- high end :ref:`SCSI` drives


.. index:: SSD
.. _ssd:

SSD
~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Solid-state_drive

An SSD (*Solid-State Drive*) is a binary data storage device
based on an integrated circuit that does
not require voltage to be applied to maintain state.

* SSDs are faster and (currently) more expensive than :ref:`hard drives`.
* SSDs are more energy efficient than :ref:`hard drives`.
* Notebooks and netbooks may include or be upgraded with an SSD.
* Servers benefit from SSDs for caching, fast reads, and fast writes.


.. index:: Disc Drives
.. _disc drives:

Disc Drives
~~~~~~~~~~~~
* *CD*
* *DVD*
* *Blu-ray*
* [3D-] optical storage



.. index:: Data Device Bus
.. _data device bus:

Data Device Bus
=================

`<https://en.wikipedia.org/wiki/Bus_(computing)>`__

.. index:: USB
.. _usb:

USB
-----
| Wikipedia: https://en.wikipedia.org/wiki/USB
| Wikipedia: https://en.wikipedia.org/wiki/USB_2.0
| Wikipedia: https://en.wikipedia.org/wiki/USB_3.0
| Wikipedia: https://en.wikipedia.org/wiki/USB_Type-C

USB (*Universal Serial Bus*) is a group of standards
for device interaction and one-way and two-way power and data transfer.

* Serial Bus -- a routed/bridged tree of connected devices
* USB Hub -- n-way splitter with two or more ports
* Powered USB Hub -- USB Hub which must be plugged in; can charge many devices
  (see also: USB Type-C)
*

USB Connectors

* USB Type A -- classic rectangular USB with pins on one side
* USB Type B -- square USB (e.g. some printers)
* Mini-USB -- now deprecated (see: Micro-USB)
* USB Mini-A -- (deprecated)
* USB Mini-B -- (deprecated)
* Micro-USB -- industry standard OMTP (2007), ITU (2009), EU (2010)

  * USB Micro-A -- rectangular
  * USB Micro-B -- trapezoidal
  * USB Micro-AB -- supports both Micro-A and Micro-B
  * USB OTG (*on-the-go*) -- (mobile) support for charging and hub
  * USB 3.0 Micro-B -- Micro-USB-B + *5 pins*
    (USB Micro-A cables work with USB 3.0 Micro-B connectors,
    but USB 3.0 Micro-B cables
    do not work with USB Micro-B connectors)

* USB 3.0 Type A -- classic rectangular USB with pins on one side
  (works with USB Type A)
* USB 3.0 Type B --
* USB Type-C -- *two-way charging*)

USB Buses

* USB -- mbps
* USB 2.0 -- mbps
* USB 3.0 -- mbps
* USB Type-C (two-way charge + data) -- mbps


.. index:: USB Type-C
.. _usb type-c:

USB Type-C
~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/USB_Type-C

* :ref:`Operating Systems`: Windows 10, OSX 10, Android M
* Adapters: DisplayPort, Thunderbolt, MHL
* USB Type-C as the primary charging interface:

  * Post-2015 MacBooks, Chromebook Pixel 2+

* Vendors with portable storage drives with USB Type-C connectors (2015):

  * LaCie, SanDisk


.. index:: Serial ATA
.. index:: SATA
.. _sata:

SATA
------
| Wikipedia: https://en.wikipedia.org/wiki/Serial_ATA
| Wikipedia: https://en.wikipedia.org/wiki/Serial_ATA#eSATA

SATA (*Serial* :ref:`ATA <pata>`) is a data device bus standard.

* SATA (1.5, 3.0, 6.0, 16 Gbit/s) is faster than 
  all current :ref:`USB` standards
  (USB 2.0, USB 3.0. USB 3.1 (:ref:`USB Type-C`)),
  :ref:`IDE <ide drive>`, and :ref:`ATA (PATA) <pata>`
* :ref:`eSATA` is SATA for external drives.

.. index:: eSATA
.. _esata:

eSATA
~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Serial_ATA#eSATA

eSATA (*External* :ref:`SATA`) works with
(powered, unpowered, portable) external drives.


.. index:: SCSI
.. _scsi:

SCSI
-------
| Wikipedia: https://en.wikipedia.org/wiki/SCSI
| DevPrefix: ``/dev/sg`` (CD/DVD)
| DevPrefix: ``/dev/sd`` (hardrive, USB)
| DevFS: ``/dev/scsi``

SCSI (*Small Computer System Interface*) is a set of standards
for device interaction and data interchange.

* Drives faster than 7200 RPM are often either :ref:`SCSI`
  or, now, :ref:`SATA` drives
* Some CD/DVD devices are :ref:`SCSI` devices
* :ref:`SATA` and :ref:`eSATA` devices
  register as SCSI devices
  with newer :ref:`Linux` kernels and distributions.


.. index:: IDE (drive interface)
.. _ide drive:

IDE
----
| Wikipedia: https://en.wikipedia.org/wiki/Parallel_ATA#IDE_and_ATA-1

IDE (*Integrated Drive Electronics*) is a cable connector
and drive interface standard which predates
(and is now part of) the :ref:`Parallel ATA <pata>` standards.

* Older storage devices may have a 40-pin :ref:`IDE <ide drive>` connector

  * Newer drives have :ref:`USB`, :ref:`SATA`, or :ref:`eSATA`
    connectors
    (which, like IDE, all also require the drive to handle its own
    storage logic)


.. index:: ATA
.. index:: PATA
.. index:: Parallel ATA
.. _pata:

PATA
----
PATA, ATA (*Parallel ATA* (*AT Attachment*)) is a drive interface standard
based on ATA and ATAPI.

* Older storage devices may have a 40-pin :ref:`IDE <ide drive>`
:ref:`ATA (PATA) <pata>` connector.

  * Newer drives have :ref:`USB`, :ref:`SATA`, or :ref:`eSATA` connectors

* :ref:`SATA` (*Serial ATA*) is derived from :ref:`PATA` (*Parallel ATA*).


.. index:: System Bus
.. _system bus:

System Bus
============

`<https://en.wikipedia.org/wiki/Bus_(computing)>`__

ISA
----
| Wikipedia: https://en.wikipedia.org/wiki/Industry_Standard_Architecture

AGP
----
| Wikipedia: https://en.wikipedia.org/wiki/Accelerated_Graphics_Port

PCI
----
| Wikipedia: https://en.wikipedia.org/wiki/Conventional_PCI

PCI-e
-------
| Wikipedia: https://en.wikipedia.org/wiki/PCI_Express


Video Card
=============
| Wikipedia: https://en.wikipedia.org/wiki/Video_card

See: :ref:`gpu`
