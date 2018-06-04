"""Employee model."""
from sqlalchemy import Column, Integer, Float, String, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from mysql_connector import Base, Session
from src import constants


# Instantiate session
session = Session()


class Employee(Base):
    __tablename__ = 'employee'

    employee_id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    department_id = Column(
        Integer, ForeignKey('department.department_id'), nullable=False)
    date_of_joining = Column(Date, nullable=False)
    gender = Column(Enum(*constants.GENDER), nullable=False, default='male')
    address = Column(String(1000), nullable=True)
    salary = Column(Float(10, 2), nullable=False)
    department = relationship('department', backref='employee')

    def __repr__(self):
        return 'Employee(%r, %r, %r, %r, %r, %r, %r)' % (
            self.employee_id, self.name, self.department_id,
            self.date_of_joining, self.gender, self.address, self.salary)
