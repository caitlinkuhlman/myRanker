from flask import Blueprint, request, url_for, make_response, jsonify, render_template, send_from_directory
import os, json

# import  rankit.build.rank_script.build_rank as build_rank
# import  pandas as pd

build_blueprint = Blueprint(
    'build', __name__,
    template_folder='templates'
)

@build_blueprint.route('/buildListComp')
def buildListComp():
    return render_template('buildListComp.html')


@build_blueprint.route('/buildListComp/<dataset_name>')
def processDataset(dataset_name):
    # get the arguments from get request
    # dataset_name = request.args.get("dataset_name")

    # get the absolute path of the dataset
    # datasets_dir = os.path.dirname(os.path.dirname(os.getcwd() + "/rankit/datasets/"))
    datasets_dir = os.path.dirname(os.path.abspath(os.path.dirname(__name__)) + "/rankit/datasets/")
    print(datasets_dir)
    abs_file_path = os.path.join(datasets_dir, dataset_name)

    # load the json file contents into json object
    with open(abs_file_path, 'r') as data_file:
        datastore = json.load(data_file)

    #filter only object names
    datastore_ids = list(map(lambda data: data["States"], datastore))
    datastore_ids.sort()

    return render_template('buildListComp.html', dataset=datastore_ids)


@build_blueprint.route('/build/submit', methods=["POST"])
def build():

    # dataset_name = request.form.get('dataset_name')
    # pairs_json = request.form.get('pairs')
    # pairsfile = dataset_name+"_pairsfile.json"
    #
    # with open(pairsfile, 'w') as f:
    #     json.dump(pairs_json, f)

    print("ranking...")
    #rank = build_rank.build(dataset=dataset, pairsfile=pairsfile)
    # rank = build_rank.build(dataset=dataset_name, pairsfile=pairsfile)

    # dataset = pd.read_csv("matters_indices_2014.csv")
    # pairsfile = "sample_pairs.csv"
    # pairs = pd.read_csv(pairsfile, header=None)

    #rank = build_rank.build(dataset=dataset, pairs=pairs)
    #return rank.to_json()



