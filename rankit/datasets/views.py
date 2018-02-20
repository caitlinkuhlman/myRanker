from flask import Blueprint, render_template


datasets_blueprint = Blueprint(
    'datasets', __name__,
    static_folder='static',
    template_folder='templates'
)


@datasets_blueprint.route('/dataset')
def datasets():
    return render_template('full_datasets.html')


