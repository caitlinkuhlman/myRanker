function findMin(weights) {
  var current_min = weights[0].weight
  for (i=0; i<weights.length; i++){
    if (current_min > weights[i].weight) {
      current_min = weights[i].weight
    }
  }
  return current_min
}


function findMax(weights) {
  var current_max = weights[0].weight
  for (i=0; i<weights.length; i++){
    if (current_max < weights[i].weight) {
      current_max = weights[i].weight
    }
  }
  return current_max
}


function normalize(val, min, max) {
  return (val-min)/(max-min)
}


function normalizeWeights(data) {
  var dict = []
  min = findMin(data)
  max = findMax(data)
  for (i=0; i<data.length; i++){
    current_normalized = normalize(data[i].weight, min, max);
    dict.push({
      "attribute": data[i].attribute,
      "weight": current_normalized
    });
  }
  return dict
}

function roundTo(n, digits) {
  if (digits === undefined) {
    digits = 0;
  }

  var multiplicator = Math.pow(10, digits);
  n = parseFloat((n * multiplicator).toFixed(11));
  var test =(Math.round(n) / multiplicator);
  return +(test.toFixed(digits));
}

function sumToOne(data) {
  var dict = []
  var sum = 0
  for (i=0; i<data.length; i++){
    if (data[i].weight < 0) {
      sum = sum + (-1)*data[i].weight
    } else {
      sum = sum + data[i].weight
    }
  }

  for (j=0; j<data.length; j++) {
    if (data[j].weight < 0) {
      dict.push({
        "attribute": data[j].attribute,
        "weight": roundTo((-1)*(data[j].weight/sum), 2)
      });

    } else {
      dict.push({
        "attribute": data[j].attribute,
        "weight": roundTo(data[j].weight/sum, 2)
      });
    }
  }
  return dict
}

// dict has a format:
// [
//  {
//    attribute: <attribute1>,
//    weight: <weight1>
//  }
//  {
//    attribute: <attribute2>,
//    weight: <weight2>
//  }
// ]
// To access: dict[0].attribute -> attribute1
//            dict[1].weight -> weight2


///////////////////////////

function renderTable(data) {
  var tempData = data[0];
  var keys = renderHead(data[0]);

  var table =  $('#table').DataTable({
    scrollY: '100vh',
    scrollCollapse: true,
    pageLength: 25,
    searching: true
    //fixedColumns: {
    //    leftColumns: 3
    //}
  })

  $('#table').on('draw.dt', function(e) {
    highlightRows();
    shadeRowsByconf(data);
  })

  renderData(data, keys)

}

function renderHead(datum) {
  const title = 'Title'
  const rank = 'Rank'
  const score = 'Score'
  var w = 'Weights = '
  var data = Object.keys(datum)

  if (data.indexOf(score) > 0) {
    data.splice(data.indexOf(score), 1);
    data.unshift(score);
  }
  if (data.indexOf(title) > 0) {
    data.splice(data.indexOf(title), 1);
    data.unshift(title);
  }
  if (data.indexOf(rank) > 0) {
    data.splice(data.indexOf(rank), 1);
    data.unshift(rank);
  }

  const thead = data
  .map(k => `<th>${k}</th>`)
  .join('\n')


  document.querySelector('#head').innerHTML = thead
  return data
}

function setBarColor(dataConf) {
  //return highlightColor(dataConf, "#FB8072", "#3F3A3C")
  return "#6a6265";
}

function renderData(data, keys) {
  var t = $('#table').dataTable();


  let maxScore = -1; // Is this true?? can a score be negative
  data.forEach(function(row) {
    if (row.Score > maxScore) {
      maxScore = row.Score;
    }

  });


  const html = data.map(x => {
    const dataScore = x.Score;
    const dataConf = x.Confidence;
    x.Score = `
    <div class="bar-chart-bar">
    <div class="inTableBar" style="width: ${(dataScore / ((maxScore !== 0) ? maxScore : 0.01)) * 100}%;background-color:${setBarColor(dataConf)}"></div>
    </div>
    `
    var props = keys
    .map(k => x[k])
    t.fnAddData(props, false);
  }
)

t.fnDraw();

}

function searchTable(e) {
  var value = e.target.value;
  var table = $('#table').DataTable();
  table.search( value ).draw();
}

function parseData(raw) {
  return JSON.parse(raw.substring(1, raw.length - 1))
}
