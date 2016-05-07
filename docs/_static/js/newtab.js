
// newtab.js
// * https://mathiasbynens.github.io/rel-noopener/
$(document).ready(function() {

  var options = {
    'open_in_new_tab': true,
    'show_visited_links': true,
  };
  console.log('options:');
  console.log(options);

  $(document).on('click', 'a', function(e) {
    if (options['open_in_new_tab']) {
      var url = $(this).attr('href');
      if (url.substring(0,4) === 'http') {
        e.preventDefault();
        var otherWindow = window.open();
        otherWindow.opener = null;
        otherWindow.location = url;
      }
    }
  });

  var sidebar = $("#sidebar-wrapper").find("div.sidebar");
      var options_widget = $("\
  <div class='widget'> \
    <h3>Options</h3> \
    <ul> \
      <li> \
        <input id='chk_newtab' \
          type='checkbox' \
          aria-label='Open links in a new tab' \
          title='Open links in a new tab' \
        ></input> \
        <label for='chk_newtab'>Open links in a new tab</label> \
      </li> \
      <li> \
        <input id='chk_showvisited' \
          type='checkbox' \
          aria-label='Show visited links' \
          title='Show visited links' \
        ></input> \
        <label for='chk_showvisited'>Show visited links</label> \
      </li> \
    </ul> \
  </div>");
  sidebar.append(options_widget);

  var chk = $('input#chk_newtab');
  chk.prop('checked', options['open_in_new_tab']);
  chk.on('change', function(e) {
    options['open_in_new_tab'] = this.checked;
  });


  // show_visited_links
  var localstate = { };
  function set_showvisitedcss() {
    var stylesheet = document.styleSheets[0];
    if (options['show_visited_links'] === true) {
      localstate['show_visited_links/a:visited/color'] = (
        stylesheet.insertRule('a:visited { color: #a0a !important; }',
                             stylesheet.cssRules.length)
      );
    } else {
      var ruleidx = localstate['show_visited_links/a:visited/color'];
      if (ruleidx !== undefined) {
        if (stylesheet.cssRules) {
          if (stylesheet.cssRules.length) {
            stylesheet.deleteRule(ruleidx);
          }
        } else { // IE < 9
          if (stylesheet.rules.length) {
            stylesheet.removeRule(ruleidx);
          }
        }
      }
      localstate['show_visited_links/a:visited/color'] = undefined;
    }
  }
  set_showvisitedcss();

  var chk = $('input#chk_showvisited');
  chk.prop('checked', options['show_visited_links']);
  chk.on('change', function(e) {
    options['show_visited_links'] = this.checked;
    set_showvisitedcss();
  });
});

