from flask import Blueprint, render_template
from rankit.build.utils import filterByPrimaryKey
from  rankit.datasets.utils import getDataset


build_blueprint = Blueprint(
    'build', __name__,
    template_folder='templates'
)

# Routes
@build_blueprint.route('/build/<dataset_name>')
def buildStart(dataset_name):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))

    return render_template('build.html', dataset_name = dataset_name, dataset=datastore_ids)

# List Comparison
@build_blueprint.route('/build/<dataset_name>/lc')
def lc(dataset_name):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))

    return render_template('lc.html', dataset_name = dataset_name, dataset=datastore_ids)

# Categorical Comparison
@build_blueprint.route('/build/<dataset_name>/cc')
def cc(dataset_name):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))

    return render_template('cc.html', dataset_name = dataset_name, dataset=datastore_ids)

# Pairwise Comparison
@build_blueprint.route('/build/<dataset_name>/pwc')
def pwc(dataset_name):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))

    return render_template('pwc.html', dataset_name = dataset_name, dataset=datastore_ids)

