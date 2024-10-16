import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()
SERVER = os.getenv('MS_SQL_SERVER')
DATABASE = os.getenv('MS_SQL_DATABASE')
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')

# """SimpleConnection"""
# connectionString = f'''DRIVER={{SQL SERVER}};
#                                  SERVER={SERVER};
#                                  DATABASE={DATABASE};
#                                  Trusted_Connection=yes'''


"""SimpleConnection"""
connectionString = f'''DRIVER={{ODBC Driver 17 for SQL Server}};
                                 SERVER={SERVER};
                                 DATABASE={DATABASE};
                                 UID={USER};
                                 PWD={PASSWORD}'''

'''Create DB Params'''  # Запрос на создание БД
SQL_COMMAND = r'''
CREATE DATABASE Products
ON
(
NAME = ProductsDatabase_data,
FILENAME = 'D:\local_serv\MSSQL16.SQLEXPRESS\MSSQL\DATA\ProductsDatabase_data.mdf',
SIZE = 10MB,
MAXSIZE = 2GB,
FILEGROWTH = 5%
)
LOG ON
(
NAME = ProductsDatabase_log,
FILENAME = 'D:\local_serv\MSSQL16.SQLEXPRESS\MSSQL\DATA\ProductsDatabase_data.ldf',
SIZE = 5MB,
MAXSIZE = 200MB,
FILEGROWTH = 5%
)'''

conn = pyodbc.connect(connectionString)
conn.autocommit = True
cursor = conn.cursor()
try:
    cursor.execute(SQL_COMMAND)
except pyodbc.Error as ex:
    print(ex)
else:
    print("Database Created")
finally:
    conn.close()






# SQL_QUERY = '''
# SELECT fio
# FROM Students
# '''


# conn = pyodbc.connect(connectionString)
# cursor = conn.cursor()
# cursor.execute(SQL_QUERY)
# records = cursor.fetchall()
# for record in records:
#     print(f'{record.fio}')

# SQL_QUERY = '''
# CREATE TABLE dbo.TestTable
# (id int PRIMARY KEY,
#  TestColumn1 nvarchar(50),
#  TestColumn2 nvarchar(100));'''


# conn = pyodbc.connect(connectionString)
# cursor = conn.cursor()
# cursor.execute(SQL_QUERY)
# cursor.commit()
