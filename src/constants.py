"""Application constants"""
GENDER = ['male', 'female']

# HTTP response error messages
ERROR_MESSAGE_NOT_FOUND = 'Requested {title} {id} not found.'
ERROR_MESSAGE_BAD_REQUEST = \
    '{title} - {id} must be integer and greater than zero'
ERROR_MESSAGE_INTERNAL_ERROR = 'Could not connect to MySQL.'

# HTTP response error codes
ERROR_CODE_BAD_REQUEST = 'bad_request'

# Endpoint messages
DELETE_MESSAGE = '{module} detail successfully removed for {title} {id}'
DUPLICATE_KEY_MESSAGE = 'Duplicate entry found for {title} - {id}'

# Constants for validation
VALIDATION_DEPARTMENT_POST = {
    'missing_fields': ['department_id', 'name'],
    'integer_fields': ['department_id']
}
VALIDATION_EMPLOYEE_POST = {
    'required_fields': ['name', 'department_id'],
    'integer_fields': ['department_id']
}
