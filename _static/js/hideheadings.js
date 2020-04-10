
// show or hide toc entries according to 


function hide_toc_entries(root, level) {
   var max_heading_level = 10;
   var node = $(root);
   for (var i=0; i < level; i++) {
      hdrstr = 'li';
      for (var j=0; j<i; j++) {
         hdrstr += ' li';
      }
      console.log(['show', hdrstr]);
      node.find(hdrstr).show();
   }
   for (var i=level; i < max_heading_level; i++) {
      hdrstr = 'li';
      for (var j=0; j<i; j++) {
         hdrstr += ' li';
      }
      console.log(['hide', hdrstr]);
      node.find(hdrstr).hide();
   }
}

hide_toc_entries(toc, 1);


function find_deepest_elem(root, elemtype) {
   var max_level = 10;
   var node = $(root);
   var prevset = node.find(elemtype);
   for (var i=1; i < max_level; i++) {
      if (prevset.length) {
         prevset = prevset.find(elemtype);
      } else {
         return i-1;
      }
   }
}

find_deepest_elem(toc, 'li');


function add_slider(root, sliderId, currentValue, min, max) {
   var node = $(root);
   node.append(`<div class="slidecontainer"><input type="range" min="${min}" max="${max}" value="${currentValue}" class="slider" id="${sliderId}"></div>`);


}
