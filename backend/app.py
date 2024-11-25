from flask import Flask
from flask_cors import CORS
import psycopg2
from dotenv import find_dotenv, load_dotenv
import sys, os
from flask_migratepg import MigratePg

from database import databaseConnection
from routes import health_bp,comments_bp, sentiment_bp


app = Flask(__name__)
# enable CORS. Extend to resource specific CORS
# CORS(app, resources={r"/*": {"origins": "http://localhost:5173", "allow_headers": "*"}})
CORS(app)
 


# load .env variables
if not load_dotenv(find_dotenv()):
    print("Error loading variables from dotenv")
else:
    print(".env file loaded successfully!") 

# errors with migration need to work on integrating this
#migrating to database
# app.config.from_mapping(
#     MIGRATIONS_PATH=os.path.abspath('database/migrations'),
#     PSYCOPG_CONNINFO=os.getenv("DATABASE_URL")
# )

# MigratePg(app)
 


app.register_blueprint(health_bp)
app.register_blueprint(sentiment_bp, url_prefix ="/model")
app.register_blueprint(comments_bp, url_prefix="/comments")







if __name__ == '__main__': 
    app.run(debug=True)