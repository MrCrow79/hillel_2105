from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc

from lessons.lesson_22.alchemy_base import engine, Base
from lessons.lesson_22.tables.employee_table import EmployeeTable
from lessons.lesson_22.tables.user_table import UserTable
from lessons.lesson_22.tables.department_table import DepartmentTable

Base.metadata.create_all(engine)  # create table Employee, Department

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

it_department = DepartmentTable(name='IT')
hr_department = DepartmentTable(name='HR')

john = EmployeeTable(name='John', department=it_department)
alice = EmployeeTable(name='Alice', department=hr_department)
bob = EmployeeTable(name='Bob', department=it_department)

# session.add_all([it_department, hr_department, john, alice, bob])
# session.commit()
#
# Вибірка співробітників та їх департаментів
employees = session.query(EmployeeTable).all()
for employee in employees:
    print(f"Ім'я: {employee.name}, Департамент: {employee.department.name}")

# [print(k) for k in it_department.employees]

# it_department = DepartmentTable(name='Finance')
# session.add(it_department)
# session.commit()

res = session.query(DepartmentTable).join(EmployeeTable, full=True).all()  # full join
res = session.query(DepartmentTable).join(EmployeeTable, isouter=True).all()  # left join
[print(k.name, k.employees) for k in res]


# # Закриття сесії
session.close()