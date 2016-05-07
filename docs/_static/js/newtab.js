
// newtab.js
$(document).ready(function() {
    $(document).on('click', 'a', function(e) {
        var url = $(this).attr('href');
        if (url.substring(0,4) === 'http') {
            e.preventDefault();
            var otherWindow = window.open();
            otherWindow.opener = null;
            otherWindow.location = url;
        }
    });
});
