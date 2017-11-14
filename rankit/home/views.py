from flask import render_template, Blueprint, request

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)

@home_blueprint.route('/')
def index():
    return render_template('index.html')

@home_blueprint.route('/about')
def about():
    return render_template('about.html')

@home_blueprint.route('/team')
def team():
    return render_template('team.html')

@home_blueprint.route('/login')
def login():
    return render_template('modal_log_in.html')
