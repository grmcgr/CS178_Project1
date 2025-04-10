# check the slides for information to add to this - from labs 


# idea - list of contacts with most recent change with user who changed it 
# work contacts with username / email / phone number / first name / preferred name / 
# option to open text boxes to change the names 
# then do a sql table of who has updated and when 
# return me a list of all the people who username = mcgrane1 updated 
# return me a list of who has been updated in the last week
# user not in system - set up your username

import pymysql
import pymysql.cursors
import cred
import boto3

# Section 1: My SQL (RDS) Connection Helpers

def get_conn():
    """
    Establish and return a connection to the MySQL RDS database using 
    credentials from cred.py
    Use DictCursor to return query results as dictionaries.
    """
    return pymysql.connect(
        host=cred.host,
        user=cred.user,
        password=cred.password,
        db=cred.db,
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_query(query, args=()):
    """
    Execute a SQL query using a connection to RDS. 
    Closes the connection automatically after running the query.
    Returns the results as a list of dictionaries.
    """
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(query, args)
            rows = cur.fetchall()
        return rows
    finally:
        conn.close()


