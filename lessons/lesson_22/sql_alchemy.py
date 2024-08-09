from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc

from lessons.lesson_22.alchemy_base import engine, Base
from lessons.lesson_22.tables.user_table import UserTable

Base.metadata.create_all(engine)  # create table User

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()

# Додавання нового користувача
new_user = UserTable(name='John', age=30)  # create bew instance as a new row in table
session.add(new_user)  # insert new row in table
session.commit()
# Відповідає INSERT INTO users (name, age) VALUES ('John', 30);
#
# # Оновлення інформації про користувача
user_asc = session.query(UserTable).filter_by(name='John').order_by(UserTable.id).first()  # order by asc
user_desc = session.query(UserTable).filter_by(name='John').order_by(desc(UserTable.id)).first()  # order by desc

user_select_all = session.query(UserTable).all()  # select all users, returns list of instances
user_select_first = session.query(UserTable).first()  # select first users, returns instance

user_select_where = session.query(UserTable).filter_by(name='John').all()  # filter_by == where, filter_by(name='John') = WHERE name='John'

user_select_order_by_asc = session.query(UserTable).order_by(UserTable.id).all()  # order_by = order by in sql
user_select_order_by_desc = session.query(UserTable).order_by(desc(UserTable.id)).all()  # order_by = order by in sql


print(user_select_first.name, user_select_first.id, user_select_first.age)
user_select_first.age = 77  # зміна існуючої строки в бд(udpate )
session.commit()  # save changes in the DB, # Відповідає UPDATE users SET age=31 WHERE name='John';

# for user_ in (session.query(UserTable).filter_by(name='John').all()):
#     user_.name += ' surname'


# user_asc.age = 32
# user_desc.age = 33
# session.commit()

#
# with engine.connect() as con:
#     con.execute("delete from USER where id = 1")

# Видалення користувача

# for u in session.query(UserTable).filter_by(name='John').all():
#     session.delete(u)

session.commit()
# Відповідає DELETE FROM users WHERE name='John';
#
#
# Вибірка всіх користувачів
all_users = session.query(UserTable).all()
# SQL аналог: SELECT * FROM users;
#
# # Фільтрація за умовою
john = session.query(UserTable).filter_by(name='John').first()
# # SQL аналог: SELECT * FROM users WHERE name = 'John' LIMIT 1;
#
# # Сортування
sorted_users = session.query(UserTable).order_by(UserTable.age.desc()).all()
# # SQL аналог: SELECT * FROM users ORDER BY age DESC;