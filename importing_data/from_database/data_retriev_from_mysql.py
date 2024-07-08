
import mysql.connector as connector

def connection(my_database):
     """connecting to mysql"""
     db_connection = connector.connect(host = "localhost",
                                     user = "root",
                                     password = "denis1987",
                                     database = my_database)
     return db_connection


def data_retrieval(conn, query):
     """retrieving data from connected database"""
     my_cursor = conn.cursor()
     my_cursor.execute(query)
     result = my_cursor.fetchall()
     my_cursor.close()
     conn.close()

     return result
