import sqlite3
import logging
from datetime import datetime
from multipledispatch import dispatch

NOTES_TABLE = "notes"
CALENDAR_TABLE = "calendar_events"
DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"


def connect_db(database):
    try:
        return sqlite3.connect(database)
    except sqlite3.Error as err:
        logging.exception(err)
        raise err


def get_all_rows(connection, table):
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table} WHERE status_id = 1")
        rows = cursor.fetchall()
        cursor.close()
        return rows

    except sqlite3.Error as err:
        logging.exception(err)
        raise err
    finally:
        connection.close()


def get_row(connection, table, row_id):
    try:
        statement = f"SELECT * FROM {table} WHERE rowid = ?"

        cursor = connection.cursor()
        cursor.execute(statement, (row_id,))
        row = cursor.fetchall()
        cursor.close()

        return row[0]
    except sqlite3.Error as err:
        logging.exception(err)
        raise err
    finally:
        connection.close()


@dispatch(object, str, str, str)
def insert_row(connection, table, title, description):
    current_date_time = datetime.now()
    date_time = current_date_time.strftime(DATETIME_FORMAT)

    try:
        row = (date_time, date_time, 1, title, description)
        statement = f"""INSERT INTO {table}
                        (created_date, modified_date, status_id, title, description)
                        VALUES
                        (?, ?, ?, ?, ?)"""

        cursor = connection.cursor()
        cursor.execute(statement, row)
        connection.commit()
        cursor.close()

    except sqlite3.Error as err:
        logging.exception(err)
        raise err
    finally:
        connection.close()


@dispatch(object, str, str, str, str)
def insert_row(connection, table, event, start_date, end_date):
    try:
        row = (event, start_date, end_date)
        statement = f"""INSERT INTO {table}
                        (event, start_date, end_date)
                        VALUES
                        (?, ?, ?)"""

        cursor = connection.cursor()
        cursor.execute(statement, row)
        connection.commit()
        cursor.close()

    except sqlite3.Error as err:
        logging.exception(err)
        raise err
    finally:
        connection.close()


@dispatch(object, str, int, str, str)
def update_row(connection, table, row_id, title, description):
    current_date_time = datetime.now()
    date_time = current_date_time.strftime(DATETIME_FORMAT)

    try:
        row = (title, description, date_time, row_id)
        statement = f"UPDATE {NOTES_TABLE} set title = ?, description = ?, modified_date = ? WHERE rowid = ?"

        cursor = connection.cursor()
        cursor.execute(statement, row)
        connection.commit()
        cursor.close()

    except sqlite3.Error as err:
        logging.exception(err)
        raise err
    finally:
        connection.close()


@dispatch(object, str, int, str, str, str)
def update_row(connection, table, row_id, start_date, end_date, event):
     try:
        row = (start_date, end_date, event, row_id)
        statement = f"UPDATE {table} set start_date = ?, end_date = ?, event = ? WHERE rowid = ?"

        cursor = connection.cursor()
        cursor.execute(statement, row)
        connection.commit()
        cursor.close()
     except sqlite3.Error as err:
        logging.exception(err)
        raise err
     finally:
        connection.close()


def delete_row(connection, table, row_id):
    try:
        statement = f"UPDATE {table} set status_id = '2' WHERE rowid = ?"

        cursor = connection.cursor()
        cursor.execute(statement, (row_id,))
        connection.commit()
        cursor.close()

    except sqlite3.Error as err:
        logging.exception(err)
        raise err
    finally:
        connection.close()


# NOTES OPERATIONS
def get_all_notes(conn):
    return get_all_rows(conn, NOTES_TABLE)


def get_note(conn, id):
    return get_row(conn, NOTES_TABLE, id)


def create_note(conn, title, description):
    return insert_row(conn, NOTES_TABLE, title, description)


def edit_note(conn, id, title, description):
    return update_row(conn, NOTES_TABLE, id, title, description)


def remove_note(conn, id):
    return delete_row(conn, NOTES_TABLE, id)


# CALENDAR OPERATIONS
def get_all_events(conn):
    return get_all_rows(conn, CALENDAR_TABLE)


def get_event(conn, id):
    return get_row(conn, CALENDAR_TABLE, id)


def create_event(conn, event, start_date, end_date):
    return insert_row(conn, CALENDAR_TABLE, event, start_date, end_date)


def edit_event(conn, id, start_date, end_date, event):
    return update_row(conn, CALENDAR_TABLE, id, start_date, end_date, event)


def remove_event(conn, id):
    return delete_row(conn, CALENDAR_TABLE, id)

