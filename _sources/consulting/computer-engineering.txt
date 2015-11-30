
.. index:: Computer Engineering
.. _computer engineering:

*********************
Computer Engineering
*********************
| Wikipedia: https://en.wikipedia.org/wiki/Computer_engineering

Computer engineering combines, traditionally, electrical engineering
and :ref:`computer science`.

* Computers are made of components with inputs, outputs, and logic tables.
* Computer programs may or may not be verified using formal methods.
* https://en.wikipedia.org/wiki/List_of_emerging_technologies#Electronics
* https://en.wikipedia.org/wiki/List_of_emerging_technologies#IT_and_communications


.. index:: Monitor
.. _monitor:

Monitor
==========
* Serial
* CRT
* LCD
* OLED
* Quantum Dots
* [ ] list of emerging technologies # ~display

todo: grep for todo,fixme,[ ]


.. index:: Northbridge
.. _northbridge:

Northbridge
=================
| Wikipedia: `<https://en.wikipedia.org/wiki/Northbridge_(computing)>`__

* Many/most desktops, laptops, and servers have a northbridge
  which connects many core system components.
* A :ref:`CPU` is connected to a northbridge.
* A :ref:`CPU` may be connected to a northbridge
  through a motherboard *processor socket*.
* A northbridge connects to :ref:`RAM`.
* A northbridge connects to a :ref:`System Bus` (e.g. :ref:`PCI-e`)
* A :ref:`southbridge` connects to a :ref:`northbridge`.


.. index:: Processor
.. _processor:

Processor
----------


.. index:: CPU
.. _cpu:

CPU
~~~~~
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

=====
ARM
=====
| Wikipedia: https://en.wikipedia.org/wiki/ARM_architecture

* Routers
* Smartphones
* Notebooks

  * Chromebooks

* Routers
* Servers


.. index:: PPC
.. _ppc:

=====
PPC
=====
| Wikipedia:  https://en.wikipedia.org/wiki/PowerPC

* https://en.wikipedia.org/wiki/PowerPC#Operating_systems
* `<https://en.wikipedia.org/wiki/Apple's_transition_to_Intel_processors>`__
  (2006)


.. index:: x86
.. _x86:

=====
x86
=====
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

========
x86_64
========
| Wikipedia: https://en.wikipedia.org/wiki/X86-64

x86_64 (*x64*, *AMD64*) is a 64-bit :ref:`CPU` architecture.

* amd64 is :ref:`x86_64`.
* In 2015, most new computers are either :ref:`x86_64` or :ref:`ARM`.




.. index:: Memory
.. _memory:

Memory
--------
| Wikipedia: https://en.wikipedia.org/wiki/Computer_memory

* :ref:`RAM` -- live working area ("desktop", "workspace")
* :ref:`Persistent Storage` -- Hard Drive, CD/DVD, USB drive,
  SSD ("file cabinet")


.. index:: RAM
.. _ram:

RAM
~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Random-access_memory

RAM (*Random Access Memory*) is a category of
volatile storage technologies
which require voltage to remain applied in order to maintain state.

* RAM is hundreds of times faster than many/most other
  :ref:`Persistent Storage` methods.
* It takes seconds for the voltage from RAM to discharge.
* A *cold boot* or *cold reboot* is when the RAM gets a few seconds
  (sometimes 30 or more) to discharge. (**"the magic touch"**)


.. index:: System Bus
.. _system bus:

System Bus
------------

`<https://en.wikipedia.org/wiki/Bus_(computing)>`__

.. index:: ISA
.. _isa:

ISA
~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Industry_Standard_Architecture


.. index:: PCI
.. _pci:

PCI
~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Conventional_PCI


.. index:: PCMCIA
.. _pcmcia:

PCMCIA
~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/PC_Card

PCMCIA is a standard for smaller-form-factor expansion cards.

* PCMCIA is now known as "PC Card" and "CardBus".
* Some laptops have PCMCIA slots.
* There are PCI to PCMCIA adapter cards.


.. index:: AGP
.. _agp:

AGP
~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Accelerated_Graphics_Port


.. index:: ExpressCard
.. _expresscard:

ExpressCard
~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/ExpressCard

* Some laptops have ExpressCard slots.
* ExpressCard supersedes the :ref:`PCMCIA` (PC Card, CardBus)
  standards for smaller-form-factor expansion cards.


.. index:: PCI-e
.. _pci-e:

PCI-e
~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/PCI_Express


.. index:: Video Card
.. _video card:


Video Card
-------------
| Wikipedia: https://en.wikipedia.org/wiki/Video_card

A video card connects a :ref:`system bus` with a monitor
through one or more display connectors
and does computer graphics processing.

* A computer may have zero or more video cards.
* A video card contains a :ref:`gpu`.
* Many/most video cards connect to the :ref:`system bus`
  (e.g. :ref:`AGP`, :ref:`PCI-e`).
* Some video cards connect over :ref:`USB`
  (e.g. for adding monitors to a notebook).


.. index:: Multiheaded Display
.. _multiheaded display:

Multiheaded Display
~~~~~~~~~~~~~~~~~~~~~~
| Docs: https://wiki.archlinux.org/index.php/Multihead
| Docs: https://wiki.ubuntu.com/X/Config/Multihead/

.. epigraph::

   Q: Why would I need more than one monitor?

   A: To multitask.

   A: For presentations. For presentations with
   multiple projectors and something like :ref:`Resolume`.

Per :ref:`video card` multi-headed display configurations:

* Synchronized, Mirroring --- Same output on multiple monitors
* Teamed, Seamed, Tiled --- One framebuffer which spans multiple monitors
* Multi-seat --- separate display/keyboard/mouse
  ("multi-user console server", *thin client server*, LTSP)

Challenges

* Window placement

  * Split screen
  * Tabbed
  * Stacked
  * Floating

* Keyboard shortcuts

  * move window_x to monitor 2
  * move window_x and ancillary floating windows to desktop 6
  * set monitor 2 to desktop 6
  * move this whole workspace to the monitor on the side
  * show window_x in fullscreen across other windows
  * toggle floating and always-on-top for window_x

See: :ref:`i3wm`


.. index:: GPU
.. _gpu:

GPU
~~~~
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

=====
CUDA
=====
| Wikipedia: https://en.wikipedia.org/wiki/CUDA
| Homepage: http://www.nvidia.com/object/cuda_home_new.html

CUDA (*Compute Unified Device Architecture*) is an API for
:ref:`GPUs <gpu>`.

CUDA-accelerated libraries for
:ref:`data science`, :ref:`machine-learning`, :ref:`deep learning`:

  + Pylearn2 (Theano), Numba
  + Torch
  + cuBLAS (BLAS + CUDA = faster than Intel MKL)

    https://developer.nvidia.com/cuBLAS


.. index:: PhysX
.. _physx:

========
PhysX
========
| Wikipedia: https://en.wikipedia.org/wiki/PhysX
| Homepage: https://developer.nvidia.com/gameworks-physx-overview

PhysX is a realtime physics engine for :ref:`GPUs <gpu>` by Nvidia.



.. index:: VGA
.. _vga:

VGA
~~~~
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
~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Digital_Visual_Interface
| Wikipedia: https://en.wikipedia.org/wiki/Digital_Visual_Interface#Connector

DVI is a video display interface.

* DVI connectors are often *white*.
* There are a number of different DVI connectors;
  as well as Mini-DVI and Micro-DVI connectors.


.. index:: HDMI
.. _hdmi:

HDMI
~~~~~
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


.. index:: Mini HDMI
.. _mini hdmi:

============
Mini HDMI
============
Mini HDMI is an :ref:`HDMI` Type C ("Mini HDMI Type A") connector.

* Mini HDMI connectors are often found on older mobile devices.
* :ref:`Micro HDMI` supersedes Mini HDMI.

.. note:: An adapter is required to connect :ref:`Mini HDMI`
   and/or :ref:`Micro HDMI` connectors
   to e.g. a standard HDMI Type A connector on a TV.


.. index:: Micro HDMI
.. _micro hdmi:

============
Micro HDMI
============
Micro HDMI is an :ref:`HDMI` Type E connector.

* Micro HDMI connectors are often found on newer mobile devices.
* :ref:`Micro HDMI` supersedes :ref:`Mini HDMI`.

.. note:: An adapter is required to connect :ref:`Mini HDMI`
   and/or :ref:`Micro HDMI` connectors
   to e.g. a standard HDMI Type A connector on a TV.



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

USB bus speeds:

* USB -- 12 mbps
* USB 2.0 -- 480 Mbps
* USB 3.0 -- 5000 Mbps (5 Gbps) (5 :ref:`gigabit`)
* USB 3.1 -- 10000 Mbps (10 Gbps) (10 :ref:`gigabit`)
* :ref:`USB Type-C` (USB 3.1; 10 GBps)

.. _microusb:

USB connectors:

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

* Each USB device can draw 5 :ref:`v <volt>` 500 :ref:`mA <ampere>`
  of current (2.5 :ref:`watts <watt>`).

  * :ref:`USB Type-C` devices support 5 :ref:`v <volt>` 1.5 :ref:`A <ampere>`,
    3.0 :ref:`A <ampere>` + 900 :ref:`mA <ampere>`
    (e.g. for charging and powering one laptop or mobile device from another).


.. index:: USB Hub
.. _usb hub:

USB Hub
~~~~~~~~~~
A :ref:`USB` Hub is an n-way splitter with two or more
USB connectors.

* A *powered USB Hub* is a USB Hub which must be connected
  to an external power source;
  and can charge many devices

  * :ref:`USB Type-C` essentially functions as a powered USB Hub
    (in either direction, as power is available)


.. index:: USB Keyboard
.. _usb keyboard:

=============
USB Keyboard
=============


.. index:: USB Mouse
.. _usb mouse:

===========
USB Mouse
===========

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

IDE (*Integrated Drive Electronics*) is a 40-pin cable connector
and drive interface standard which predates
(and is now part of) the :ref:`Parallel ATA <pata>` standards.

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
based on :ref:`IDE <ide drive>`, ATA, and ATAPI.

* :ref:`SATA` (*Serial ATA*) is derived from :ref:`PATA` (*Parallel ATA*).
* Newer drives have :ref:`USB`, :ref:`SATA`, or :ref:`eSATA` connectors


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

See: :ref:`data engineering`


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
.. _nic:

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

.. _wi-fi:  
.. _wifi:

802.11 "WiFi" standards:

+---------------+-------------------+----------------------------------+
| IEEE Standard | Frequency Band[s] | Bandwidth (bits per second)      |
+---------------+-------------------+----------------------------------+
| 802.11b       | 2.4 GHz           | 11 Mbps                          |
+---------------+-------------------+----------------------------------+
| 802.11g       | 2.4 GHz           | 54 Mbps                          |
+---------------+-------------------+----------------------------------+
| 802.11a       | 5 GHz             | 54 Mbps                          |
+---------------+-------------------+----------------------------------+
| 802.11n       | 2.4 GHz, 5 GHz    | 600 Mbps (MIMO)                  |
+---------------+-------------------+----------------------------------+
| 802.11ac      | 2.4 GHz, 5 GHz    | 1300 Mbps (MIMO)                 |
+---------------+-------------------+----------------------------------+
| 802.11ad      | 60 GHz            | 7000 Mbps ("WiGig")              |
+---------------+-------------------+----------------------------------+
| 802.11ax      | 2.4 GHZ, 5 GHZ    | ~4x 802.11ac [ Draft ]           |
+---------------+-------------------+----------------------------------+
| 802.11ay      | 60 GHz            | 100000 Mbps (100 Gbps) [ Draft ] |
+---------------+-------------------+----------------------------------+
|               |                   |                                  |
+---------------+-------------------+----------------------------------+

MIMO
    Multiple-Input Multiple-Output 802.11 devices
    aggregate multi-link capacity
    (and so operate with multi-band presence).

Other IEEE 802.11 standards:

* 802.11s -- wireless mesh networking
*

.. note:: Microwave ovens and cordless telephones, for example,
   operate in the 2.4 GHz (and 900 MHz) bands; which may cause
   interference in the already-crowded 2.4 GHz frequencies;
   which is why 802.11a, 802.11n, 802.11ac all [also] support
   the 5 GHz (:ref:`hz`) range.


.. index:: Wi-Fi Direct
.. _wi-fi direct:

Wi-Fi Direct
~~~~~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Wi-Fi_Direct

Wi-Fi Direct is an alternative to :ref:`Bluetooth` with
relatively seamless
wireless device pairing/configuration.


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

  * http://redstone.us.com/simplified-wireless-architecture/
  * http://redstone.us.com/8-major-breakthroughs/


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




Network Glossary
==================

.. glossary::

  SOHO
    Small home office

  Modem
    Modulator/demodulator. Transforms between [:ref:`ethernet`, :ref:`ethernet`
    over :ref:`HSB`] signals
    Coaxial *Cable* (*Co-ax*),
    to e.g. *DSL* Twisted Copper Pair(s),
    :ref:`Mobile Broadband` (*cell-modem*),
    SDR (*Software Defined Radio*),
    :ref:`Fiber to the x`.

  ARP
    ARP (*Address Resolution Protocol*) is an :ref:`IETF` standard
    for linking :term:`IP` addresses with :ref:`ethernet` addresses.

    | Standard: https://tools.ietf.org/html/rfc826

    ::

        arp -a  # list arp entries [BSD style]
        arp -e  # list arp entries [Linux tabular format]
        arp -n  # do not resolve DNS addresses (display IPs instead)

  DHCP
    DHCP (*Dynamic Host Configuration Protocol*) is an internet standard
    for acquiring IP address leases and e.g. DNS resolver configuration
    settings.

    Most SOHO routers include a DHCP server.

    Some ISPs offer 'dynamic' IPs: an IP lease is acquired and/or
    released for a given MAC address, and may change as often as the ISP
    DHCP configuration specifies.

    Some ISPs offter 'static' IPS: through DHCP and/or manual
    configuration of static routes.

    If a DHCP lease expires while e.g. downloading or streaming,
    the connections are only dropped if the address
    is also removed from the interface (e.g. by dhclient upon
    notification of the DHCP lease expiration). One workaround
    for this is to preemptively renew the DHCP lease
    (as dhclient usually does).

    To troubleshoot an ISP connection by removing the router
    and directly attaching a device with a firewall that starts at boot
    time,
    it's often necessary to 'clone' the :term:`MAC address`
    (for a static IP) or release the DHCP lease and/or power-cycle the
    modem.

    | Wikipedia: https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol

  Gateway
    A gateway provides a connection to another :term:`IP` network.

    A routing table may include a default gateway :term:`network route`
    and zero or more additional routes defined by system configuration
    and/or :term:`DHCP`

  Network Interface
    A network interface is a software identifier for a "port"
    on a :term:`NIC`.

    .. code:: bash

        ## List interfaces
        ifconfig    # UNIX, BSD, Linux
        ipconfig    # Windows
        ip l #link  # Linux
        ip -s link  # Linux
        ip a #addr  # Linux

        ## Bring an interface up or down
        ifconfig eth0 up 127.2.2.2 netmask 255.255.255.0 broadcast 127.2.2.255
        ifconfig eth0 down
        ip l set dev eth0 up
        ip l set dev eth0 down

    * There may be one or more network interfaces registered to a
      :term:`NIC`::

        ip addr add 127.1.2.3 dev lo netmask 255.255.255.0

  NIC
    A NIC (:term:`Network Interface` *Card*), or *Network Card*,
    is a physical adapter
    for connecting to a network (generally with a physical
    :ref:`ethernet` (or :ref:`fiber`) cable).

    * A :ref:`wireless` :term:`NIC` is also called
      a *wireless card* or *wireless adapter*.

    | Docs: :ref:`NIC`

  Network Route
    Packets are routed based upon network routing tables: rules
    for which :term:`network interface(s) <network interface>`
    and/or link(s)/tunnel(s) to send packets destined
    for anywhere (default gateway) or a specific network subnet
    (identified by e.g. a /24 prefix or a 255.255.255.0 subnet mask).

        netstat -rn # BSD, OSX, Linux
        route -n    # Linux # Flags="G"
        route add gw 192.168.1.1 dev eth0
        ip r #route # Linux       # "default via"
        ip r add default gw 10.2.2.253
        ip r add 10.2.3.0/24 via 10.2.2.253 dev eth0

        # routes are usually managed by the OS.
        # to reset them all and reboot all interfaces with downtime (!):
        #  /etc/init.d/networking restart   # SysV Ubuntu, Debian
        #  service network restart          # systemd {...}

        # restart interface eth0
        #  #(and re-run dhcplient for an IP lease from DHCP
        #  #  (e.g. from a router that assigns local IPs ike 192.168.0.101))
        #  ifdown eth0; ifup eth0           # Linux [man ifdown ifup]

  Hub
    A network hub connects (or *bridges*) multiple network interfaces
    to a shared bus; where all machines get a copy of all packets
    as repeated by the hub.

    * Normally, a :ref:`NIC` (device, driver) is configured
      to select only packets destined for local addresses.
    * (In *promiscuous mode*, an interface receives all packets
      regardless of the packet protocol destination field.
      (Useful for debugging e.g. :term:`ARP`)).

  Bridge
    A network bridge is a :term:`hub`; often
    a software defined bridge to which :term:`network interfaces <network
    interface>` can be *added*/*attached* and *deleted*/*removed*.

    In :ref:`Linux`, network bridges are configured with ``brctl``:

        brctl
        brctl show

        # create a bridge which will last until reboot
        brctl addbr br0
        brctl addif br0 eth0
        btctl addif br0 eth1
        brctl show  br0
        brctl showmacs br0

  Switch
    A network switch routes packets to specific ports based upon
    an :term:`ARP` table.

    * :term:`SOHO` :term:`Routers <router>` are often
      configured as a switch (relay packets);
      with a fallback or configuration setting to
      :term:`hub` mode (repeat all packets).

  Router
    A :term:`SOHO` Router is usually configured as a
    :term:`Gateway` and a :term:`Switch`
    (with at least one port allocated to a different network
    connection).

    * An actual ("trunk", "internet", "backbone")
      router is usually configured as a `Router`,
      with routing table advertisement protocols
      like RIP, BGP, and **IPv6 radvd**; in order to optimize throughput
      and minimize latency.
    * :term:`SOHO` :term:`Routers <router>` are often
      configured as a switch (relay packets);
      with a fallback or configuration setting to
      :term:`hub` mode (repeat all packets).

  AP
    A :ref:`wireless` access point (*AP*) is a wireless :term:`NIC`
    with one or more antennas and a power source;
    which often also acts as a router and/or a wireless mesh router.

    .. note::

        Cool :term:`AP` Ideas
        (cost, maintenance, spacing, redundancy, resiliency):

        * [ ] Wifi Streetlamp posts
        * [ ] Wifi Parking meters
        * [ ] Solar wireless APs (shaped as flowers for cost and
          water/cleaning/maintenance)
        * [ ] MEMS wireless APs (see also: Bluetooth BLE)

  WiFi
    WiFi is a name for a set of
    :ref:`IEEE 802.11 <802.11>` :ref:`wireless` standards.
