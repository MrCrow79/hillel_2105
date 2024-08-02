create_table_query = """CREATE TABLE public.math_students (
	id bigint NOT NULL,
	name varchar NOT NULL,
	CONSTRAINT math_students_pk PRIMARY KEY (id)
);"""


# if primary keys is (Id, Name)
# 1 Denys
# 1 Alex
# 2 Alex
# 2 Denys

# if primary keys is Id
# 1 Denys
# 2 Denys
# 3 Alex

select_all_query = 'select * from public.math_students'

select_all_with_condition = "select * from public.math_students asd where asd.\"name\" = 'Alex'"

create_table_cource = """CREATE TABLE public.cource (
	id bigint NOT NULL,
	name varchar NOT NULL,
	CONSTRAINT math_students_pk PRIMARY KEY (id)
);"""

create_table_students = """CREATE TABLE public.students (
	id int NOT NULL,
	"name" varchar NOT NULL,
	description varchar NULL,
	cource_id int NOT NULL,
	CONSTRAINT students_pk PRIMARY KEY (id),
	CONSTRAINT students_corces_fk FOREIGN KEY (cource_id) REFERENCES public.corces(id)
	ON DELETE CASCADE
);
"""

imsert_into_cource = """INSERT INTO public.corces
(id, "name")
VALUES(1, 'math'), (2, 'biology'), (3, 'liteture');
"""

inster_into_students = """INSERT INTO public.students
(id, "name", description, cource_id)
values
(1, 'Denys', null, 1),
(2, 'Alex', null, 1),
(3, 'Ivan', 'ivans description', 2),
(4, 'Alex II', 'Some descriptions', 3);"""

# create_st_addr = """CREATE TABLE public.students_addr (
# 	id int NOT NULL,
# 	"addr" varchar NOT NULL
# );"""
#
# insert_st_addr = """INSERT INTO public.students_addr (id, "addr")
# VALUES (1, 'Kharviv'),
# (2, 'Kyiv'),
# (4, 'Lviv')
# ;"""

update_student = """UPDATE students SET name = 'New name' WHERE id = 1;"""

inner_join = "select * from students s join corces c on s.cource_id = c.id"  # join == inner join
full_join = "select * from students join corces on students.cource_id = corces.id"  # join == inner join

inner_with_st_addr = 'select * from students_addr sa join students s on sa.id = s.id'
right_with_st_addr = 'select * from students_addr sa right join students s on sa.id = s.id'