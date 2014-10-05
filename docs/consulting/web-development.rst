Web Development
-----------------

Web Glossary
~~~~~~~~~~~~~~~
.. glossary::

    Web Page
        A single ("static") HTML page.

        https://en.wikipedia.org/wiki/Web_page

    Website
        A set of interlinked HTML pages. Also used to refer to a web page.

        https://en.wikipedia.org/wiki/Website

    Web Application
        A software application running on a hosted server which returns
        responses to specific requests. May interact with a database,
        email services, etc.

        Works with variable data inputs and outputs.

        https://en.wikipedia.org/wiki/Web_application

    Web Hosting Service
        A service providing virtual or physical server resource space
        for a web page, web site, or web application.

        https://en.wikipedia.org/wiki/Web_hosting_service

    IP Address
        A number identifying a particular network entity (e.g. ``127.0.0.1``)

        We are running out of 32-bit IPv4 addresses (``127.0.0.1``),
        and are now moving toward 128-bit IPv6 addresses (
        ``0000:0000:0000:0000:0000:0000:0000:0001``, ``::1``)

        Certain IP addresses are locally-routable (e.g. ``192.168.0.1``
        within a home LAN)
        while others are globally-routable (e.g. ``8.8.8.8``
        through the internet).

        https://en.wikipedia.org/wiki/IP_address

    Domain Name
        A human-readable textual name for a network entity
        (e.g. ``example.org``)

        https://en.wikipedia.org/wiki/Domain_name

    DNS
        Domain Name System. Converts a domain name into an
        IP address (e.g. 127.0.0.1 (IPv4) or ::1 (IPv6)).

        Initial DNS hosting costs are often covered by Web Hosts.

        There are DNS record types for different types of services.

        Surfing to a website in a browser
        may utilize A, AAAA, and/or CNAME records to lookup the IP
        address of the web server.

        Sending an email utilizes an MX record to lookup the IP address
        and sender information for the mail host.

        Updates to DNS settings can take as long as 86400 seconds (one
        day) to propagate, depending upon the DNS TTL.

        https://en.wikipedia.org/wiki/Domain_Name_System

    URL
        Uniform Resource Locator. A string of characters that identify
        a particular (view of) a resource.

        ::

            scheme://host:port/p/a/t/h?query#fragment

        Where ``host`` is an IP address, hostname, or domain name.

        With an http scheme, the default port is 80.

        With an https scheme, the default port is 443.

        https://en.wikipedia.org/wiki/Uniform_resource_locator

    Web Browser
        A software program which visually renders resources
        identified by a URL and interprets scripts.

        Examples: Internet Explorer, Mozilla Firefox, Google Chrome

        All web browsers support HTML.

        Many web browsers support images like GIF, JPEG, PNG, and SVG.

        Many web browsers support Javascript scripts.

        Web browsers work with a DOM (Document Object Model).

        https://en.wikipedia.org/wiki/Web_browser

    DOM
        Document Object Model. Can be thought of as an outline of
        the objects in a particular document
        (e.g. text, shapes, images, videos).

        Different web browsers interpret the DOM differently,
        depending on Web Standards and individual implementations.

        https://en.wikipedia.org/wiki/Document_Object_Model

    Web Standard
        An agreed-upon standard specification for web things
        (e.g. HTTP, HTML, XHTML, HTML5, CSS, Javascript, SVG)

        https://en.wikipedia.org/wiki/Web_standards

.. index:: Web Content

Web Content
~~~~~~~~~~~~~

Media Resources: Copy, Text, Photos, Images, Videos (things with URLs)


Structured Data
++++++++++++++++++
* http://schema.org/docs/full.html
* Organization

  * name
  * url
  * address PostalAddress
  * telephone
  * email address(es)
  * Description
  * logo
  * image(s)
  * map URL
  * sameAs (~= URL)
  * legalName
  * founder
  * foundingDate
  * taxID (TIN)

* LocalBusiness (> Category)

  * name
  * url
  * address PostalAddress
  * telephone
  * email address(es)
  * Directions
  * image(s)
  * branchOf <Organization>
  * openingHours
  * currenciesAccepted
  * paymentAccepted
  * priceRange
  * map URL
  * FoodEstablishment (> Category)

    * acceptsReservations Yes/No/URL
    * menu text/URL
    * servesCuisine text


.. _web-design:
.. index:: Web Design

Web Design
~~~~~~~~~~~
https://en.wikipedia.org/wiki/Web_design


.. _web-layout:
.. index:: Web Layout

Web Layout
+++++++++++
A *web layout* is a box-model composition of DOM objects, their styles, and their
behaviors at various screen sizes and resolutions.

Different browsers implement the DOM, HTML, CSS, and Javascript
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


Image Based Layouts
````````````````````
At first glance, it may seem that an image-based layout with fixed
dimensions (as might be developed in a traditional graphic design program)
would be simpler as easier. However:

* an 800px wide image layout is hardly usable on a mobile device
* search engines and screen readers are unable to read text embedded
  within images; necessitating `alt` attributes on `<img>` tags and `title`
  attributes on `<a>` tags
* When scaled (by zooming in), raster images like JPEG, PNG, and GIF
  look blocky and pixelated

Practically, it is not possible to develop a responsive web layout which
supports diverse screen sizes and resolutions with traditional graphic
design tools. It is far more consistent and reproducible to start with
an HTML web page and a CSS framework and then develop a template from
there.


Screen Captures
++++++++++++++++
There are many tools and services for collecting screen captures (or
screen shots) of web layouts.

Features to look for:

* Capturing the visible area of the page
* Capturing the whole page
* Setting the browser resolution

Some Javascript testing tools and services support taking screen captures
and movies at various points in a testing workflow.


.. index:: Bootstrap
.. _bootstrap:

Bootstrap
+++++++++++
`<https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)>`_

* What is Bootstrap?

  * A responsive HTML and CSS (LESS) Framework
  * http://getbootstrap.com/
  * `<https://en.wikipedia.org/wiki/LESS_(stylesheet_language)>`_

* Styles / Themes / Templates

  * From Scratch / Customizing

    * http://getbootstrap.com/customize/#less-variables
    * http://bootply.com/

  * Templates

    * http://bootswatch.com/ (FREE)
    * http://www.themesforbootstrap.com/
    * https://wrapbootstrap.com/
    * https://wrapbootstrap.com/theme/deusone-responsive-one-page-template-WB0271X52
    * http://themeforest.net/search?utf8=%E2%9C%93&term=bootstrap

  * Image-heavy templates

    * Difficult to modify (without the PSD source and Photoshop)
    * Slower to load on a phone or tablet


.. index:: Web Page Checklist

Web Development Checklist
~~~~~~~~~~~~~~~~~~~~~~~~~~
See also: `<http://webdevchecklist.com/>`_

* [ ] Pick a CSS framework
* [ ] Create page layout template

  * [ ] Create or acquire static template

    * Helps if it already contains CSS framework

  * [ ] Create or acquire dynamic template

* [ ] Create static HTML page from layout template


* [ ] Port content from existing site

  * [ ] Add HTML formatting
  * [ ] Add CSS #id deep link anchors and classes


* [ ] Add structured data markup to page

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

* [ ] Section: Above the fold

  * Image
  * Video
  * Text


* [ ] Add an ``<h1>`` tag with a page title

* [ ] Section: About

  * [ ] Add textual escription
  * [ ] Add structured data (e.g. ``schema:Organization``)


* [ ] Section: Products

  * [ ] Acquire product/menu/service offering information
  * [ ] Format product/menu/service offering information as HTML
  * [ ] Convert product/menu/service offering information to structured data


* [ ] Section: Media / In the news

  * [ ] Research media profile
  * [ ] Acquire news media assets


* [ ] Section: Contact

  * [ ] Name, Address, Telephone
  * [ ] Email
  * [ ] Locations (``schema:LocalBusiness``)

    * [ ] Embed map thumbnail/widget
    * [ ] Link to Directions

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

  * [ ] JS libraries
  * [ ] Analytics loaders



Hosting / DNS
~~~~~~~~~~~~~

.. index:: DNS Configuration
.. _dns-configuration:

DNS Configuration
+++++++++++++++++++
:term:`DNS` Domain Name Information (A, CNAME, MX)
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

* Online Whois

  * http://whois.domaintools.com/$DOMAIN

Web Hosting
+++++++++++++
:term:`Web Hosting <web-hosting-service>` Information

* Reverse IP (How many sites are hosted from the same IP address?)

  * http://reverseip.domaintools.com/search/?q=$IP

See: :py:mod:`wrdsbc.tools.domain`


Requirements
~~~~~~~~~~~~~~
https://en.wikipedia.org/wiki/Requirements_analysis

https://en.wikipedia.org/wiki/User_story


