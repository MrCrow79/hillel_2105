from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from lessons.lesson_22.alchemy_base import Base



class DepartmentTable(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("EmployeeTable", back_populates="department")
