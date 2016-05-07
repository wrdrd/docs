
// newtab-noopener.js
// http://caniuse.com/#feat=rel-noopener (Chrome, Opera, )
$(document).ready(function() {
    var urls = $("a[href^='http']");
    urls.attr('target','_blank');
    $.map(urls, function(val, i) {
        var rel = val.attr('rel');
        $(val).attr('rel', rel + ' noopener'); // rel=noopener
    })
});
