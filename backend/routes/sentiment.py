from flask import request, Blueprint, jsonify
from models import sentiment_model, emotion_sentiment_model
from database import databaseConnection
import psycopg2

sentiment_bp = Blueprint("sentiment", __name__)


# initialize sentiment model
sentiment_pipeline = sentiment_model()

#initialize emotion-sentiment model
emotion_sentiment_pipeline = emotion_sentiment_model()

# Use the model to analyze text
result = sentiment_pipeline("Yeah this product sucks and I want a new one. Please refund my money")
emotion= emotion_sentiment_pipeline("This sucks ass")
print(result[0]["label"])
print(emotion)


# get the emotional sentiment of a specific comment by id
@sentiment_bp.route("/sentiment/<id>", methods=["GET"])
def get_sentiment(id):
    try:
         comment_id = int(id) 
    except ValueError as err:
            print(f"ID is not an integer: {err}")
            return jsonify({"error": "ID needs to be an integer"}), 400
    except KeyError as err:
            print(f"ID was not added to request: {err}")
            return jsonify({"error": "ID is missing"}), 400
    
    conn_pool, conn, cur = databaseConnection()
    
    try:
        cur.execute("SELECT feedback FROM user_comments WHERE id = %s", (id,))
        feedback = cur.fetchall()
        print(feedback)
        if cur.rowcount ==0:
            print("No record found with this id")
            return jsonify({"message": "No record found with this id"}), 400
        else:
            sentiment = emotion_sentiment_pipeline(feedback)
            conn.commit()
            return jsonify({"Comment Sentiment":sentiment[0]["label"] }), 200
    except psycopg2 as err:
        print("Database error", err)
        return jsonify({"Error Message":f"Database error with this request"}),400
    except Exception as e:
         return jsonify({"message": f"An unexpected error occurred: {str(e)}"}), 500

  
# get rating of comment (out of 5 stars)
@sentiment_bp.route("/rating/<id>", methods=["GET"])
def get_rating(id):
    try:
         comment_id = int(id) 
    except ValueError as err:
            print(f"ID is not an integer: {err}")
            return jsonify({"error": "ID needs to be an integer"}), 400
    except KeyError as err:
            print(f"ID was not added to request: {err}")
            return jsonify({"error": "ID is missing"}), 400
    
    conn_pool, conn, cur = databaseConnection()
    
    try:
        cur.execute("SELECT feedback FROM user_comments WHERE id = %s", (id,))
        feedback = cur.fetchall()
        print(feedback)
        if cur.rowcount ==0:
            print("No record found with this id")
            return jsonify({"message": "No record found with this id"}), 400
        else:
            rating = sentiment_pipeline(feedback)
            conn.commit()
            return jsonify({"Comment Rating":rating[0]["label"] }), 200
    except psycopg2 as err:
        print("Database error", err)
        return jsonify({"Error Message":f"Database error with this request"}),400
    except Exception as e:
         return jsonify({"message": f"An unexpected error occurred: {str(e)}"}), 500
