
/* load popovers */
$(document).ready(function () {
  
  shuffleDataset()
  displayAttributesAfterRender()
  $('#lc').attr('href', 'lc')
  $('#cc').attr('href', 'cc')
  $('#pwc').attr('href', 'pwc')
  
  $('[data-toggle="popover"]').popover();
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

function sortDataset() {
	  const dataset = getDataset()
	  dataset.sort()
	  render(dataset)
	}

function shuffleDataset() {
	  const dataset = getDataset()
	  for (let i = dataset.length - 1; i > 0; i--) {
	    const j = Math.floor(Math.random() * (i + 1));
	    [dataset[i], dataset[j]] = [dataset[j], dataset[i]];
	  }
	  render(dataset)
	}

function searchDataset(e) {
    let difference = dataset.filter(x => getRankedObjects().indexOf(x) == -1)
    const value = e.target.value
    const re = new RegExp(value, 'i')
    const newDataset = difference.filter(x => re.test(x))
    render(newDataset)
  }

function render(dataset) {
	  const pool = document.querySelector('#top')
	  const html = dataset.map(x => `<div tabindex="0" id="${x}" class="object noSelect pop" data-toggle="popover" data-trigger="focus" data-html="true">${x}</div>`).join('\n')
	  pool.innerHTML = html
	}
