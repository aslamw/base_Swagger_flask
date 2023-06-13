from flask import Flask
from flask_swagger import swagger
from .config import swaggerui_blueprint, SWAGGER_URL
app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'teste_swagger',
    'uiversion': 3
}

from src import routes

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)