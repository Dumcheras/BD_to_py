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

SQL_QUERY = '''
CREATE TABLE dbo.TestTable
(id int PRIMARY KEY, 
 TestColumn1 nvarchar(50),
 TestColumn2 nvarchar(100));'''


conn = pyodbc.connect(connectionString)
cursor = conn.cursor()
cursor.execute(SQL_QUERY)
cursor.commit()
