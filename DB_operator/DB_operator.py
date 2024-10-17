import os
import pyodbc
from dotenv import load_dotenv
import SQL_Queries


class ConnectDB: # подключение к бд
    @staticmethod
    def connect_to_db(server, database, user, password):
        ConnectionString = f'''DRIVER={{ODBC Driver 17 for SQL Server}};
                                         SERVER={server};
                                         DATABASE={database};
                                         UID={user};
                                         PWD={password}'''
        try:
            conn = pyodbc.connect(ConnectionString)
            conn.autocommit = True
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            return conn


class MSSQLOperator:

    def __init__(self, connector_obj):
        self.conn = connector_obj

    def create_database(self, database_name, size=None, maxsize=None, filegrowth=None):    # метод создания бд
        SQL_COMMAND= SQL_Queries