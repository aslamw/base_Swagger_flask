from flask_swagger import swagger

from flask_swagger_ui import get_swaggerui_blueprint
from flask import jsonify


SWAGGER_URL = '/api/docs'  # Rota para acessar a interface Swagger UI
API_URL = '/api/swagger.json'  # Rota para o arquivo swagger.json gerado pelo Flask-Swagger

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "MyAPI"
    }
)
@app.route('/api/swagger.json')
def swagger_json():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "MyAPI"
    return jsonify(swag)
