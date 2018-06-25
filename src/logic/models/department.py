"""Department model."""
from oto import response
from sqlalchemy import Column, Integer, String, exc
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
