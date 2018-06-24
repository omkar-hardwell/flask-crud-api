"""Validation for API methods."""


def is_number(value):
    """Check value is digit.
    :param value: int
    :return: boolean
    """
    if value.isdigit():
        return True
    return False
