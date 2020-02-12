from config import connection


def insert_to_DB(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
