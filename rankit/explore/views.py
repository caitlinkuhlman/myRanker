from flask import Blueprint, request, render_template, url_for
from rankit.build.views import getRanking, getDataset
import json

explore_blueprint = Blueprint(
    'explore', __name__,
    template_folder='templates'
)


@explore_blueprint.route('/explore/<dataset_name>')
def explore(dataset_name):

    data = json.dumps(getDataset(dataset_name))

    print(data)
    return render_template('explore.html', data=data)


@explore_blueprint.route('/explore/<dataset_name>/<primaryKeyPairs>')
def exploreJson(dataset_name, primaryKeyPairs):

    data = getRanking(dataset_name, primaryKeyPairs)

    return render_template('explore.html', data=data)



@explore_blueprint.route('/explore/<dataset_name>', methods=["POST"])
def explorePost(dataset_name):

    # get the dataset name from the request
    dataset_name = request.get_json().get("dataset_name")

    # get the pairs from client in json format
    primaryKeyPairs = request.get_json().get("pairs")

    data = getRanking(dataset_name, primaryKeyPairs)

    return render_template('explore.html', data=data)

