from flask import FLASK
app = Flask(__name__)

#Register blueprints or routes
from .routes import api
app.register_blueprint(api)
