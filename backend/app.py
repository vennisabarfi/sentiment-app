from flask import Flask, jsonify, request
import psycopg2
from dotenv import find_dotenv, load_dotenv
import sys, os
from flask_migratepg import MigratePg

app = Flask(__name__)


# load .env variables
if not load_dotenv(find_dotenv()):
    print("Error loading variables from dotenv")
else:
    print(".env file loaded successfully!") 

app.config.from_mapping(
    MIGRATIONS_PATH=os.path.abspath('database/migrations'),
    PSYCOPG_CONNINFO=os.getenv("DATABASE_URL")
)

print(os.getenv("DATABASE_URL"))
MigratePg(app)


# establish database connection
def databaseConnection():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        cur = conn.cursor()
        print("Database connection successful!")
    except psycopg2.OperationalError as err:
        print("Error establishing database connection", err)
        sys.Exit(1)
    return conn, cur


@app.route("/health", methods=["GET"])
def health():
    conn, cur = databaseConnection()
  
    return{"messsage": "API endpoint is healthy"}

if __name__ == '__main__': 
    app.run(debug=True)