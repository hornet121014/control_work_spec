import mysql.connector
from mysql.connector import Error

host_name = "localhost"
user_name = "root"
user_password = "**********"
db_name = "human_friends"

def create_connection_db(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def connection():
    connection_db = create_connection_db(host_name, user_name, user_password, db_name)
    return connection_db


def logout():
    pass
