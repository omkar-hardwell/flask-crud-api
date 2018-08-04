"""Validation for API methods."""
import datetime
from functools import wraps
from oto import response, status as oto_status
from oto.adaptors.flask import flaskify
from src import constants


def is_number(value):
    """Check value is digit.
    :param value: str
    :return: boolean
    """
    if value.isdigit():
        return True
    return False


def is_float(value):
    """Check value is float.
    :param value: str
    :return: boolean
    """
    try:
        float(value)
        # check for nan/infinity etc.
        if value.isalpha():
            return False
        return True
    except ValueError:
        return False


def validate_request(payload, request_type, model):
    """Validate POST and PUT request.
    :param payload: json
    :param request_type: str
    :param model: str
    :return: list
    """
    validation_message = []
    if not payload:
        return 'Request should not be empty'
    if request_type == 'POST' and model == 'department':
        missing_fields_list = missing_fields(
            payload,
            constants.VALIDATION_DEPARTMENT_POST_AND_PUT['required_fields'])
        if missing_fields_list:
            validation_message.append(missing_fields_list)
    elif request_type == 'POST' and model == 'employee':
        missing_fields_list = missing_fields(
            payload,
            constants.VALIDATION_EMPLOYEE_POST_AND_PUT['required_fields'])
        if missing_fields_list:
            validation_message.append(missing_fields_list)
        non_numeric_fields = numeric_fields(
            payload,
            constants.VALIDATION_EMPLOYEE_POST_AND_PUT['integer_fields'])
        if non_numeric_fields:
            validation_message.append(non_numeric_fields)
        if not validate_date(payload.get('date_of_joining')):
            validation_message.append({
                'invalid date format':
                    'Date of joining should be in valid YYYY-MM-DD format'})
        if payload.get('gender') not in constants.GENDER:
            validation_message.append({
                'invalid gender value': 'Gender should be male or female'})
        if not is_float(str(payload.get('salary'))):
            validation_message.append({
                'invalid salary value': 'Salary should be like 2000.00'})
    elif request_type == 'PUT' and model == 'department':
        missing_fields_list = missing_fields(
            payload,
            constants.VALIDATION_DEPARTMENT_POST_AND_PUT['required_fields'])
        if missing_fields_list:
            validation_message.append(missing_fields_list)
    elif request_type == 'PUT' and model == 'employee':
        missing_fields_list = missing_fields(
            payload,
            constants.VALIDATION_EMPLOYEE_POST_AND_PUT['required_fields'])
        if missing_fields_list:
            validation_message.append(missing_fields_list)
        non_numeric_fields = numeric_fields(
            payload,
            constants.VALIDATION_EMPLOYEE_POST_AND_PUT['integer_fields'])
        if non_numeric_fields:
            validation_message.append(non_numeric_fields)
        if not validate_date(payload.get('date_of_joining')):
            validation_message.append({
                'invalid date format':
                    'Date of joining should be in valid YYYY-MM-DD format'})
        if payload.get('gender') not in constants.GENDER:
            validation_message.append({
                'invalid gender value': 'Gender should be male or female'})
        if not is_float(str(payload.get('salary'))):
            validation_message.append({
                'invalid salary value': 'Salary should be like 2000.00'})
    return validation_message


def missing_fields(payload, key_list):
    """Check missing fields.
    :param payload: json
    :param key_list: list
    :return: mixed
    """
    missing_fields_list = []
    for key in key_list:
        if key not in payload:
            missing_fields_list.append(key)
    if missing_fields_list:
        return {'missing fields': [key for key in missing_fields_list]}
    return missing_fields_list


def numeric_fields(payload, key_list):
    """Check fields are numeric.
    :param payload: json
    :param key_list: list
    :return: mixed
    """
    non_numeric_fields = []
    for key in key_list:
        if not is_number(str(payload.get(key))):
            non_numeric_fields.append(key)
    if non_numeric_fields:
        return {'non integer or negative fields list':
                [key for key in non_numeric_fields]}
    return non_numeric_fields


def validate_date(date):
    """Validate date in Y-m-d format.
    :param date: Date to validate.
    :return: boolean
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def is_authenticated(headers):
    """Authenticate request with api key.
    :param headers: dict - Request headers.
    :return: boolean
    """
    if constants.API_KEY_IN_HEADER in headers:
        if headers.get(constants.API_KEY_IN_HEADER) == constants.API_KEY:
            return True
    return False


def authorization(request):
    """Wrapper function to validate request.
    :param request: obj - Request object.
    :return: Wrapper function response.
    """
    def authenticate(func):
        @wraps(func)
        def authenticate_and_call(*args, **kwargs):
            if not is_authenticated(request.headers):
                return flaskify(response.create_error_response(
                    code=constants.ERROR_CODE_UNAUTHORIZED_REQUEST,
                    message=constants.ERROR_MESSAGE_UNAUTHORIZED_ACCESS,
                    status=oto_status.UNAUTHORIZED))
            return func(*args, **kwargs)
        return authenticate_and_call
    return authenticate


def validate_filter_request(filter_data, model):
    """Validate GET request for filter records.
    :param filter_data: dict - Request to filter data.
    :param model: str
    :return: list
    """
    validation_message = []
    invalid_fields_message = []
    non_numeric_fields = numeric_fields(
        filter_data, constants.INTEGER_FIELDS_FILTER_REQUEST)
    if non_numeric_fields:
        validation_message.append(non_numeric_fields)
    if filter_data.get('order_by') \
            and filter_data.get('order_by') not in constants.SORT_ORDER:
        validation_message.append({
            'invalid order by value':
                'order_by value should be ASC or DESC'})
    missing_fields_list = missing_fields_for_filters(filter_data)
    if missing_fields_list:
        validation_message.append({'missing fields': missing_fields_list})
    if model == 'department':
        if filter_data.get('sort_by'):
            invalid_fields_list = invalid_fields(
                filter_data.get('sort_by'), 'sort_by',
                constants.VALIDATION_DEPARTMENT_FIELDS_FOR_FILTER)
            if invalid_fields_list:
                invalid_fields_message.append(invalid_fields_list)
        if filter_data.get('search_by'):
            invalid_fields_list = invalid_fields(
                filter_data.get('search_by'), 'search_by',
                constants.VALIDATION_DEPARTMENT_FIELDS_FOR_FILTER)
            if invalid_fields_list:
                invalid_fields_message.append(invalid_fields_list)
    if model == 'employee':
        if filter_data.get('sort_by'):
            invalid_fields_list = invalid_fields(
                filter_data.get('sort_by'), 'sort_by',
                constants.VALIDATION_EMPLOYEE_FIELDS_FOR_FILTER)
            if invalid_fields_list:
                invalid_fields_message.append(invalid_fields_list)
        if filter_data.get('search_by'):
            invalid_fields_list = invalid_fields(
                filter_data.get('search_by'), 'search_by',
                constants.VALIDATION_EMPLOYEE_FIELDS_FOR_FILTER)
            if invalid_fields_list:
                invalid_fields_message.append(invalid_fields_list)
    if invalid_fields_message:
        validation_message.append({'invalid fields': invalid_fields_message})
    return validation_message


def invalid_fields(fields, operation, valid_fields):
    """Validate invalid fields.
    :param fields: str
    :param operation: str
    :param valid_fields: list
    :return: list
    """
    invalid_fields_list = []
    for field in fields.split(','):
        if field not in valid_fields:
            invalid_fields_list.append(field)
    if invalid_fields_list:
        return '{invalid_fields}. {operation} contains {valid_fields}'.format(
            invalid_fields=','.join(invalid_fields_list), operation=operation,
            valid_fields=','.join(valid_fields))
    return invalid_fields_list


def missing_fields_for_filters(filter_data):
    """Validate missing fields.
    :param filter_data: dict
    :return: list
    """
    missing_field_search = []
    missing_field_sort = []
    for k, v in filter_data.items():
        if k in constants.FIELDS_FOR_SEARCH:
            if filter_data[k] is None:
                missing_field_search.append(k)
    if len(missing_field_search) == 2:
        missing_field_search.clear()
    for k, v in filter_data.items():
        if k in constants.FIELDS_FOR_SORT:
            if filter_data[k] is None:
                missing_field_sort.append(k)
    if len(missing_field_sort) == 2:
        missing_field_sort.clear()
    return missing_field_search + missing_field_sort
