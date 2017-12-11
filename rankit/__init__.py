from flask import Flask
import logging, sys


app = Flask(__name__)
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app.config.from_object('config.DevelopmentConfig')


from rankit.home.views import home_blueprint
from rankit.build.views import build_blueprint
from rankit.explore.views import explore_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(build_blueprint)
app.register_blueprint(explore_blueprint)

