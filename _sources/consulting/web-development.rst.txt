

.. index:: Web Development
.. _web development:

Web Development
-----------------
| Wikipedia: https://en.wikipedia.org/wiki/Web_development


Web Glossary
~~~~~~~~~~~~~~~
.. glossary::

    Web Page
        A *web page* is a single ("static") :ref:`HTML` page.

        * Sometimes, when people say :term:`web page`
          they really mean the whole
          :term:`website` (as composed by e.g.
          a :term:`web application` backed by a :ref:`database <databases>`
          or a static page generator
          with support for managing
          collections
          of interlinked :ref:`HTML` pages
          (e.g. :ref:`Sphinx`, :ref:`Tinkerer`).

        | Wikipedia: https://en.wikipedia.org/wiki/Web_page

    Website
    Web site
        A website is a set of interlinked :ref:`HTML` pages.
        Also used to refer to a web page.

        | Wikipedia: https://en.wikipedia.org/wiki/Website

    Web Application
        A web application is a software application
        running on a server which returns
        responses to specific requests and may interact with a database,
        email services, etc.

        * Like all :term:`systems <system>`,
          a web application works with variable data inputs and outputs.

        | Wikipedia: https://en.wikipedia.org/wiki/Web_application
        | Docs: :ref:`Information Systems > Cloud Application Layers <cloud application layers>`

    Web Hosting Service
        A web hosting service offers
        virtual or physical server resource space
        for a web page, web site, or web application.

        * Shared, Dedicated, Virtual Private, Cloud (Virtual Instance)
        * Managed (24/7 Supported // n hours a month),
          Unmanaged (file a support request and wait)

        | Wikipedia: https://en.wikipedia.org/wiki/Web_hosting_service
        | Docs: :ref:`clouds`
        | Docs: :ref:`web hosting`

    MAC address
        A MAC (*Media Access Control*) address is a
        48-bit identifier.

        * :ref:`NIC` cards have a `MAC address`.
        * :ref:`Wireless` cards a `MAC address`.
        * Many :ref:`Wireless` Access Points (*AP*)
          MAY all have the same text ``SSID``
          but different `MAC addresses`
          (e.g. for :ref:`wireless mesh networking <wireless mesh
          network>` or `WDS`)
        * :term:`DHCP` :term:`IP address` leases
          are tied to a `MAC address`.
        * A `MAC address`
          identifies a node to the nearest packet routing link
          segment (e.g. AP, Switch, Hub, Bridge).
        * Some :term:`IPv6 addresses <ipv6 address>`
          contain the link `Mac address`.
        * :term:`UUID` version 1 128-bit identifiers
          contain a link `MAC address` and the date/time.
          (:ref:`Python` ``import uuid; print(uuid.uuid1())``)

        | Wikipedia: https://en.wikipedia.org/wiki/MAC_address

    ARP
        Address Resolution Protocol

        | Wikipedia: https://en.wikipedia.org/wiki/Address_Resolution_Protocol

    TCP
        Transmission Control Protocol

        | Wikipedia: https://en.wikipedia.org/wiki/Transmission_Control_Protocol

    IP
        Internet Protocol

        | Wikipedia: https://en.wikipedia.org/wiki/Internet_Protocol

    IP Address
        A :term:`IP` identifier
        number identifying a particular network entity (e.g. ``127.0.0.1``)

        * We are running out of 32-bit :term:`IPv4` addresses (``127.0.0.1``),
          and are now moving toward 128-bit :term:`IPv6` addresses (
          ``0000:0000:0000:0000:0000:0000:0000:0001``, ``::1``)

        * Certain IP addresses are locally-routable (e.g. ``192.168.0.1``
          within a home LAN)
          while others are globally-routable (e.g. ``8.8.8.8``)

        | Wikipedia: https://en.wikipedia.org/wiki/IP_address

    IPv4
        IPv4 (:term:`IP` version 4) is a :ref:`web standard <web
        standards>` protocol defined by :ref:`ietf`.

        | Wikipedia: https://en.wikipedia.org/wiki/IPv4
        | Docs: :term:`IPv4 Address`


    IPv4 Address
        :term:`IPv4` addresses are 32-bit :term:`IP Address`
        identifiers.

        | Standard: https://tools.ietf.org/html/rfc1918


        .. code:: bash

            ## Local IPv4 Addresses
            127.0.0.1
            10.0.0.0/8
            172.16.0.0/12
            192.168.0.0/16

            ## Global IPv4 Addresses
            8.8.8.8

    IPv6
        IPv6 (:term:`IP` version 6)
        is a :ref:`web standard <web standards>`
        protocol defined by :ref:`ietf`.

        | Wikipedia: https://en.wikipedia.org/wiki/IPv6

    IPv6 Address
        :term:`IPv6` addresses are 128-bit :term:`IP Address`
        identifiers.

        | Wikipedia: https://en.wikipedia.org/wiki/IPv6_address
        | Standard: https://tools.ietf.org/html/rfc4291
        | Docs: https://en.wikipedia.org/wiki/IPv6_address#IPv6_address_scopes
        | Docs:

        IPv6 Address Examples:

        .. code:: bash

            ## Local IPv4 Addresses
            0000:0000:0000:0000:0000:0000:0000:0001  == ::1  # 127.0.0.1
            0001:0000:0000:0000:0000:0000:0000:0001  == 1::1

            ::/128          # unspecified           (~IPv4 0.0.0.0/32)
            ::1/128         # localhost             (~IPv4 127.0.0.0/24)
            ::/0            # unicast default route (~IPv4 0.0.0.0/0)
            ::ffff:0:0/96   # IPv6-mapped IPv4
            ::96            # IPV4 compatible IPv6 addresses (deprecated)
            2002::/16       # 6to4
            2001::/32       # teredo
            fc00::/7        # unique local address
            fe80::/10 #MAC  # link-local address    (~IPv4 169.254.0.0/16)
            fec0::/10       # site-local address (deprecated)
            3ffe::/16       # 6bone (returned)

            ## Global IPv6 Addresses
                                                             # 8.8.8.8

    DHCP
        DHCP (*Dynamic Host Configuration Protocol*) is a standard
        for acquiring an :term:`IP address`, :term:`DNS`, and :ref:`NTP`
        settings.

        | Wikipedia: https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol

    Domain Name
        A human-readable textual name for a network entity
        (e.g. ``example.org``)

        | Wikipedia: https://en.wikipedia.org/wiki/Domain_name

    DNS
        Domain Name System. Converts a :term:`domain name`
        (e.g. ``localhost`` or ``wrdrd.github.io``) into an
        :term:`IP address` (e.g. ``127.0.0.1`` (IPv4) or ``::1`` (IPv6)).

        * Initial DNS hosting costs are often covered by Web Hosts.
        * There are DNS record types for different types of services.
        * Surfing to a website in a browser
          may utilize ``A``, ``AAAA``, and/or ``CNAME`` records to lookup
          the :term:`IP address` of the web server (or least busy load
          balancer).
        * Sending an email utilizes an ``MX`` record to lookup the IP address
          and sender information for the mail host.
        * Updates to DNS settings can take as long as 86400 seconds (one
          day) to propagate, depending upon the DNS TTL.

        | Wikipedia: https://en.wikipedia.org/wiki/Domain_Name_System
        | Docs: :ref:`DNS Configuration <dns-configuration>`
        | Docs: :py:mod:`wrdrd.tools.domain`

    URL
        A URL (*Uniform Resource Locator*) is a string of characters that identify
        a resource location.

        Where ``host`` is an IP address, hostname, or domain name,
        a URL is of the form:
        ::

            scheme://host:port/p/a/t/h

            https://wrdrd.github.io/docs/   # https, wrdrd.github.io, port 443, /docs/

        * With an :ref:`http <HTTP>` scheme, the default port is 80.
        * With an :ref:`https <HTTPS>` scheme, the default port is 443.

        | Wikipedia: https://en.wikipedia.org/wiki/Uniform_resource_locator

    URI
        A URI (*Uniform Resource Identifier*) is a string of characters that identify
        a resource.

        ::

            scheme://host:port/p/a/t/h?query#fragment

            https://wrdrd.github.io/docs/#wrdrd

        * :term:`URLs <url>` are URIs.
        * :term:`URNs <urn>` are URIs.

        | Wikipedia: https://en.wikipedia.org/wiki/Uniform_resource_identifier

    URN
        A URN (*Uniform Resource Name*) is a string of characters
        that identify a named resource *in a namespace*.

        ::

            urn:namespace:key

            urn:isbn:0-486-27557-4
            urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66

        | Wikipedia: https://en.wikipedia.org/wiki/Uniform_resource_name

    Magnet URI
        A Magnet :term:`URI` is a :term:`URN` containing an key to retrieve
        from a network (such as a :ref:`DHT`).

        * :term:`Web browsers <web browser>` can be configured
          to open Magnet URIs with other programs.

        | Wikipedia: https://en.wikipedia.org/wiki/Magnet_URI_scheme

    UUID
        A UUID (*Universally Unique Identifier*) is a 128- :ref:`bit`
        identifier for a resource.

        :ref:`IETF` RFC 4122 defines 5 different algorithms
        for generating :term:`UUID <uuid>`:

        * UUID 1
              A UUID 1 identifier contains a
              :term:`mac address` and a :ref:`datetime <time standards>`
              with 100- nano-:ref:`second` resolution.
        * UUID 2
              A UUID 2 identifier contains a
              :term:`mac address` and a :ref:`POSIX` UID or GID.
        * UUID 3
              A UUID 3 identifier contains an :ref:`MD5`
              hash of a :term:`URI`, :term:`URN`, or :ref:`URL`.
        * UUID 4
              A UUID 4 identifier contains a random identifier
              as determined by the configured source of random.
        * UUID 5
              A UUID 5 identifier contains an :ref:`SHA-1 <sha>`
              hash of a :term:`URI`, :term:`URN`, or :ref:`URL`.

        | Wikipedia: https://en.wikipedia.org/wiki/Universally_unique_identifier
        | Standard: https://tools.ietf.org/html/rfc4122

    Web Browser
        A software program which visually renders resources
        identified by a URL and interprets scripts.

        Examples: Internet Explorer, Mozilla Firefox, Google Chrome

        * All web browsers support :ref:`HTML` over :ref:`HTTP`.
        * Many web browsers support :ref:`HTTPS` and/or :ref:`HTTP STS`.
        * Some web browsers support :ref:`WebSockets`.
        * Some web browsers support :ref:`WebRTC`.
        * Many web browsers support image formats like
          :ref:`GIF`,
          :ref:`JPEG`,
          :ref:`PNG`,
          and :ref:`SVG` Scalable Vector Graphics.
        * Many web browsers support :ref:`Javascript` scripts.
        * All web browsers work with a :term:`DOM` (Document Object Model)
          which is parsed from :ref:`HTTP`
          and transformed by :ref:`Javascript`.
        * A number of example web browser extensions:
          :ref:`Browser Extensions`

        | Wikipedia: https://en.wikipedia.org/wiki/Web_browser
        | Docs: :ref:`Tools  > Browsers <browsers>`
        | Docs: :ref:`WebSec`

    DOM
        Document Object Model. Can be thought of as a layout outline of
        the objects in a particular document
        (e.g. text, shapes, images, videos).

        Different web browsers interpret the DOM differently,
        depending on Web Standards and individual implementations.

        | Wikipedia: https://en.wikipedia.org/wiki/Document_Object_Model
        | Docs: :ref:`Web Design <web-design>`

    Web Standard
        An agreed-upon standard specification for web things like
        data interchange, structure, and presentation.

        | Wikipedia: https://en.wikipedia.org/wiki/Web_standards
        | Docs: :ref:`web standards`
        | Docs: :ref:`semantic web standards`

    Open Web Standards
        Open Web Standards are :ref:`Open Source` :term:`Web Standards <web standard>`
        (e.g. :ref:`HTTP`,
        :ref:`HTML`,
        :ref:`XHTML`,
        :ref:`HTML5`,
        :ref:`CSS`,
        :ref:`Javascript`,
        :ref:`SVG`,
        :ref:`RDF`)



.. index:: Web Content
.. index:: Content
.. _web content:

Web Content
~~~~~~~~~~~~~

Media Resources: Copy, Text, Photos, Images, Videos
(things with :ref:`HTTP` URLs)

See :ref:`web standards`, :ref:`Art & Design <art-design>`



.. index:: Web Design
.. _web design:

Web Design
~~~~~~~~~~~
| Wikipedia: https://en.wikipedia.org/wiki/Web_design


.. index:: CSS
.. _css-webdev:

CSS
+++++
| Wikipedia: https://en.wikipedia.org/wiki/Cascading_Style_Sheets
| Docs: :ref:`CSS`

CSS (*Cascading Style Sheets*) define the presentational
aspects of :ref:`HTML` and a number of mobile and desktop
web framworks.

* CSS is designed to ensure separation of data and presentation.
  With javascript, the separation is then data, code, and presentation.


.. index:: Web Layout
.. _web-layout:

Web Layout
+++++++++++
A *web layout* is a box-model composition of :term:`DOM` objects,
their styles, and their
behaviors at various screen sizes and resolutions.

Different browsers implement the :term:`DOM`,
:ref:`HTML`, :ref:`CSS`, and :ref:`Javascript`
differently. It is necessary to test a web layout in the browsers which
are utilized by the target audience.

In general, a simpler page renders faster and more
consistently.

Some users may be browsing without Javascript (either because their
very classic web browser doesn't support it, or, optionally,
because of security concerns introduced by active page scripts). Because
of this, it's usually best to not rely upon Javascript for page layout
and instead work with pure-CSS implementations.

CSS framework developers specialize in developing CSS grids and layouts
which work across browsers, devices, and various screen sizes.


* https://en.wikipedia.org/wiki/Page_layout
* https://en.wikipedia.org/wiki/Web_design#Page_layout
* https://en.wikipedia.org/wiki/CSS_frameworks
* https://en.wikipedia.org/wiki/Responsive_Web_Design
* https://en.wikipedia.org/wiki/List_of_displays_by_pixel_density


.. _image-based-layouts:

Image Based Layouts
````````````````````
At first glance, it may seem that an image-based layout with fixed
dimensions (as might be developed in a traditional graphic design program)
would be simpler and easier; however:

* an 800px wide image layout is hardly usable on a mobile device
* search engines and screen readers are unable to read text embedded
  within images; necessitating ``alt=`` attributes on ``<img>`` tags
  and ``title=`` attributes on ``<a>`` tags
* when scaled (by zooming in), raster images like JPEG, PNG, and GIF
  look blocky and pixelated

Practically, it is not possible to develop a responsive web layout which
supports diverse screen sizes and resolutions with traditional graphic
design tools. It is far more consistent and reproducible to start with
an HTML web page and a CSS framework and then develop a template from
there.

.. index:: Screen Captures
.. _screen captures:

Screen Captures
++++++++++++++++
There are many tools and services for collecting screen captures (or
screen shots) of web layouts.

Features to look for:

* Capturing the visible area of the page
* Capturing the whole page
* Setting the browser resolution

Ways to collect screen captures
and movies at various points in a testing workflow:

* Browser: :ref:`Web Browser <browsers>`
  testing tools (e.g. :ref:`Javascript`)
* Browser: :ref:`browser extensions`
* Web Service: multi-platform browser testing grid services
* Build Script: record the [:ref:`X <X11>`] buffer with the test sequence
* Local Recording:
  :ref:`ffmpeg`, :ref:`VLC`, CamStudio

See: :ref:`Video Production`


.. index:: Bootstrap
.. _bootstrap:

Bootstrap
+++++++++++
| Wikipedia: `<https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)>`_
| Homepage: https://getbootstrap.com/
| Source: git https://github.com/twbs/bootstrap

* What is Bootstrap?

  * A responsive HTML and CSS (LESS, Sass SCSS (4.0)) Framework.
  * `<https://en.wikipedia.org/wiki/LESS_(stylesheet_language)>`_
  * `<https://en.wikipedia.org/wiki/Sass_(stylesheet_language)>`_
  
* Bootstrap :term:`Web Site` Styles / Themes / Templates

  https://expo.getbootstrap.com/resources/

  * Custom:

    * https://getbootstrap.com/customize/#less-variables
    * http://bootply.com/

  * Templates:

    * https://themes.getbootstrap.com/ (Updated, Free, Official)

      https://themes.getbootstrap.com/pages/our-license
    * https://expo.getbootstrap.com/resources/#themes
    * https://bootswatch.com/ (Free)
    * http://www.themesforbootstrap.com/
    * https://wrapbootstrap.com/
    * https://wrapbootstrap.com/theme/deusone-responsive-one-page-template-WB0271X52
    * http://themeforest.net/search?utf8=%E2%9C%93&term=bootstrap

  * Examples:

    * https://expo.getbootstrap.com/
    * http://builtwithbootstrap.com/
    * http://v4-alpha.getbootstrap.com/examples/


.. index:: Web Development Checklist
.. _web development checklist:

Web Development Checklist
~~~~~~~~~~~~~~~~~~~~~~~~~~
A checklist for building a modern website
with structured data; for search,
social web, sharing.

See also: `<http://webdevchecklist.com/>`_

* [ ] Pick a CSS framework
* [ ] Create page layout template

  * [ ] Create or acquire static template

    * Helps if it already includes a CSS framework

  * [ ] Create or acquire dynamic template

* [ ] Create static HTML page from layout template


* [ ] Port content from existing site

  * [ ] Add HTML formatting
  * [ ] Add CSS #id deep link anchors and classes


* [ ] Add structured data markup to page

  * http://schema.org/docs/full.html
  * See: :ref:`knowledge engineering`,
    :ref:`semantic web standards`,
    :ref:`Schema.org`

  * [ ] Add standard header tags

    * [ ] ``meta`` tags: description
    * [ ] ``link rel="canonical"``
    * [ ] ``lang="en"``

  * [ ] Add OpenGraph meta markup

    * http://ogp.me/
    * ``og:title``
    * ``og:type``
    * ``og:image`` (``:width``, ``:height``, ``:type``)
    * ``og:url``

* [ ] Section: Navbar

  * [ ] Choose top-level links
  * [ ] Indicate current location

* [ ] Section: Above the fold

  * ``schema:ImageObject``
  * ``schema:VideoObject``
  * ``schema:MusicVideoObject``
  * Text
  * HTML/CSS/JS

* [ ] Add an ``<h1>`` tag with a page title

* [ ] Section: About

  * [ ] Add textual description
  * [ ] Organization (``schema:Organization``)
  * [ ] Business (``schema:Organization`` > ``schema:LocalBusiness`` > {...})

* [ ] Section: Products / Services

  * [ ] Acquire product/menu/service offering information

    + [ ] Products (``schema:Product``, ``schema:ProductModel``)
    + [ ] Services (``schema:Service`` < ``schema:Intangible``)

  * [ ] Format product/menu/service offering information as HTML + RDFa

* [ ] Section: Media / In the news

  * [ ] Research media profile

    + [ ] Articles ``schema:Article`` > ``schema:NewsArticle``

  * [ ] Acquire news media assets

    + [ ] Media Objects (``schema:MediaObject``)


* [ ] Section: Contact

  * [ ] Email
  * [ ] Name, Address, Telephone
    (``schema:LocalBusiness`` > ``schema:Organization`` > ``schema:Place``)
  * [ ] Locations (``schema:LocalBusiness``)

    * [ ] Embed map thumbnail/widget
    * [ ] Link to Directions


  * ``schema:Organization``

    * ``name``
    * ``url``
    * ``address`` <``schema:PostalAddress``>
    * ``hasMap`` (``map``) URL
    * Directions
    * ``telephone``
    * ``faxNumber``
    * ``email``
    * ``description``
    * ``logo``
    * ``image``
    * ``sameAs`` (~= URL)
    * ``legalName``
    * ``founder``
    * ``foundingDate``
    * ``taxID`` (TIN)
    * ``memberOf``

  * ``schema:LocalBusiness`` < ``schema:Organization``

    * ``name``
    * ``url``
    * ``address`` <``schema:PostalAddress``>
    * ``hasMap`` (``map``) URL
    * Directions
    * ``telephone``
    * ``faxNumber``
    * ``email``
    * ``image`` (s)

    * ``branchOf`` <``schema:Organization``>
    * ``openingHours``
    * ``currenciesAccepted``
    * ``paymentAccepted``
    * ``priceRange``

    * ``schema:FoodEstablishment`` < ``schema:LocalBusiness``

      * ``acceptsReservations`` Yes/No/URL
      * ``menu`` text/URL
      * ``servesCuisine`` text


  * [ ] Social Media

    * [ ] Google+
    * [ ] Twitter
    * [ ] Facebook
    * [ ] LinkedIn
    * [ ] [...]


* [ ] Section: Footer

  * [ ] Copyleft: ``&copy; <year> <business name>``
  * [ ] <location>
  * [ ] Feedback
  * [ ] Terms
  * [ ] Privacy


* [ ] Section: Post-load JS scripts

  * [ ] JS libraries (:ref:`CDN`, cdnjs, jQuery, :ref:`Bootstrap`,
    underscore, Backbone, Angular, React)
  * [ ] JS Analytics loaders (:ref:`data science`
    > :ref:`repro:ObservationalStudy <linked reproducibility>`)
  * [ ] JS Optimization loaders (:ref:`machine-learning`
    > :ref:`repro:ControlledTrial <linked reproducibility>`)


Hosting / DNS
~~~~~~~~~~~~~

.. index:: DNS Configuration
.. _dns-configuration:

DNS Configuration
+++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Domain_Name_System
| Standards: https://en.wikipedia.org/wiki/Domain_Name_System#RFC_documents
| Standards: https://en.wikipedia.org/wiki/List_of_DNS_record_types
| Standards: https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions

:term:`DNS` :term:`Domain Name` Information (``A``, ``AAAA``, ``CNAME``,
``TXT``, ``MX``, ``SRV``)
::

    DOMAIN="<domainname>"
    IP=$(nslookup $DOMAIN)

* Date of Registration / Expiration
* Registrant (Name, Address, Email)

  * Privacy / WhoisGuard

* DNS Registration Service Provider
* Linux/OSX DNS Commands::

    nslookup DOMAIN
    dig $DOMAIN
    dig +qr any $DOMAIN
    dig -t mx $DOMAIN
    whois $DOMAIN
    whois $DOMAIN | egrep 'Registrar|Date|Domain Status|Registrant|Admin'

* Online Whois Tools

  * https://whois.domaintools.com/$DOMAIN

See: :py:mod:`wrdrd.tools.domain`


.. index:: Web Hosting
.. _web hosting:

Web Hosting
+++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Web_hosting_service

:term:`Web Hosting <Web Hosting Service>` Information

* Reverse IP (How many sites are hosted from the same
  :term:`IP address`?)

  * http://reverseip.domaintools.com/search/?q=$IP

See: :ref:`Information Systems > Clouds <clouds>`


.. index:: WebSec
.. _websec:

WebSec
~~~~~~~~~
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Web_security_exploits
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Internet_security


WebSec (*web security*) is :ref:`Information Security`
for web applications.

Security at :ref:`W3C` :

* http://www.w3.org/Security/
* http://www.w3.org/Security/wiki/Main_Page
* http://www.w3.org/2011/webappsec/
* :ref:`Web Standards`


.. index:: Resonsible Disclosure
.. _responsible disclosure:

Responsible Disclosure
+++++++++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Responsible_disclosure

- https://www.owasp.org/index.php/Vulnerability_Disclosure_Cheat_Sheet


.. index:: Bug Bounty Program
.. _bug bounty program:

Bug Bounty Program
``````````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Bug_bounty_program

- Hacker One:

  - Homepage: https://hackerone.com/
  - https://hackerone.com/twitter

- Professional integrity:

  https://en.wikipedia.org/wiki/Integrity

- :ref:`Open Source`


.. index:: SANS/CIS Consensus Audit Guidelines:
.. _sans/cis consensus audit guidelines:

SANS/CIS Consensus Audit Guidelines:
+++++++++++++++++++++++++++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Consensus_audit_guidelines
| Wikipedia: https://en.wikipedia.org/wiki/The_CIS_Critical_Security_Controls_for_Effective_Cyber_Defense
| Wikipedia: https://en.wikipedia.org/wiki/CSC_Version_6.0

* "SANS Top 20": https://www.sans.org/critical-security-controls/
* "SANS Top 25": https://cwe.mitre.org/top25/

* CIS: 

  * https://www.cisecurity.org/critical-controls.cfm
  * https://www.cisecurity.org/critical-controls/reports/
  * PDF for email.


.. index:: CWE
.. index:: Common Weakness Enumeration
.. _cwe:
.. _common weakness enumeration:

CWE
++++++
CWE (*Common Weakness Enumeration*)

| Homepage: https://cwe.mitre.org/


* https://cwe.mitre.org/top25/
* https://cwe.mitre.org/top25/#CWE-89
* https://cwe.mitre.org/data/definitions/89.html


.. index:: OWASP
.. _owasp:

OWASP
++++++++
| Homepage: https://www.owasp.org/

* https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project
* https://www.owasp.org/index.php/OWASP_Proactive_Controls
* https://www.owasp.org/index.php/Top_10_2013-Table_of_Contents
* https://www.owasp.org/index.php/Web_Standards_and_Specifications


.. index:: WebSec Forums
.. _websec forums:

WebSec Forums
++++++++++++++++++
Internet Forums for WebSec ("Web Security")

* :ref:`Responsible Disclosure` / Vulnerability Disclosure
* https://www.cvedetails.com/
* :ref:`IRC`, :ref:`Slack`, :ref:`Mattermost`
* https://www.reddit.com/r/websec
* https://www.reddit.com/r/netsec
* https://twitter.com/search?q=websec
* https://twitter.com/search?q=netsec
* https://twitter.com/search?q=netsec
* https://twitter.com/search?q=infosec


.. index:: HTTP
.. _http-:

HTTP
++++++
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Hypertext_Transfer_Protocol
| WikipediaCategory: https://en.wikipedia.org/wiki/Category:Hypertext_Transfer_Protocol_headers


See:

* Knowledge Engineering > :ref:`HTTP`
* :ref:`HTTPS`, :ref:`HTTPS-`


.. index:: HTTPS
.. _https-:

HTTPS
+++++++
| Wikipedia: https://en.wikipedia.org/wiki/HTTPS

See:

* Knowledge Engineering > :ref:`HTTPS`
* :ref:`HTTP`, :ref:`HTTP-`


.. index:: HTTP STS
.. index:: HTTP Strict Transport Security
.. _http sts-:

HTTP STS
++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security

HTTP STS (*HTTP Strict Transport Security*) is
a standardized extension for notifying browsers
that all requests should be made over :ref:`HTTPS`
indefinitely or for a specified time period.

See also:

* Knowledge Engineering > :ref:`HTTP STS`
* :ref:`https everywhere`


.. index:: ACME Protocol
.. _acme protocol:

ACME Protocol
++++++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/Automated_Certificate_Management_Environment
| Src: https://github.com/ietf-wg-acme/acme/
| Spec: https://tools.ietf.org/html/draft-ietf-acme-acme
| Spec: https://ietf-wg-acme.github.io/acme/draft-ietf-acme-acme.html

- ACME (Automated Certificate Management Environment) is a protocol
  for Web PKI with X.509 Certificates and :ref:`HTTPS` (TLS/SL).
- ACME Spec Introduction:
  https://tools.ietf.org/html/draft-ietf-acme-acme#section-1
- :ref:`Letsencrypt` implements the :ref:`ACME` spec.


.. index:: Letsencrypt
.. _letsencrypt:

Letsencrypt
````````````````
| Wikipedia: https://en.wikipedia.org/wiki/Let%27s_Encrypt
| Homepage: https://letsencrypt.org/
| Src: https://github.com/letsencrypt
| Docs: https://letsencrypt.readthedocs.io/en/latest/
| Docs: https://letsencrypt.readthedocs.io/en/latest/using.html#getting-certificates-and-choosing-plugins
| Docs: https://letsencrypt.readthedocs.io/en/latest/using.html#third-party-plugins

- "A free, automated, and open certificate authority."
- Certs are valid for 90 days
- Use the staging server to avoid the certificate roll rate limit
- There are many :ref:`ACME` clients (that work with letsencrypt):
  
  https://letsencrypt.org/docs/client-options/

  - Certbot is an official, packaged Python client.


.. index:: Web Development Requirements
.. _web development requirements:

Web Development Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* [ ] :ref:`Software Development > Project Management <project management>`
* [ ] :ref:`Team Building > Collaboration Checklist <collaboration checklist>`
* [ ] :ref:`Collaboration Plan`
* [ ] :ref:`Photography Checklist`
* [ ] :ref:`Social Media Images`
* [ ] :ref:`Web Hosting`
* [ ] :ref:`Web Development Checklist`


User Stories
+++++++++++++
| Wikipedia: https://en.wikipedia.org/wiki/User_story

User Stories are an :ref:`agile` :ref:`technique <seven layer model of collaboration>`
for capturing structured requires on *cards* (or as *issues* in e.g. GitHub).

* User Stories are, in general, less complex than *Use Cases*
  which are often more highly specified (in terms of e.g. UML diagrams).
* User Stories can be grouped in **epics**. An **epic** story
  is a long and arduous journey; often with multiple parts.
* User Stories can be :ref:`estimated <effort estimation>`
  and assigned arbitrary but relatively relevant point values
  with e.g. :ref:`planning poker` and/or a :ref:`kanban` web application.


See also:

* :ref:`Software Development` > :ref:`Agile <agile>` > :ref:`User Story`
* :ref:`Team Building` > :ref:`six patterns of collaboration`
