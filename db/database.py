import sqlite3
from company_details.bankAccount import BankAccount
from company_details.customer import Customer
from company_details.division import Division
from company_details.documents import Documents
from company_details.invoice import Invoice
from company_details.supplier import Supplier


def open_connection():
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()


def data_base(query, parameters):
    try:
        connection, cursor = open_connection()
        cursor.execute(query, parameters)
        connection.commit()
        data = cursor.fetchall()
        print(data)
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        connection.close()
