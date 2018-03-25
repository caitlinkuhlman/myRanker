from flask import Blueprint, render_template
from rankit.build.utils import filterByPrimaryKey
from  rankit.datasets.utils import getDataset
from rankit.build.utils import getRanking
import json


build_blueprint = Blueprint(
    'build', __name__,
    template_folder='templates'
)

# Routes
@build_blueprint.route('/build/<dataset_name>')
def buildStart(dataset_name):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))
    data = json.dumps(getDataset(dataset_name))

    return render_template('build.html', dataset_name = dataset_name, dataset=datastore_ids, data=data, ranked_data=None, weights=None, confidence=0)

# List Comparison
@build_blueprint.route('/build/<dataset_name>/lc')
def lc(dataset_name):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))
    data = json.dumps(getDataset(dataset_name))

    return render_template('lc.html', dataset_name = dataset_name, dataset=datastore_ids, data=data, ranked_data=None, weights=None, confidence=0)

# Categorical Comparison
@build_blueprint.route('/build/<dataset_name>/cc')
def cc(dataset_name):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))
    data = json.dumps(getDataset(dataset_name))

    return render_template('cc.html', dataset_name = dataset_name, dataset=datastore_ids, data=data, ranked_data=None, weights=None, confidence=0)

# Pairwise Comparison
@build_blueprint.route('/build/<dataset_name>/pwc')
def pwc(dataset_name):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))
    data = json.dumps(getDataset(dataset_name))

    return render_template('pwc.html', dataset_name = dataset_name, dataset=datastore_ids, data=data, ranked_data=None, weights=None, confidence=0)

# Run script in build
@build_blueprint.route('/build/<dataset_name>/<method>/<pairs>')
def getConfidence(dataset_name, method, pairs):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))
    data = json.dumps(getDataset(dataset_name))

    primaryKeyPairs = []
    parsed_pairs = re.findall("\d+=([\w\s'-:!\.,()]*[\>]{1}[\w\s'-:!\.,()]*)&", pairs)
    
    for pair in parsed_pairs:
        high, low = pair.split('>')
        primaryKeyPairs.append({'high': high, 'low' : low})

    ranked_data, weights, confidence = getRanking(dataset_name, primaryKeyPairs)

    return render_template(method+'.html', dataset_name = dataset_name, dataset=datastore_ids, data=data, ranked_data=ranked_data, weights=weights, confidence=confidence)

