from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from lessons.lesson_22.alchemy_base import Base


class EmployeeTable(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("DepartmentTable", back_populates="employees")


    def __str__(self):
        return f'{self.id}, {self.name}, {self.department.name}'
