"""Department model"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from mysql_connector import Base, Session


# Instantiate session
session = Session()


class Department(Base):
    __tablename__ = 'department'

    department_id = Column(
        Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    employee = relationship('Employee')

    def __repr__(self):
        return 'Department(%r, %r)' % (
            self.department_id, self.name)
