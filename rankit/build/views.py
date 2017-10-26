from flask import Blueprint, render_template, request, url_for

build_blueprint = Blueprint(
    'build', __name__,
    template_folder='templates'
)

@build_blueprint.route('/buildListComp')
def buildListComp():
    return render_template('buildListComp.html')



@build_blueprint.route('/build/submit', methods=["POST"])
def build():
    request.form
    print("ranking...")
    #rank = build_rank.build(dataset=dataset, pairsfile=pairsfile)
