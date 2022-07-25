import psycopg2
from psycopg2 import Error


def db_select(sqlcode):
    try:
        connection = psycopg2.connect(user="postgres", password="Admin123", host="localhost",
                                      port="5432", database="MeetingRoom")
        cursor = connection.cursor()
        cursor.execute(sqlcode)
        dat = cursor.fetchall()
        return dat
    except (Exception, Error) as error:
        return error
    finally:
        if connection:
            cursor.close()
            connection.close()


def db_update(sqlcode):
    try:
        connection = psycopg2.connect(user="postgres", password="Admin123", host="localhost",
                                      port="5432", database="MeetingRoom")
        cursor = connection.cursor()
        cursor.execute(sqlcode)
        connection.commit()
    except (Exception, Error) as error:
        return error
    finally:
        if connection:
            cursor.close()
            connection.close()
