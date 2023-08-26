import mysql.connector
import environ

env = environ.Env()
environ.Env().read_env()


class Mysql_Connection:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password=env('M1x_2021'),
        database=env('cliente')
    )
    cursor = connection.cursor()
