import sqlite3
from Learn_DB.TestData import Test_Data


class Data_Base:

    def __init__(self, filename):
        self.filename = filename


    def get_connection(self):
        con = sqlite3.connect(self.filename)
        print('DataBase Opened')
        return con

    def create_table(self, con, table_name):
        con.execute('''CREATE TABLE IF NOT EXISTS ''' + table_name + '''(F_NAME, EMAIL, PWD)''')
        print('Table created')

    def insert_records(self, con, table_name, obj):
        data = '''INSERT INTO ''' + table_name + '''(F_NAME, EMAIL, PWD) VALUES(?, ?, ?) '''
        con.execute(data, (obj.f_name, obj.email, obj.pwd))
        con.commit()
        print('inserted the given records')

    def close_connection(self, con):
        con.close()
        print('closed the connections')