from pony.orm import Database, db_session
from pony.orm import Required, Set, Optional

from lessons.lesson_22.alchemy_base import DATABASE_URL2

#db = Database(provider='postgres', user='postgres', password='123', host='localhost', database='postgres')
db = Database(provider='sqlite', filename='database.sqlite', create_db=True)



class Department(db.Entity):
    name = Required(str)
    employees = Set('Employee')  # Багато спідробітників можуть


class Employee(db.Entity):
    name = Required(str)
    department = Required('Department')  # Працювати в одному відділі
    age = Optional(int, sql_default='30')


db.generate_mapping(create_tables=True)

with db_session:
    department = Department(name='Security2')
    db.commit()

    #Додавання нового співробітника
    john = Employee(name='John', department=department)
    db.commit()

    # Оновлення інформації про співробітника
    john.name = 'John Doe'
    db.commit()

    # Видалення співробітника
    # db.delete(john)
    # db.commit()

############

    employees = Employee.select(lambda e: e.age > 20 and e.department.name == 'Security')

    # SQL аналог: SELECT * FROM employee WHERE age > 30 AND department_id IN (SELECT id FROM department WHERE name = 'IT');

    # Сортування співробітників за зростанням віку
    sorted_employees = employees.order_by(Employee.age.asc)

    # print(list(sorted_employees)[0].name)
    # SQL аналог: SELECT * FROM (SELECT * FROM employee WHERE age > 30 AND department_id IN (SELECT id FROM department WHERE name = 'IT')) ORDER BY age;

    # Вибірка перших 5 співробітників
    first_five_employees = sorted_employees[:5]
    print(first_five_employees)