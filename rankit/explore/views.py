from flask import Blueprint, request, render_template
from rankit.build.utils import getRanking
from  rankit.datasets.utils import getDataset

import json, re

explore_blueprint = Blueprint(
    'explore', __name__,
    template_folder='templates'
)


@explore_blueprint.route('/explore/<dataset_name>/')
def explore(dataset_name):

    data = json.dumps(getDataset(dataset_name))

    return render_template('explore.html', weights=None, data=data, dataset_name=dataset_name, list=None)


@explore_blueprint.route('/explore/<dataset_name>/<pairs>')
def exploreJson(dataset_name, pairs):
    primaryKeyPairs = []
    parsed_pairs = re.findall("\d+=([\w\s'-:!\.,()]*[\>]{1}[\w\s'-:!\.,()]*)&", pairs)

    # for pair in parsed_pairs:
    #     high, low = pair.split('>')
    #     primaryKeyPairs.append({'high': high, 'low' : low})
    list = []


    for pair in parsed_pairs:
        high, low = pair.split('>')
        if (high not in list): list.append(high)
        if (low not in list): list.append(low)
        primaryKeyPairs.append({'high': high, 'low' : low})

    data, weights = getRanking(dataset_name, primaryKeyPairs)

    return render_template('explore.html', weights=weights, data=data, dataset_name=dataset_name, list=list)
