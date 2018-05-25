
/* load popovers */
$(document).ready(function () {
  $('[data-toggle="popover"]').popover();

  //displayAttributesAfterRender()
  
  $('#lc').attr('href', 'lc')
  $('#cc').attr('href', 'cc')
  $('#pwc').attr('href', 'pwc')
})



$('.popover-dismiss').popover({
  trigger: 'focus'
})



$('body').on('click', function (e) {
  // did not click a popover toggle or popover
  if ($(e.target).data('toggle') !== 'popover'
  && $(e.target).parents('.popover.in').length === 0) {
    $('[data-toggle="popover"]').popover('hide');
  }
});

function displayAttributesAfterRender() {
    objects = Array.from(document.querySelector('#top').children)
  
    for (var i=0; i<objects.length; i++) {
      var object = findObject(objects[i].innerText)
      var text = "<table class='data-pool-popover'><tr><th>Attribute</th><th>Value</th></tr>";
      for (var propt in object) {
        text = text + "<tr><td>" + propt + "</td><td>" + object[propt]+"</td></tr>";
      }
      text = text + "</table>"
      document.getElementById(objects[i].innerText).setAttribute("data-content", text)
    }
}