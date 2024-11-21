from flask import Flask, jsonify, request
import psycopg2
from dotenv import find_dotenv, load_dotenv
import sys, os
from flask_migratepg import MigratePg
from models import sentiment_model, emotion_sentiment_model


app = Flask(__name__)


# load .env variables
if not load_dotenv(find_dotenv()):
    print("Error loading variables from dotenv")
else:
    print(".env file loaded successfully!") 

#migrating to database
app.config.from_mapping(
    MIGRATIONS_PATH=os.path.abspath('database/migrations'),
    PSYCOPG_CONNINFO=os.getenv("DATABASE_URL")
)

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



# initialize sentiment model
sentiment_pipeline = sentiment_model()

#initialize emotion-sentiment model
emotion_sentiment_pipeline = emotion_sentiment_model()

# Use the model to analyze text
result = sentiment_pipeline("Yeah this product sucks and I want a new one. Please refund my money")
emotion= emotion_sentiment_pipeline("This sucks ass")
print(result[0]["label"])
print(emotion)


# get the emotional sentiment of a comment
@app.route("/sentiment", methods=["POST"])
def get_sentiment():
    try:
        data = request.json
        if not data or "comment" not in data:
            return jsonify({"message": "Invalid input, 'comment' field is required"}), 400

        comment = data["comment"]
        comment_feeling = emotion_sentiment_pipeline(comment)
        return jsonify({"message":comment_feeling[0]["label"] }), 200
    except ValueError as err:
        return jsonify({"message": err}),400
    except Exception as e:
         return jsonify({"message": f"An unexpected error occurred: {str(e)}"}), 500

  


@app.route("/health", methods=["GET"])
def health():
    conn, cur = databaseConnection()
  
    return{"messsage": "API endpoint is healthy"}

if __name__ == '__main__': 
    app.run(debug=True)