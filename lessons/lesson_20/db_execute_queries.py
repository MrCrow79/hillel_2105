# import psycopg2
#
# # db_name
# # host
# # port
# # user_name
# # user_password
#
# db_name = 'students'
# user_name = 'postgres'
# host = '127.0.0.1'
# port = 5432
# user_password = 123
#
# # connection = psycopg2.connect(database=db_name, user=user_name, password=user_password, host=host, port=port)
# # # connection.autocommit = True
# # cursor = connection.cursor()
# #
# #
# # cursor.execute("""INSERT INTO public.students
# # (id, "name", description, cource_id)
# # values
# # (7, 'Yuri', null, 2);""")
# #
# # cursor.execute("""
# # UPDATE students SET name = 'New name' WHERE id = 1;""")
# #
# # connection.commit()
# # cursor.execute('Select * from public.students')
# # q_result = cursor.fetchall()  # get all results from previous query
# #
# #
# # print(q_result)
# #
# #
# # # important
# # cursor.close()
# # connection.close()
#
# connection = psycopg2.connect(database=db_name, user=user_name, password=user_password, host=host, port=port)
# cursor = connection.cursor()
#
#
#
# # cursor.execute(create_st_addr)
# # cursor.execute(insert_st_addr)
#
#
# connection.commit()
#
# cursor.execute("select * from students_addr sa right join students s on sa.id = s.id")
# print(cursor.fetchall())
#
# # important
# cursor.close()
# connection.close()
