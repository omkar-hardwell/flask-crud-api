"""Employee model."""
from oto import response
from sqlalchemy import Column, Integer, Float, String, Date, Enum, \
    ForeignKey, exc
from sqlalchemy.orm import backref, relationship
from sqlalchemy.orm.exc import NoResultFound
from mysql_connector import Base, Session
from src import constants
from src.logic.models import department


# Instantiate session
session = Session()


class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    department_id = Column(Integer, ForeignKey(
        'department.department_id', ondelete='CASCADE'), nullable=False)
    date_of_joining = Column(Date, nullable=False)
    gender = Column(Enum(*constants.GENDER), nullable=False, default='male')
    address = Column(String(1000), nullable=True)
    salary = Column(Float(10, 2), nullable=False)
    parent = relationship(
        'Department', backref=backref('employee', cascade='all,delete'))

    def __repr__(self):
        return "<Employee(employee_id=%s, name='%s', department_id=%s, " \
            "date_of_joining='%s', gender='%s', address='%s', " \
            "salary=%s)>" % (self.employee_id, self.name, self.department_id,
                             self.date_of_joining, self.gender, self.address,
                             self.salary)


def get_employee(employee_id):
    """Get the employee details against the given employee id.
    :param employee_id: int - Unique identification of employee.
    :return: Employee details against the given employee id.
    :raises: sqlalchemy exceptions.
    """
    try:
        result_set = session.query(
            Employee, department.Department.name
        ).join(
            department.Department,
            Employee.department_id == department.Department.department_id
        ).filter(
            Employee.employee_id == employee_id
        ).one()
        result = {
            'employee': {
                'address': result_set[0].address,
                'date_of_joining': str(result_set[0].date_of_joining),
                'department': result_set[1],
                'employee_id': result_set[0].employee_id,
                'gender': result_set[0].gender,
                'name': result_set[0].name,
                'salary': float(str("%0.2f" % result_set[0].salary))
            }
        }
        return response.Response(result)
    except NoResultFound:
        return response.create_not_found_response(
            constants.ERROR_MESSAGE_NOT_FOUND.format(
                title='employee id', id=employee_id))
    except (exc.SQLAlchemyError, exc.DBAPIError):
        return response.create_fatal_response(
            constants.ERROR_MESSAGE_INTERNAL_ERROR)


def delete_employee(employee_id):
    """Delete the employee details against the given employee id.
    :param employee_id: int - Unique identification of employee.
    :return: Success message on delete employee details.
    :raises: sqlalchemy exceptions.
    """
    try:
        result_set = session.query(Employee). \
            filter(Employee.employee_id == employee_id).one()
        session.delete(result_set)
        session.commit()
        return response.Response(message=constants.DELETE_MESSAGE.format(
            module='Employee', title='employee id', id=employee_id))
    except NoResultFound:
        return response.create_not_found_response(
            constants.ERROR_MESSAGE_NOT_FOUND.format(
                title='employee id', id=employee_id))
    except (exc.SQLAlchemyError, exc.DBAPIError):
        return response.create_fatal_response(
            constants.ERROR_MESSAGE_INTERNAL_ERROR)


def post_employee(payload):
    """Add an employee details.
    :param payload: json - Employee details.
    :return: Employee details added against the given data.
    :raises: sqlalchemy exceptions.
    """
    try:
        employee = Employee(
            address=payload.get('address'),
            date_of_joining=payload.get('date_of_joining'),
            department_id=payload.get('department_id'),
            gender=payload.get('gender'),
            name=payload.get('name'),
            salary=payload.get('salary')
        )
        session.add(employee)
        session.commit()
        # Get employee details via get_employee() using last inserted id.
        return get_employee(employee.employee_id)
    except(exc.SQLAlchemyError, exc.DBAPIError):
        return response.create_fatal_response(
            constants.ERROR_MESSAGE_INTERNAL_ERROR)


def put_employee(employee_id, payload):
    """Update the employee details against the given employee id.
    :param employee_id: int - Unique identification of employee.
    :param payload: json - Employee details.
    :return: Success message on update of employee details.
    :raises: sqlalchemy exceptions.
    """
    try:
        employee = {
            'address': payload.get('address'),
            'date_of_joining': payload.get('date_of_joining'),
            'department_id': payload.get('department_id'),
            'gender': payload.get('gender'),
            'name': payload.get('name'),
            'salary': payload.get('salary')
        }
        affected_row = session.query(Employee).filter(
            Employee.employee_id == employee_id).update(employee)
        if not affected_row:
            raise NoResultFound
        session.commit()
        return response.Response(message=constants.UPDATE_MESSAGE.format(
            module='Employee', title='employee id', id=employee_id))
    except NoResultFound:
        return response.create_not_found_response(
            constants.ERROR_MESSAGE_NOT_FOUND.format(
                title='employee id', id=employee_id))
    except(exc.SQLAlchemyError, exc.DBAPIError):
        return response.create_fatal_response(
            constants.ERROR_MESSAGE_INTERNAL_ERROR)
