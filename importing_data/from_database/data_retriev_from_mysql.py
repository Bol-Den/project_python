
import mysql.connector as connector

def connection(my_host, my_user, my_password, my_database):
     """connecting to mysql"""
     db_connection = connector.connect(host = my_host,
                                     user = my_user,
                                     password = my_password,
                                     database = my_database)
     return db_connection


def data_retrieval(connection, sql):
     """retrieving data from connected database"""
     my_cursor = connection.cursor()
     my_cursor.execute(sql)
     result = my_cursor.fetchall()
     return result
