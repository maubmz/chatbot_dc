import mysql.connector
import environ

def conexion_mysql():
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='M1x_2021',
        database='cliente'
    )
    return connection
