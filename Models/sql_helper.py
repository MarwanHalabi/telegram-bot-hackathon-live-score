import pymysql

from config import connection


def insert_to_DB(query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except pymysql.DatabaseError as err:
        print("Insert record Error", err)
        return False


def delete_from_DB(query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except:
        print("Error,Could not delete from database")


def get_data_from_DB(query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except:
        print("Failed to get data")
