def create_database_default(name):
    COMMAND = fr"CREATE DATABASE {name}"
    return COMMAND


def create_database(name, size, maxsize, filegrowth):
    COMMAND = fr'''
CREATE DATABASE {name}
ON
(
NAME = {name}Database_data,
FILENAME = 'D:\local_serv\MSSQL16.SQLEXPRESS\MSSQL\DATA\{name}Database_data.mdf',
SIZE = {size}MB,
MAXSIZE = {maxsize}GB,
FILEGROWTH = {filegrowth}
)
LOG ON
(
NAME = {name}Database_log,
FILENAME = 'D:\local_serv\MSSQL16.SQLEXPRESS\MSSQL\DATA\{name}Database_data.ldf',
SIZE = {size}MB,
MAXSIZE = {str(round(int(maxsize) * 0.1))}GB,
FILEGROWTH = {filegrowth}
)'''
    return COMMAND


def create_employers(table_name):  # запрос для создания таблицы
    QUERY = fr'''CREATE TABLE {table_name}
            (employer_id int PRIMARY KEY,
            employer_name nvarchar(100),
            employer_url nvarchar(200));'''
    return QUERY


def create_vacansies(table_name):  # запрос для создания таблицы
    QUERY = fr'''CREATE TABLE {table_name}
            (vacansies_id int PRIMARY KEY,
            vacansies_name nvarchar(100),
            vacansies_url nvarchar(200),
            vacansies_salary_form int,
            vacansies_salary_to int,
            employer_id int
            REFERENCES employers(employer_id));'''
    return QUERY
