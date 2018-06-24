"""Application logic."""
from oto import response
from src.logic.models import department
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
                id=department_id))
    return department.get_department(department_id)
