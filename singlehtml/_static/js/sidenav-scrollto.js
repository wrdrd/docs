

"use strict";

$(function($) {
  var SidenavPlugin = function(element, options) {
  {
    var elem = $(element);
    var obj = this;
    var settings = $.extend({
      param: 'defaultValue',
    }, options || {});

    this.navbar_scrollto = function(node)
      var sidebar = $('#sidebar-wrapper').first()[0];
      var navbar = $(sidebar).find('div.sidebar').first()[0];

      if (sidebar && navbar) {
        var do_scroll = false;
        if ($(navbar).is(':visible')) {
          if ($.scrollTo) {
            do_scroll = true;
          } else {
            console.log('$.scrollTo not found');
          }
        }
        if (do_scroll) {
          // console.log("scrollTo", node);
          if (!($(node).isOnScreen())) {
            $(sidebar).scrollTo($(node), {
              axis: 'y',
              offset: { top: -100 }
            });
          }
        }
      } else {
        console.log('sidebar is', sidebar);
        console.log('navbar is', navbar);
      }
    }

    this.set_navbar_top = function(nodeurl)

      ($('#navbar-top')
        .find('a.reference.internal')
        .removeClass('youarehere')
      );

      ($('#navbar-top')
        .find('a.reference.internal[href="' + nodeurl + '"]')
        .addClass('youarehere')
      );
    }

    this.set_navbar = function(nodeurl)

      var navbar = $('#sidebar-wrapper').find('div.sidebar').first()[0];

      ($(navbar)
        .find('a.youarehere')
        .removeClass('youarehere')
      );

      var navbarlink = $(navbar).find('a[href="' + nodeurl + '"]');
      if (navbarlink) {
        navbarlink.addClass('youarehere');
        console.log(navbarlink);
        try {
          navbar_scrollto(navbarlink.first()); // # navbar a.youarehere
        } catch(e) {
          console.log('navbar_scrollto(navbarlink.first()): err');
          console.log(e);
        }
      } else {
        // TODO: walk upwards for nearest heading?
        var content = $('#content-wrapper');
        var content_link = $(content).find('a[ref="' + nodeurl + '"]');
        var headerlinks = (
          $(content_link)
            .closest('div.section')
              .find('a.headerlink'));

        //  _.one(headerlink)
        var headerlink = navbarlink.first();

        $(headerlink).addClass('youarehere');

        // TODO: [ ] find navbarlinks

        console.log("nodeurl not found");
        console.log(nodeurl);
      }

    this.navbar_update = function(nodeurl)

      console.log('navbar_update', nodeurl);

      if (nodeurl.match('^#index-[0-9]+')) {
        return;
      }
      var __node = $(nodeurl).first();
      if (!(__node)) {
        console.log('navbar_update: nodeurl not found', nodeurl)
        return
      } else {
        console.log('node', __node);
      }
      var content = $('#content-wrapper');
      var navbar = $('#sidebar-wrapper').find('div.sidebar').first()[0];
      ($(content)
        .find('a.headerlink.youarehere')
        .removeClass('youarehere')
        .text('¶')
      );
      if (nodeurl) {
        ($(content)
          .find('a.headerlink[href="' + nodeurl + '"]')
          .addClass('youarehere')
          .text('⬅')
        );

        set_navbar_top(nodeurl);

        set_navbar(nodeurl);
      } else {
        console.log("nodeurl is false");
        console.log(nodeurl);
      }
    }

    //this.navbar__remap_sphinx_toc_links = function()
    //  var content = $('#content-wrapper');
    //  ($(content)
    //    .find('a.headerlink')
    //    .map(function(i, node) {
    //      console.log(i, node);
    //      //$(node.previousSibling).attr('href', $(node).attr('href'));
    //    })
    //  );
    //}

    this.navbar__add_top_button = function()
      ($('<button type="button" class="toplink navbar-toggle"><a href="#" title="Top"><span>^</span></a></button>')
      .appendTo('body'));
    }

    this.navbar_init = function()
      // require('jquery.scrollto')
      //var scriptstr = '<script src="https://cdn.jsdelivr.net/jquery.scrollto/2.1.0/jquery.scrollTo.min.js"></script>';
      //$(scriptstr).appendTo("head");
      navbar_update(window.location.hash);

      navbar__remap_sphinx_toc_links();
      navbar__add_top_button();

      window.onhashchange = function(e) {
        // console.log(e); // e.newURL , e.oldURL
        var loc_hash_url = window.location.hash;
        console.log(loc_hash_url);
        if (loc_hash_url != false) {
          navbar_update(loc_hash_url);
        };
      };
    }
}

$(document).ready(navbar_init);

