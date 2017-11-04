from flask import Blueprint, request, url_for, make_response, jsonify, render_template, send_from_directory
import os, json

# import  rankit.build.rank_script.build_rank as build_rank
# import  pandas as pd

build_blueprint = Blueprint(
    'build', __name__,
    template_folder='templates'
)

def getDataset(dataset_name):
    # get the absolute path of the dataset
    # datasets_dir = os.path.dirname(os.path.dirname(os.getcwd() + "/rankit/datasets/"))

    datasets_dir = os.path.dirname(os.path.abspath(os.path.dirname(__name__)) + "/rankit/datasets/")
    print(datasets_dir)
    abs_file_path = os.path.join(datasets_dir, dataset_name)

    # load the json file contents into json object
    with open(abs_file_path, 'r') as data_file:
        datastore = json.load(data_file)
    return datastore

def filterByPrimaryKey(datastore):
    #filter only object names
    datastore_ids = list(map(lambda data: data["primaryKey"], datastore))
    datastore_ids.sort()

    return datastore_ids

@build_blueprint.route('/build/list/<dataset_name>')
def listComparison(dataset_name):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))

    return render_template('list_comparison.html', dataset_name = dataset_name, dataset=datastore_ids, view_name = "List Comparison")

@build_blueprint.route('/build/x')
def buildList():
    return render_template('full_datasets.html')

@build_blueprint.route('/build/pairwise/<dataset_name>')
def pairwise(dataset_name):
    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))

    return render_template('pairwise_comparison.html', dataset_name = dataset_name, dataset=datastore_ids, view_name = "Pairwise Comparison")

@build_blueprint.route('/build/categorical/<dataset_name>')
def categorical(dataset_name):

    # retrieve dataset
    datastore_ids = filterByPrimaryKey(getDataset(dataset_name))

    return render_template('categorical_comparison.html', dataset_name = dataset_name, dataset=datastore_ids, view_name = "Categorical Comparison")


@build_blueprint.route('/build/submit/', methods=["POST", "GET"])
def build():

    # dataset_name = request.form.get('dataset_name')
    # pairs_json = request.form.get('pairs')
    # pairsfile = dataset_name+"_pairsfile.json"
    #
    # with open(pairsfile, 'w') as f:
    #     json.dump(pairs_json, f)

    print("ranking...")

    # pairsfile = "sample_pairs.json"
    # dataset = pd.read_json("matters_data.json")
    # pairs = pd.read_json(pairsfile)
    #
    # rank = build_rank.build(dataset=dataset, pairs=pairs)
    # return rank.to_json()


