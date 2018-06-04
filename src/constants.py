"""Application constants"""
GENDER = ['male', 'female']

# HTTP response error messages
ERROR_MESSAGE_NOT_FOUND = 'Requested {title} {id} not found.'
ERROR_MESSAGE_BAD_REQUEST = '{id} must be integer and greater than zero'
ERROR_MESSAGE_INTERNAL_ERROR = 'Could not connect to MySQL.'

# HTTP response error codes
ERROR_CODE_BAD_REQUEST = 'bad_request'
