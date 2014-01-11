Process
=======

Background
-----------

DNS/Hosting
~~~~~~~~~~~~~
* ``DOMAIN="<domainname>"``
* ``IP=$(nslookup $DOMAIN)``
* DNS Domain Name Information (A, CNAME, MX)

  * Date of Registration / Expiration
  * DNS Provider
  * Registrant (Name, Address, Email)

    * Privacy / WhoisGuard?

  * Reigration Service Provider
  * Linux Commandline:

    * ``dig $DOMAIN``
    * ``dig -t mx $DOMAIN``
    * ``whois $DOMAIN``

      * ``egrep 'Registrar|Date|Domain Status|Registrant|Admin``

  * Online

    * http://whois.domaintools.com/$DOMAIN

* Web Hosting Information

  * Reverse IP (How many sites hosted at same IP?)

    * ``http://reverseip.domaintools.com/search/?q=$IP``

Business
~~~~~~~~~~
* Acquire structured data markup

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


Marketing
----------

Background
~~~~~~~~~~~

* https://en.wikipedia.org/wiki/Marketing
* https://en.wikipedia.org/wiki/Marketing_plan
* https://en.wikipedia.org/wiki/Online_marketing

Web Analytics
~~~~~~~~~~~~~~~

* https://en.wikipedia.org/wiki/Web_analytics
* https://en.wikipedia.org/wiki/Conversion_marketing#Conversion_rate
* Acquire Analytics tracking codes

Branding
~~~~~~~~~~

Concept
++++++++

* Audience

  * Who are you trying to reach?

* Actions

  * What do you want them to do?

* Emotions

  * How do you want them to feel?


Copy
+++++

* Keywords and phrases


Graphic Design
+++++++++++++++

* Acquire color scheme

  * https://en.wikipedia.org/wiki/Color_scheme

* Acquire type set

  * https://en.wikipedia.org/wiki/Typeface#Style_of_typefaces
  * https://en.wikipedia.org/wiki/Web_typography

* Acquire logo

  * https://en.wikipedia.org/wiki/Logo#Internet-compatible_logos
  * TODO: Logo Sizes (Large, Thumbnail)

    * Facebook

      * Thumbnail: 160x160

    * Twitter
    * LinkedIn
    * Twitter
    * Favicon
    * Apple Touch

      * 57x57, 72x72, 114x114, 144x144

* Acquire favicon

  * https://en.wikipedia.org/wiki/Favicon
  * PNG: 16x16, 32x32, 64x64, 128x128, 256x256, 512x512
  * https://en.wikipedia.org/wiki/ICO_(file_format)
  * Transparent backgrounds look best

* Acquire source images

  * From embedded image layout:

    * Contact Original Designer
    * Crop from image layout

* Acquire content images
* Acquire social media icons

Web Layout
+++++++++++

* https://en.wikipedia.org/wiki/Page_layout
* https://en.wikipedia.org/wiki/Web_design#Page_layout
* https://en.wikipedia.org/wiki/Responsive_Web_Design

  * https://en.wikipedia.org/wiki/List_of_displays_by_pixel_density

* https://en.wikipedia.org/wiki/CSS_frameworks

  * Pick a CSS framework (e.g. Bootstrap)


Web Page
~~~~~~~~~

* Create page layout template

  * Create or acquire static template

    * Helps if it already contains CSS framework

  * Create or acquire dynamic template


* Create static HTML page from layout template


* Port content from existing site

  * Add HTML formatting
  * Add CSS #id and classes


* Add structured data markup to page

  * Add standard header tags

    * meta description

    * link rel="canonical"
    * lang="en"

  * Add OpenGraph meta markup

    * http://ogp.me/
    * og:title
    * og:type
    * og:image (:width, :height, :type)
    * og:url


* Section: Navbar

  * Add CSS #id for single-page layout


* Section: Above the fold

  * Image
  * Video
  * Text


* Add <h1> tag


* Section: About

  * schema:Organization
  * Description


* Section: Products

  * Acquire product/menu/service offering information
  * Format product/menu/service offering information as HTML
  * Convert product/menu/service offering information to structured data


* Section: Media / In the news

  * Research media profile
  * Acquire news media assets


* Section: Contact

  * Name, Address, Telephone
  * Email
  * Locations (LocalBusiness)

    * Embed map thumbnail/widget
    * Link to Directions

  * Social Media

    * Facebook
    * Twitter
    * Google+
    * LinkedIn
    * [...]


* Section: Footer

  * &copy; <year> <business name>
  * <location> 
  * Feedback
  * Terms
  * Privacy


* Section: Post-load JS scripts

  * JS libraries
  * Analytics loaders


Web Design
~~~~~~~~~~~

Bootstrap
+++++++++++

* What is Bootstrap?

  * A responsive HTML and CSS (LESS) Framework
  * http://getbootstrap.com/
  * https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)
  * https://en.wikipedia.org/wiki/LESS_(stylesheet_language)

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


Small Business Services
--------------------------

* Google Apps

  * $5/user/month // $50/user/year
  * gmail (e.g. username@example.org)

    * can add aliases
    * can setup forwarding

  * mail, contacts, chat, calendar, drive, docs, sheets, slides,
    groups, sites

    * drive: online storage
    * sites: (e.g. employees.example.org)

      * update through web interface
      * file sharing (employee handbook pdf)

    * groups: [employee] emailing list

      * don't need accounts for every employee, they can use their
        own email addresses (everything gets relayed)
      * basically like archived emails with always on reply-all

  * http://google.com/a
  * http://learn.googleapps.com/

* Other Services

  * online billing / invoicing / accounting (freshbooks, ...)
  * online billing with Google Payments

    * http://www.google.com/wallet/business/payments/
    * http://www.google.com/wallet/business/offers/index.html

      * similar to Groupon, LivingSocial

  * unfortunately there's not yet a Square API

    * Square integrates with QuickBooks
    * http://www.google.com/enterprise/marketplace/search?query=quickbooks

  * customer relationship management (CRM)

    * 1. opt-in e-mailing list (mailchimp, ...)
    * 2. contact information "rolodex"
    * 3. "sales pipeline"

  * https://www.google.com/enterprise/marketplace/


Social Media
-------------

Business
~~~~~~~~~~

* Location-based Services

  * Google Maps

    * Directions Link
    * Static Images

      * https://developers.google.com/maps/documentation/imageapis/
      * Map Image
      * Street View Image

    * Google MapMaker

      * https://www.google.com/mapmaker/

  * Bing Maps

    * TODO

  * Foursquare

    *

  * Facebook

    *


Restaurant
~~~~~~~~~~~~

* Content

  * Foodie photos are normally close-ups at an angle

    * Top-down / bird's eye photos are not as appealing

* Online Reviews

  * Yelp

    * Photos

  * UrbanSpoon

    * TODO



compression, quality control, dynamic webapps, web service integration

