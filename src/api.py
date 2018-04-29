"""Application"""
import configs

from flask import Flask
from flasgger import Swagger


# Application instance
app = Flask(configs.API_NAME)

app.config['SWAGGER'] = {
   'title': 'Flask Api - CRUD',
   'uiversion': 2
}
Swagger(app, template_file=configs.SWAGGER_SPEC_PATH)
