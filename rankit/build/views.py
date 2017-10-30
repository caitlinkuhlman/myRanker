
from flask import Blueprint, request, url_for, make_response, jsonify, render_template
import os, json

import  rankit.build.rank_script.build_rank as build_rank
import  pandas as pd

build_blueprint = Blueprint(
    'build', __name__,
    template_folder='templates'
)

@build_blueprint.route('/build/dataset', methods=["GET"])
def processDataset():
    # get the arguments from get request
    dataset_name = request.args.get("dataset_name", "alternative")

    # get the absolute path of the dataset
    datasets_dir = os.path.dirname("/Users/Malikusha/myRanker/rankit/datasets/")
    abs_file_path = os.path.join(datasets_dir, dataset_name)

    # load the json file contents into json object
    with open(abs_file_path, 'r') as data_file:
        datastore = json.load(data_file)

    print("Dataset : %s " % dataset_name)

    # send json object containing all the data from selected dataset to client
    return render_template("buildListComp.html", dataset_json=jsonify(datastore))

@build_blueprint.route('/build/submit', methods=["POST"])
def build():

    # dataset_name = request.form.get('dataset_name')
    # pairs_json = request.form.get('pairs')
    # pairsfile = dataset_name+"_pairsfile.json"
    #
    # with open(pairsfile, 'w') as f:
    #     json.dump(pairs_json, f)

    print("ranking...")
    # rank = build_rank.build(dataset=dataset_name, pairsfile=pairsfile)

    # dataset = pd.read_csv("matters_indices_2014.csv")
    # pairsfile = "sample_pairs.csv"
    # pairs = pd.read_csv(pairsfile, header=None)

    #rank = build_rank.build(dataset=dataset, pairs=pairs)
    #return rank.to_json()



