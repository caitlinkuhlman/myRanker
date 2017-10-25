from flask import Blueprint, request, url_for
import pandas as pd
import  rankit.build.rank_script.build_rank as build_rank

build_blueprint = Blueprint(
    'build', __name__,
    template_folder='templates'
)


@build_blueprint.route('/build', methods=["POST"])
def build():
    print("ranking...")
    #rank = build_rank.build(dataset=dataset, pairsfile=pairsfile)



