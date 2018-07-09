"""Application constants"""
GENDER = ['male', 'female']

# HTTP response error messages
ERROR_MESSAGE_NOT_FOUND = 'Requested {title} {id} not found.'
ERROR_MESSAGE_BAD_REQUEST = \
    '{title} - {id} must be integer and greater than zero'
ERROR_MESSAGE_INTERNAL_ERROR = 'Internal server error'
ERROR_MESSAGE_UNAUTHORIZED_ACCESS = \
    'Authentication failed. Please use valid api key for access.'

# HTTP response error codes
ERROR_CODE_BAD_REQUEST = 'bad_request'
ERROR_CODE_UNAUTHORIZED_REQUEST = 'unauthorized'

# HTTP response success messages
DELETE_MESSAGE = '{module} detail successfully removed for {title} {id}'
UPDATE_MESSAGE = '{module} detail successfully updated for {title} {id}'

# Constants for validation
VALIDATION_DEPARTMENT_POST_AND_PUT = {
    'required_fields': ['name']
}
VALIDATION_EMPLOYEE_POST_AND_PUT = {
    'required_fields': ['name', 'department_id'],
    'integer_fields': ['department_id']
}

# Application key for authentication
API_KEY_IN_HEADER = 'Flask-Crud-Api-Key'
API_KEY = 'ebbf2878c8560d620022c781679347a9'
