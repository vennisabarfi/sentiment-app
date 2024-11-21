import os
import sys
import psycopg2



# establish database connection
def databaseConnection():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        cur = conn.cursor()
        print("Database connection successful!")
    except psycopg2.OperationalError as err:
        print("Error establishing database connection", err)
        sys.Exit(1) #exit program if the connection fails
    return conn, cur