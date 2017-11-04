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


@build_blueprint.route('/build/submit/', methods=["POST"])
def build():
    # get the pairs from client in json format
    primaryKeyPairs = request.get_json().get("pairs")
    print(primaryKeyPairs)

    # get the dataset from json file in list format
    dataset_list = getDataset(request.get_json().get("dataset_name"))

    # convert each primary key into index in pairs sent from client
    primaryKeyToIndex(dataset_list, primaryKeyPairs)
    print(primaryKeyPairs)

    pairs_json = json.dumps(primaryKeyPairs)
    # pairs = pd.read_json(pairs_json)
    # print(pairs)
    # dataset = pd.read_json(dataset_name)

    # pairsfile = "sample_pairs.json"
    # dataset = pd.read_json(json.dumps(dataset_list))
    # print(dataset)
    # pairs = pd.read_json(pairsfile)

    # rank = build_rank.build(dataset=dataset, pairs=pairs)
    # return rank.to_json()
    return "1"


def primaryKeyToIndex(dataset_list, primaryKeyPairs):
    for obj in primaryKeyPairs:
        for key in obj:
            # obj[high], obj[low]
            primKey = obj[key]
            index = findIndex(primKey, dataset_list)
            obj[key] = index


def findIndex(primKey, dataset_list):
    index = 0
    for list_entry in dataset_list:
        if list_entry["primaryKey"] == primKey:
            print(index)
            return index
        else:
            index = index + 1



