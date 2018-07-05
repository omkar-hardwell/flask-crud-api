"""Application logic."""
from oto import response
from src.logic.models import department, employee
from src import validator, constants


def get_department(department_id):
    """Get the department details against the given department id.
    :param department_id: str - Unique identification of department.
    :return: Department details against the given department id.
    """
    if not validator.is_number(department_id):
        return response.create_error_response(
            code=constants.ERROR_CODE_BAD_REQUEST,
            message=constants.ERROR_MESSAGE_BAD_REQUEST.format(
                title='department id', id=department_id))
    return department.get_department(department_id)


def get_employee(employee_id):
    """Get the employee details against the given employee id.
    :param employee_id: str - Unique identification of employee.
    :return: Employee details against the given employee id.
    """
    if not validator.is_number(employee_id):
        return response.create_error_response(
            code=constants.ERROR_CODE_BAD_REQUEST,
            message=constants.ERROR_MESSAGE_BAD_REQUEST.format(
                title='employee id', id=employee_id))
    return employee.get_employee(employee_id)


def delete_department(department_id):
    """Delete the department details against the given department id.
    :param department_id: str - Unique identification of department.
    :return: Success message on delete department details.
    """
    if not validator.is_number(department_id):
        return response.create_error_response(
            code=constants.ERROR_CODE_BAD_REQUEST,
            message=constants.ERROR_MESSAGE_BAD_REQUEST.format(
                title='department id', id=department_id))
    return department.delete_department(department_id)


def delete_employee(employee_id):
    """Delete the employee details against the given employee id.
    :param employee_id: str - Unique identification of employee.
    :return: Success message on delete employee details.
    """
    if not validator.is_number(employee_id):
        return response.create_error_response(
            code=constants.ERROR_CODE_BAD_REQUEST,
            message=constants.ERROR_MESSAGE_BAD_REQUEST.format(
                title='employee id', id=employee_id))
    return employee.delete_employee(employee_id)


def post_department(payload):
    """Add the department details.
    :param payload: json - Department details.
    :return: Department details added against the given data.
    """
    validate = validator.validate_request(payload, 'POST', 'department')
    if validate:
        return response.create_error_response(
            code=constants.ERROR_CODE_BAD_REQUEST, message=validate)
    return department.post_department(payload)


def post_employee(payload):
    """Add an employee details.
    :param payload: json - Employee details.
    :return: Employee details added against the given data.
    """
    validate = validator.validate_request(payload, 'POST', 'employee')
    if validate:
        return response.create_error_response(
            code=constants.ERROR_CODE_BAD_REQUEST, message=validate)
    return employee.post_employee(payload)


def put_department(department_id, payload):
    """Update the department details against the given department id.
    :param department_id: str - Unique identification of department.
    :param payload: json - Request body.
    :return: Success message on update of department details.
    """
    if not validator.is_number(department_id):
        return response.create_error_response(
            code=constants.ERROR_CODE_BAD_REQUEST,
            message=constants.ERROR_MESSAGE_BAD_REQUEST.format(
                title='department id', id=department_id))
    validate = validator.validate_request(payload, 'PUT', 'department')
    if validate:
        return response.create_error_response(
            code=constants.ERROR_CODE_BAD_REQUEST, message=validate)
    return department.put_department(department_id, payload)


def put_employee(employee_id, payload):
    """Update the employee details against the given employee id.
    :param employee_id: str - Unique identification of employee.
    :param payload: json - Request body.
    :return: Success message on update of employee details.
    """
    if not validator.is_number(employee_id):
        return response.create_error_response(
            code=constants.ERROR_CODE_BAD_REQUEST,
            message=constants.ERROR_MESSAGE_BAD_REQUEST.format(
                title='employee id', id=employee_id))
    validate = validator.validate_request(payload, 'PUT', 'employee')
    if validate:
        return response.create_error_response(
            code=constants.ERROR_CODE_BAD_REQUEST, message=validate)
    return employee.put_employee(employee_id, payload)
