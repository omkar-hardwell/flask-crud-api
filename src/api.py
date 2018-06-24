"""Application setup
   1) Swagger UI
   2) API routes
"""
import configs

from flask import Flask, jsonify
from oto import response
from oto.adaptors.flask import flaskify
from flasgger import Swagger
from src import constants
from src.logic import logic


# Application instance
app = Flask(configs.API_NAME)

# Swagger UI integration
app.config['SWAGGER'] = {
   'title': 'Flask Api - CRUD',
   'uiversion': 2
}
Swagger(app, template_file=configs.SWAGGER_SPEC_PATH)


@app.errorhandler(500)
def internal_error(error):
    return response.create_fatal_response(
        constants.ERROR_MESSAGE_INTERNAL_ERROR)


@app.route(configs.BASE_PATH + '/hello', methods=['GET'])
def health():
    """Check the health of the application.
    :return: Status of application.
    """
    return jsonify({'status': 'ok'})


@app.route(
    configs.BASE_PATH + '/department/<department_id>', methods=['GET'])
def get_department(department_id):
    """Get the department details against the given department id.
    :param department_id: str - Unique identification of department.
    :return: Department details against the given department id.
    """
    return flaskify(logic.get_department(department_id))


@app.route(
    configs.BASE_PATH + '/employee/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    """Get the employee details against the given employee id.
    :param employee_id: str - Unique identification of department.
    :return: Employee details against the given employee id.
    """
    return flaskify(logic.get_employee(employee_id))
