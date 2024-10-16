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

'''запрос на создание БД'''
'''Create DB Params'''
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

'''новое подключение к бд'''
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



'''запрос на создание таблицы'''

SQL_QUERY = '''
CREATE TABLE Product
(
product_id  int PRIMARY KEY,
product_name nvarchar(50),
price int
)'''

'''новое подключение к бд'''
conn = pyodbc.connect(connectionString)
conn.autocommit = True
cursor = conn.cursor()
try:
    cursor.execute('USE Products') #запрос на смену БД
    cursor.execute(SQL_QUERY)
except pyodbc.ProgrammingError as ex:
    print(ex)
else:
    print("Table Created")
finally:
    conn.close()

'''запрос на заполнение таблицы'''

SQL_QUERY = '''
INSERT INTO product (product_id, product_name, price)
VALUES 
(1,'Desctop Computer', 800),
(2,'Leptop',1200),
(3,'Tablet', 200),
(4, 'Monitor', 350),
(5, 'Printer', 150)
'''

'''новое подключение к бд'''
conn = pyodbc.connect(connectionString)
conn.autocommit = True
cursor = conn.cursor()
try:
    cursor.execute('USE Products')  # запрос на смену БД
    cursor.execute(SQL_QUERY)
except pyodbc.Error as ex:
    print(ex)
else:
    print("Table Filled In")
finally:
    conn.close()


SQL_QUERY = r'''
SELECT product_name,price
FROM Product
'''


conn = pyodbc.connect(connectionString)
cursor = conn.cursor()
cursor.execute('USE Products')  # запрос на смену БД
cursor.execute(SQL_QUERY)
records = cursor.fetchall()
for record in records:
    print(f'{record.product_name} // {record.price}')

# SQL_QUERY = '''
# CREATE TABLE dbo.TestTable
# (id int PRIMARY KEY,
#  TestColumn1 nvarchar(50),
#  TestColumn2 nvarchar(100));'''


# conn = pyodbc.connect(connectionString)
# cursor = conn.cursor()
# cursor.execute(SQL_QUERY)
# cursor.commit()
