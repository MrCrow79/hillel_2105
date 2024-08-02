import sqlite3


create_table_cource = """CREATE TABLE cource (
	id bigint NOT NULL,
	name varchar NOT NULL,
	CONSTRAINT math_students_pk PRIMARY KEY (id)
);"""

create_table_students = """CREATE TABLE students (
	id int NOT NULL,
	"name" varchar NOT NULL,
	description varchar NULL,
	cource_id int NOT NULL,
	CONSTRAINT students_pk PRIMARY KEY (id),
	CONSTRAINT students_corces_fk FOREIGN KEY (cource_id) REFERENCES corces(id)
	ON DELETE CASCADE
);
"""

imsert_into_cource = """INSERT INTO cource
(id, "name")
VALUES(1, 'math'), (2, 'biology'), (3, 'liteture');
"""

inster_into_students = """INSERT INTO students
(id, "name", description, cource_id)
values
(1, 'Denys', null, 1),
(2, 'Alex', null, 1),
(3, 'Ivan', 'ivans description', 2),
(4, 'Alex II', 'Some descriptions', 3);"""

conn = sqlite3.connect('my_sqlite3.db')
cursor = conn.cursor()

# cursor.execute(create_table_cource)
# cursor.execute(create_table_students)

#
# cursor.execute(imsert_into_cource)
# cursor.execute(inster_into_students)

conn.commit()

cursor.execute('select * from students')
print(cursor.fetchall())