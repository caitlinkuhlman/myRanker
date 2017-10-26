from flask import Blueprint, request, url_for, make_response
import  rankit.build.rank_script.build_rank as build_rank
import  pandas as pd

build_blueprint = Blueprint(
    'build', __name__,
    template_folder='templates'
)


@build_blueprint.route('/build/test')
def build():

    pairsfile = "sample_pairs.csv"
    dataset = pd.read_csv("matters_indices_2014.csv")
    # normalize(dataset)
    pairs = pd.read_csv(pairsfile, header=None)

    rank = build_rank.build(dataset=dataset, pairs=pairs)

    # output = make_response(rank.to_csv())
    # output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    # output.headers["Content-type"] = "text/csv"
    return rank.to_json()

