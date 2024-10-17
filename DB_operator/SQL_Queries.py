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


