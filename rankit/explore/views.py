from flask import Blueprint, request, render_template
from rankit.build.views import getRanking, getDataset
import json, re

explore_blueprint = Blueprint(
    'explore', __name__,
    template_folder='templates'
)


@explore_blueprint.route('/explore/<dataset_name>/')
def explore(dataset_name):

    data = json.dumps(getDataset(dataset_name))

    return render_template('explore.html', data=data, dataset_name=dataset_name)


@explore_blueprint.route('/explore/<dataset_name>/<pairs>')
def exploreJson(dataset_name, pairs):

    primaryKeyPairs = []
    parsed_pairs = re.findall("\d+=([\w\s'-:]*[,]{1}[\w\s'-]*)&", pairs)
    for pair in parsed_pairs:
        high, low = pair.split(',')
        primaryKeyPairs.append({'high': high, 'low' : low})

    data, weigths = getRanking(dataset_name, primaryKeyPairs)


    return render_template('explore.html', weigths=weigths, data=data, dataset_name=dataset_name)



@explore_blueprint.route('/explore/<dataset_name>', methods=["POST"])
def explorePost(dataset_name):

    # get the dataset name from the request
    # dataset_name = request.get_json().get("dataset_name")

    # get the pairs from client in json format
    primaryKeyPairs = request.get_json().get("pairs")

    data, weigths = getRanking(dataset_name, primaryKeyPairs)

    return render_template('explore.html', weigths=weigths, data=data, dataset_name=dataset_name)

