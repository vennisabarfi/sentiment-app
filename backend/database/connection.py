import os
import sys
import psycopg2
from psycopg2.pool import SimpleConnectionPool



# establish database connection
def databaseConnection():
    try:
        conn_pool = SimpleConnectionPool(minconn=1, #minimum number of connections
                                    maxconn=10, #maximum number of connections
                                    dsn = os.getenv("DATABASE_URL"))
        # get connection from pool
        conn = conn_pool.getconn()
        #initialize cursor
        cur = conn.cursor()
        print("Database connection successful!")
    except psycopg2.OperationalError as err:
        print("Error establishing database connection", err)
        sys.exit(1) #exit program if the connection fails
    return conn_pool, conn, cur