
.. index:: Computer Engineering
.. _computer-engineering:

*********************
Computer Engineering
*********************
| Wikipedia: https://en.wikipedia.org/wiki/Computer_engineering

Computer engineering combines, traditionally, electrical engineering
and :ref:`computer-science`.

* Computers are made of components with inputs, outputs, and logic tables.
* Computer programs may or may not be verified using formal methods.
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
* Some GPUs support :ref:`CUDA`.
* Some GPUs support :ref:`PhysX`.


.. index:: CUDA
.. _cuda:

CUDA
~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/CUDA
| Homepage: http://www.nvidia.com/object/cuda_home_new.html

CUDA (*Compute Unified Device Architecture*) is an API for
:ref:`GPUs <gpu>`.

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

PhysX is a realtime physics engine for :ref:`GPUs <gpu>` by Nvidia.


Video Card
=============
| Wikipedia: https://en.wikipedia.org/wiki/Video_card

A video card connects a :ref:`system bus` with a monitor
through one or more display connectors
and does computer graphics processing.

* A computer may have zero or more video cards.
* A video card contains a :ref:`gpu`.


.. index:: VGA
.. _vga:

VGA
----
| Wikipedia: https://en.wikipedia.org/wiki/Video_graphics_array
| Wikipedia: https://en.wikipedia.org/wiki/VGA_connector

VGA (*Video Graphics Array*) is a video display interface.

* VGA connectors are often *blue*.
* VGA connectors are 15-pin and trapezoidal
* VGA predates :ref:`DVI` and :ref:`HDMI`
* There are :ref:`VGA` to :ref:`DVI` and/or :ref:`HDMI` adapters.


.. index:: DVI
.. _dvi:

DVI
-----
| Wikipedia: https://en.wikipedia.org/wiki/Digital_Visual_Interface
| Wikipedia: https://en.wikipedia.org/wiki/Digital_Visual_Interface#Connector

DVI is a video display interface.

* DVI connectors are often *white*.
* There are a number of different DVI connectors;
  as well as Mini-DVI and Micro-DVI connectors.


.. index:: HDMI
.. _hdmi:

HDMI
-----
| Wikipedia: https://en.wikipedia.org/wiki/HDMI
| Wikipedia: https://en.wikipedia.org/wiki/HDMI#Connectors

HDMI (*High-Definition Multimedia Interface*) is an audio/visual 
interface standard.

* HDMI cables carry audio and video over the same cable.
* There are 5 types of HDMI connectors:

  * Type A -- classic 19-pin HDMI
  * Type B -- 29-pin HDMI
  * Type C -- "Mini HDMI"  (mini- HDMI Type A)
  * Type D -- "Micro HDMI" (looks like micro-:ref:`USB`)
  * Type E -- automotive locking tab

* HDMI can also carry :ref:`ethernet` signals.






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
  (see :ref:`USB Type-C`)

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
* USB 3.0 Type B -- USB 3.0 Type A + extra block of pins on the top 
* :ref:`USB Type-C`

USB Buses

* USB -- 12 mbps
* USB 2.0 -- 480 Mbps
* USB 3.0 -- 5000 Mbps (5 Gbps) (5 :ref:`gigabit`)
* USB 3.1 -- 10000 Mbps (10 Gbps) (10 :ref:`gigabit`)
* :ref:`USB Type-C` (USB 3.1; 10 GBps)


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
PATA, ATA (*Parallel ATA* (*AT Attachment*)) is a 40-pin
drive interface standard
based on :ref:`IDE`, ATA and ATAPI.

* :ref:`SATA` (*Serial ATA*) is derived from :ref:`PATA` (*Parallel ATA*).
* Newer drives have :ref:`USB`, :ref:`SATA`, or :ref:`eSATA` connectors



.. index:: System Bus
.. _system bus:

System Bus
============

`<https://en.wikipedia.org/wiki/Bus_(computing)>`__

.. index:: ISA
.. _isa:

ISA
----
| Wikipedia: https://en.wikipedia.org/wiki/Industry_Standard_Architecture


.. index:: AGP
.. _agp:

AGP
----
| Wikipedia: https://en.wikipedia.org/wiki/Accelerated_Graphics_Port


.. index:: PCI
.. _pci:

PCI
----
| Wikipedia: https://en.wikipedia.org/wiki/Conventional_PCI


.. index:: PCI-e
.. _pci-e:

PCI-e
-------
| Wikipedia: https://en.wikipedia.org/wiki/PCI_Express


.. index:: PCMCIA
.. _pcmcia:

PCMCIA
--------
| Wikipedia: https://en.wikipedia.org/wiki/PC_Card

PCMCIA is a standard for smaller-form-factor expansion cards.

* PCMCIA is now known as "PC Card" and "CardBus".
* Some laptops have PCMCIA slots.
* There are PCI to PCMCIA adapter cards.


.. index:: ExpressCard
.. _expresscard:

ExpressCard
-------------
| Wikipedia: https://en.wikipedia.org/wiki/ExpressCard

* Some laptops have ExpressCard slots.
* ExpressCard supersedes the :ref:`PCMCIA` (PC Card, CardBus)
  standards for smaller-form-factor expansion cards.


.. index:: Network interfaces
.. _network interfaces:

Network Interfaces
====================

.. index:: Gigabit
.. _gigabit:

Gigabit
---------
A gigabit is 1000 Mbps (1000 megabits per second).

* :ref:`1000BASE-T`, :ref:`10GBASE-T`, and :ref:`40GBASE-T`
  can all handle gigabit speeds.
* Wireless routers before :ref:`802.11ac <802.11>` 
  are not fast enough to handle gigabit speeds.


.. index:: NIC
.. nic:

NIC
-----
A NIC (*Network Interface Card*) is a card
that plugs into a :ref:`system bus`
which interfaces with a wired network.



.. index:: Ethernet
.. _ethernet:

Ethernet
----------
| Wikipedia: https://en.wikipedia.org/wiki/Ethernet_over_twisted_pair


.. index:: CAT-5
.. index:: CAT-5e
.. _cat-5:

CAT-5
~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Category_5_cable

A CAT-5 (*Category 5*) cable is an :ref:`ethernet` cable.

* CAT-5 can carry :ref:`10base-t`, :ref:`100base-t`,
  or :ref:`1000base-t`
* CAT-5e is the newer CAT-5 standard.
* A cable installer uses a *crimper tool* to *crimp*
  connectors ("*terminators*")
  to the end of a :ref:`CAT-5` or :ref:`CAT-6` cable.


.. index:: CAT-6
.. _cat-6:

CAT-6
~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Category_6_cable

A CAT-6 (*Category 6*) cable is an :ref:`ethernet` cable

* CAT-5 can carry :ref:`10base-t`, :ref:`100base-t`,
  :ref:`1000base-t`, :ref:`10gbase-t`, 


.. index:: 10BASE-T
.. _10base-t:

10BASE-T
~~~~~~~~~~
10Base-T is a 10 Mbps :ref:`ethernet` standard.


.. index:: 100Base-T
.. _100base-t:

100BASE-T
~~~~~~~~~~~~~~
100BASE-T is a 100 Mbps :ref:`ethernet` standard.

* 100BASE-T is backward-compatible with 10BASE-T
  (some cards will say 10/100, or 10/100/1000)

.. index:: 1000BASE-T
.. _1000base-t:

1000BASE-T
~~~~~~~~~~~
1000BASE-T is a 1000 Mbps (1 Gbps; 1 **gigabit**) :ref:`ethernet` standard.

* 100BASE-T is backward-compatible with 10BASE-T
  (some cards will say 10/100, or 10/100/1000)


.. index:: 10GBASE-T
.. _10gbase-t:

10GBASE-T
~~~~~~~~~~~
10GBASE-T is a 10000 Mbps (10 Gbps) :ref:`ethernet` standard.


.. index:: 40GBASE-T
.. _40gbase-t:

40GBASE-T
~~~~~~~~~~~~~~~~~~~~~
10GBASE-T is a 40000 Mbps (40 Gbps) :ref:`ethernet` standard.


.. index:: Wireless
.. _wireless:

Wireless
----------

.. index:: 802.11
.. _802.11:

802.11
~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/IEEE_802.11

IEEE 802.11 is a group of standards for wireless networking.

  IEEE 802.11 is a set of media access control (MAC)
  and physical layer (PHY) specifications for
  implementing wireless local area network (WLAN)
  computer communication in the 2.4, 3.6, 5, and 60 GHz frequency bands.

802.11 "WiFi" standards:

* 802.11b -- 2.4 GHz -- 11 Mbps
* 802.11g -- 2.4 GHz -- 54 Mbps
* 802.11a -- 5 GHz -- 54 Mbp/s
* 802.11n -- 2.4 GHz, 5 GHz -- 600 Mbps (MIMO)
* 802.11ac -- 2.4 GHz, 5 GHz -- 1300 Mbps (MIMO)
* 802.11ad -- 60 GHz -- 7000 Mbps ("WiGig")
* 802.11ax -- 2.4 GHZ, 5 GHZ -- ~4x 802.11ac [ Draft ]
* 802.11ay -- 60 Ghz -- 100000 Mbps (100 Gbps) [ Draft ]

802.11 standards:

* 802.11s -- wireless mesh networking


.. index:: Mesh Wireless
.. index:: Wireless mesh network
.. _wireless mesh network:

Wireless mesh network
~~~~~~~~~~~~~~~~~~~~~~
| https://en.wikipedia.org/wiki/Wireless_mesh_network

Wireless mesh networks route connections between nodes.

* Wireless mesh networks do not require APs.
* Wireless mesh networks are designed to be resilient to and tolerant of
  network failure.
* Wireless mesh networks require ingress and egress points
  in order to route with the wider internet.

Mesh Wireless Approaches:

* OLPC (*One-laptop per child*) laptops support IEEE 802.11s 
  mesh networking with standard 802.11b/g wireless cards.

  http://wiki.laptop.org/go/Mesh_Network_Details

* Redstone Technologies LLC (:ref:`gigabit` wireless mesh networks)

  http://redstone.us.com/simplified-wireless-architecture/


.. index:: Mobile Broadband
.. _mobile broadband:

Mobile Broadband
-----------------
| https://en.wikipedia.org/wiki/Mobile_broadband


.. index:: 3G
.. _3g:

3G
~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/3G


.. index:: 4G
.. _4g:

4G
~~~~
| Wikipedia: https://en.wikipedia.org/wiki/4G

* :ref:`LTE` is a :ref:`4G` wireless standard.


.. index:: 5G
.. _5g:

5G
~~~~
| Wikipedia: https://en.wikipedia.org/wiki/5G


.. index:: CDMA
.. _cdma:

CDMA
~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Code_division_multiple_access

* W-CDMA (*WCDMA*) is a :ref:`3G` wireless standard.


.. index:: GSM
.. _gsm:

GSM
~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/GSM 


.. index:: LTE
.. _lte:

LTE
~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/LTE_(telecommunication)

* Artemis pCell pWave LTE: http://www.artemis.com/pcell


.. index:: Fiber
.. _fiber:

Fiber
-------
| https://en.wikipedia.org/wiki/Fiber-optic_communication
| https://en.wikipedia.org/wiki/Optical_fiber

Optical fiber can carry photons near the speed of light.


.. index:: Fiber to the x
.. _fiber to the x:

Fiber to the x
~~~~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Fiber_to_the_x

The various fiber deployment strategies are somewhat undescriptively
all called "fiber to the x (*FTTX*)". 

* Fiber to the neighborhood
* Fiber to the premises
* Fiber to the home

Fiber is the way forward in *wireline* broadband networks:

* https://en.wikipedia.org/wiki/Fiber_to_the_premises_by_country
* https://en.wikipedia.org/wiki/Fiber_to_the_premises_in_the_United_States


.. index:: Fibre Channel
.. _fibre channel:

Fibre Channel
~~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Fibre_Channel

Fibre channel is an optical fiber networking technology.
