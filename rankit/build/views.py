from flask import Blueprint, request, url_for

build_blueprint = Blueprint(
    'build', __name__,
    template_folder='templates'
)

@build_blueprint.route('build/dataset', methods=["GET"])
def processDataset():
    dataset_name = request.args.lists()

    # dataset_name.get('dataset_name', default=-1, type="")
    dataset_name = list(dataset_name)
    # dataset_name = dataset_name.get('dataset_name', default=-1, type="")

    print("Dataset : %s  " % dataset_name)
    return dataset_name

@build_blueprint.route('/build/submit', methods=["POST"])
def build():
    print("ranking...")
    # rank = build_rank.build(dataset=dataset_name, pairsfile=pairsfile)
    # return rank


