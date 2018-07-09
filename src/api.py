"""Application setup
   1) Swagger UI
   2) API routes
"""
import configs

from flask import Flask, jsonify, request
from oto import response
from oto.adaptors.flask import flaskify
from flasgger import Swagger
from src import constants, validator
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
@validator.authorization(request)
def health():
    """Check the health of the application.
    :return: Status of application.
    """
    return jsonify({'status': 'ok'})


@app.route(
    configs.BASE_PATH + '/department/<department_id>', methods=['GET'])
@validator.authorization(request)
def get_department(department_id):
    """Get the department details against the given department id.
    :param department_id: str - Unique identification of department.
    :return: Department details against the given department id.
    """
    return flaskify(logic.get_department(department_id))


@app.route(
    configs.BASE_PATH + '/employee/<employee_id>', methods=['GET'])
@validator.authorization(request)
def get_employee(employee_id):
    """Get the employee details against the given employee id.
    :param employee_id: str - Unique identification of department.
    :return: Employee details against the given employee id.
    """
    return flaskify(logic.get_employee(employee_id))


@app.route(
    configs.BASE_PATH + '/department/<department_id>', methods=['DELETE'])
@validator.authorization(request)
def delete_department(department_id):
    """Delete the department details against the given department id.
    :param department_id: str - Unique identification of department.
    :return: Success message on delete department details.
    """
    return flaskify(logic.delete_department(department_id))


@app.route(
    configs.BASE_PATH + '/employee/<employee_id>', methods=['DELETE'])
@validator.authorization(request)
def delete_employee(employee_id):
    """Delete the employee details against the given employee id.
    :param employee_id: str - Unique identification of employee.
    :return: Success message on delete employee details.
    """
    return flaskify(logic.delete_employee(employee_id))


@app.route(
    configs.BASE_PATH + '/department', methods=['POST'])
@validator.authorization(request)
def post_department():
    """Add the department details.
    :param: request json - Request body.
    :return: Department details added against the given data.
    """
    return flaskify(logic.post_department(request.get_json()))


@app.route(
    configs.BASE_PATH + '/employee', methods=['POST'])
@validator.authorization(request)
def post_employee():
    """Add an employee details.
    :param: request json - Request body.
    :return: Employee details added against the given data.
    """
    return flaskify(logic.post_employee(request.get_json()))


@app.route(
    configs.BASE_PATH + '/department/<department_id>', methods=['PUT'])
@validator.authorization(request)
def put_department(department_id):
    """Update the department details against the given department id.
    :param department_id: str - Unique identification of department.
    :return: Success message on update of department details.
    """
    return flaskify(logic.put_department(department_id, request.get_json()))


@app.route(
    configs.BASE_PATH + '/employee/<employee_id>', methods=['PUT'])
@validator.authorization(request)
def put_employee(employee_id):
    """Update the employee details against the given employee id.
    :param employee_id: str - Unique identification of employee.
    :return: Success message on update of employee details.
    """
    return flaskify(logic.put_employee(employee_id, request.get_json()))
