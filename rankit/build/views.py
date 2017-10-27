from flask import Blueprint, request, url_for, make_response
import  rankit.build.rank_script.build_rank as build_rank
import  pandas as pd

build_blueprint = Blueprint(
    'build', __name__,
    template_folder='templates'
)

@build_blueprint.route('/build/dataset', methods=["GET"])
def processDataset():
    dataset_name = request.args.lists()

    # dataset_name.get('dataset_name', default=-1, type="")
    dataset_name = list(dataset_name)
    # dataset_name = dataset_name.get('dataset_name', default=-1, type="")

    print("Dataset : %s  " % dataset_name)
    return dataset_name

@build_blueprint.route('/build/submit', methods=["POST"])
def build():

    print("ranking... ")

    # dataset = pd.read_csv("matters_indices_2014.csv")
    # pairsfile = "sample_pairs.csv"
    # pairs = pd.read_csv(pairsfile, header=None)

    #rank = build_rank.build(dataset=dataset, pairs=pairs)
    #return rank.to_json()




