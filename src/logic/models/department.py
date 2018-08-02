"""Department model."""
import math

from oto import response
from sqlalchemy import Column, Integer, String, exc, asc, desc
from sqlalchemy.orm.exc import NoResultFound
from mysql_connector import Base, Session
from src import constants


# Instantiate session
session = Session()


class Department(Base):
    """Department class and it's CRUD operation."""
    __tablename__ = 'department'

    department_id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return "<Department(department_id=%s, name='%s')>" % (
            self.department_id, self.name)


def get_department(department_id):
    """Get the department details against the given department id.
    :param department_id: int - Unique identification of department.
    :return: Department details against the given department id.
    :raises: sqlalchemy exceptions.
    """
    try:
        result_set = session.query(Department). \
            filter(Department.department_id == department_id).one()
        result = {
            'department': {
                'department_id': result_set.department_id,
                'name': result_set.name
            }
        }
        return response.Response(result)
    except NoResultFound:
        return response.create_not_found_response(
            constants.ERROR_MESSAGE_NOT_FOUND.format(
                title='department id', id=department_id))
    except (exc.SQLAlchemyError, exc.DBAPIError):
        return response.create_fatal_response(
            constants.ERROR_MESSAGE_INTERNAL_ERROR)


def delete_department(department_id):
    """Delete the department details against the given department id.
    :param department_id: int - Unique identification of department.
    :return: Success message on delete department details.
    :raises: sqlalchemy exceptions.
    """
    try:
        result_set = session.query(Department). \
            filter(Department.department_id == department_id).one()
        session.delete(result_set)
        session.commit()
        return response.Response(message=constants.DELETE_MESSAGE.format(
            module='Department', title='department id', id=department_id))
    except NoResultFound:
        return response.create_not_found_response(
            constants.ERROR_MESSAGE_NOT_FOUND.format(
                title='department id', id=department_id))
    except (exc.SQLAlchemyError, exc.DBAPIError):
        return response.create_fatal_response(
            constants.ERROR_MESSAGE_INTERNAL_ERROR)


def post_department(payload):
    """Add the department details.
    :param payload: json - Department details.
    :return: Department details added against the given data.
    :raises: sqlalchemy exceptions.
    """
    try:
        department = Department(
            name=payload.get('name')
        )
        session.add(department)
        session.commit()
        # Get department details via get_department() using last inserted id.
        return get_department(department.department_id)
    except(exc.SQLAlchemyError, exc.DBAPIError):
        return response.create_fatal_response(
            constants.ERROR_MESSAGE_INTERNAL_ERROR)


def put_department(department_id, payload):
    """Update the department details against the given department id.
    :param department_id: int - Unique identification of department.
    :param payload: json - Department details.
    :return: Success message on update of department details.
    :raises: sqlalchemy exceptions.
    """
    try:
        department = {'name': payload.get('name')}
        affected_row = session.query(Department).filter(
            Department.department_id == department_id).update(department)
        if not affected_row:
            raise NoResultFound
        session.commit()
        return response.Response(message=constants.UPDATE_MESSAGE.format(
            module='Department', title='department id', id=department_id))
    except NoResultFound:
        return response.create_not_found_response(
            constants.ERROR_MESSAGE_NOT_FOUND.format(
                title='department id', id=department_id))
    except(exc.SQLAlchemyError, exc.DBAPIError):
        return response.create_fatal_response(
            constants.ERROR_MESSAGE_INTERNAL_ERROR)


def get_departments(filter_data):
    """Get the departments detail against the given filter request.
    :param filter_data: dict - Data for filter the result.
    :return: Department details against given filter data. Features supported
    (sort / search / paginate).
    :raises: sqlalchemy exceptions.
    """
    try:
        result = []
        result_set = session.query(
            Department
        ).prefix_with(
            'SQL_CALC_FOUND_ROWS'
        ).filter(
            *__fields_for_search(filter_data)
        ).order_by(
            *__fields_for_sort(filter_data)
        ).offset(
            (int(filter_data.get('page')) - 1) *
            int(filter_data.get('page_size'))
        ).limit(
            filter_data.get('page_size')
        ).all()
        # Calculate total number of records after filter data.
        total_rows = session.execute('SELECT FOUND_ROWS()').scalar()
        for department in result_set:
            result.append({
                'department_id': department.department_id,
                'name': department.name
            })
        departments = {
            'departments': result,
            'page': int(filter_data.get('page')),
            'page_size':
                int(filter_data.get('page_size')),
            'total_pages': math.ceil(
                total_rows / int(filter_data.get('page_size'))) or None,
            'total_records': total_rows or None,
            'total_records_per_page': len(result) or None
        }
        return response.Response(departments)
    except(exc.SQLAlchemyError, exc.DBAPIError):
        return response.create_fatal_response(
            constants.ERROR_MESSAGE_INTERNAL_ERROR)


def __fields_for_sort(filter_data):
    """Returns list of fields with order to sort result by given request.
    :param filter_data: dict - Data for filter the result.
    :return: list
    """
    fields_to_sort = [None]
    if filter_data.get('sort_by') and filter_data.get('order_by'):
        fields_to_sort = \
            [desc(getattr(Department, k)) if v == 'DESC'
             else asc(getattr(Department, k))
             for k, v in dict(zip(
                 filter_data.get('sort_by').split(','),
                 filter_data.get('order_by').split(','))).items()
             ]
    return fields_to_sort


def __fields_for_search(filter_data):
    """Returns list of fields with their value to search result by given request.
    :param filter_data: dict - Data for filter the result.
    :return: mixed
    """
    # where 1 clause added if no fields found to search.
    fields_to_search = '1'
    if filter_data.get('search_by') and filter_data.get('search_for'):
        fields_to_search = \
            [getattr(Department, k) == v
             for k, v in dict(zip(
                filter_data.get('search_by').split(','),
                filter_data.get('search_for').split(','))).items()
             ]
    return fields_to_search
