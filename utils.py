import sqlite3 as sql
from sqlite3.dbapi2 import DatabaseError
from prettytable import from_db_cursor
import click 

def sqllite_connect():
    """connects/creates passwords database"""
    try:
        con = sql.connect('passwords.db')
        return con

    except sql.Error as error:
        click.echo("Error accessing database: " + error)

def sql_insert(con, values):
    """insert a row into the accounts table"""
    cursor = con.cursor()
    try:
        cursor.execute("""
        INSERT INTO accounts (account, username, password, email, tag)
        VALUES (?,?,?,?,?)
        """,values)
        con.commit()
    except sql.Error as error:
        click.echo("Error inserting account: " + error)

def sql_query_accounts(con, val):
    """returns cursor of accounts that match specific account"""
    cursor = con.cursor()
    try:
        cursor.execute("""
        SELECT * FROM accounts
        WHERE account=?
        """, (val))
        return cursor # returns cursor query
    except sql.Error as error:
        click.echo("Error querying accounts: " + error)

def sql_query_tags(con, val):
    """returns cursor of accounts that match specific tag"""
    cursor = con.cursor()
    try:
        cursor.execute("""
        SELECT * FROM accounts
        WHERE tag=?
        """, (val))
        return cursor # returns cursor query
    except sql.Error as error:
        click.echo("Error querying accounts: " + error)

def sql_fetch_all(con):
    """return cursor with all rows from the accounts table"""
    cursor = con.cursor()
    cursor.execute("SELECT * FROM accounts") # selects all rows
    return cursor # returns cursor query

def sql_delete_account(con, id):
    """deletes an account from the accounts table"""
    cursor = con.cursor()
    try:
        cursor.execute("DELETE FROM accounts WHERE id=?",id) # delete row
    except sql.Error as error:
        click.echo("Error deleting account, make sure id is correct: " + error)

def print_table(cursor):
    """prints table of accounts"""
    table = from_db_cursor(cursor)
    print(table.get_string())