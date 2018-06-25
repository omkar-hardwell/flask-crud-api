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
