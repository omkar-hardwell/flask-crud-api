"""Application setup
   1) Swagger UI
   2) API routes
"""
import configs

from flask import Flask, jsonify
from flasgger import Swagger


# Application instance
app = Flask(configs.API_NAME)

# Swagger UI integration
app.config['SWAGGER'] = {
   'title': 'Flask Api - CRUD',
   'uiversion': 2
}
Swagger(app, template_file=configs.SWAGGER_SPEC_PATH)


@app.route(configs.BASE_PATH + '/hello', methods=['GET'])
def health():
    """Check the health of the application."""
    return jsonify({'status': 'ok'})
