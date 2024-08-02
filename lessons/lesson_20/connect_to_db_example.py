import sqlite3


class SqliteDBConnector:

    def __init__(self, file_path='my_sqlite3.db'):
        self.file_path = file_path
        self.connection = None
        self.cursor = None

    def __enter__(self):
        print('__enter__ method')
        self.connection = sqlite3.connect(self.file_path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ method')
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


# with SqliteDBConnector() as db_cursor:
#     db_cursor.execute('Select * from students')
#     print(db_cursor.fetchall())
#     db_cursor.execute("""INSERT INTO students ('id', 'name', 'description', 'cource_id') values (10, 'Den', null, 1)""")

# print('-'*80)
# with SqliteDBConnector() as db_cursor:
#     db_cursor.execute('Select * from students')
#     print(db_cursor.fetchall())


class SqliteExecutor():
    def __init__(self):
        self.db = SqliteDBConnector

    def select_all_sturdent(self):
        with self.db() as cursor:
            cursor.execute('select * from students')
            raise AssertionError
            return cursor.fetchall()


print(SqliteExecutor().select_all_sturdent())
