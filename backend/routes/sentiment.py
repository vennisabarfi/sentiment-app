from flask import request, Blueprint, jsonify
from models import sentiment_model, emotion_sentiment_model
from database import databaseConnection, close_db
import psycopg2



sentiment_bp = Blueprint("sentiment", __name__)


# initialize sentiment model (rating)
rating_pipeline = sentiment_model()

#initialize emotion-sentiment model
emotion_sentiment_pipeline = emotion_sentiment_model()


# view all sentiments


# view average sentiments


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
        print("An error occured: ", e)
        return jsonify({"message": "Error completing request"}), 500
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)

  
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
            rating = rating_pipeline(feedback)
            conn.commit()
            return jsonify({"Comment Rating":rating[0]["label"] }), 200
    except psycopg2 as err:
        print("Database error", err)
        return jsonify({"Error Message":f"Database error with this request"}),400
    except Exception as e:
        print("An error occured: ", e)
        return jsonify({"message": "Error completing request"}), 500
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)

# view all ratings with their id  (work on this). Integrate with user_comments table may need to work on this on comments.py
@sentiment_bp.route("rating/all", methods=["GET"])
def view_ratings_by_id():
    headers = {'Access-Control-Allow-Origin': '*',
               'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
               'Access-Control-Allow-Headers': 'Content-Type'}
    if request.method.lower() == 'options':
        return jsonify(headers), 200
    
    conn_pool, conn, cur = databaseConnection()
    # select all the ratings and
    try:
        cur.execute("SELECT * FROM sentiments")
        comments = cur.fetchall()
        # conn.commit()
        return {"Comments found": comments}
    except Exception as e:
        print("An error occured: ", e)
        return jsonify({"message": "Error completing request"}), 500
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)

# view average of all ratings
@sentiment_bp.route("rating/average", methods=["GET"])
def view_all_ratings():
    headers = {'Access-Control-Allow-Origin': '*',
               'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
               'Access-Control-Allow-Headers': 'Content-Type'}
    if request.method.lower() == 'options':
        return jsonify(headers), 200
    
    conn_pool, conn, cur = databaseConnection()
    # select all the ratings and
    try:
        cur.execute("SELECT AVG(sentiment_rating) FROM sentiments")
        average_value = cur.fetchall()
   
        conn.commit()
        
        try: 
               
           sentiments_average= float((average_value[0][0]))  
        except ValueError as err:
            print("Error converting SQL tuple result to a float", err)
            
        return {"Average Rating": sentiments_average}
    except Exception as e:
        print("An error occured: ", e)
        return jsonify({"message": "Error completing request"}), 500
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)
        
# work on this
#view average ratings per product
@sentiment_bp.route("rating/average/<product>", methods=["GET"])
def view_ratings_per_product(product):
    headers = {'Access-Control-Allow-Origin': '*',
               'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
               'Access-Control-Allow-Headers': 'Content-Type'}
    if request.method.lower() == 'options':
        return jsonify(headers), 200
    
    try:
        
        validated_product = str(product.lower)
    except ValueError as err:
        print("Product Value should be string", err)
    # work on if item not in range 
    
    conn_pool, conn, cur = databaseConnection()
    # select all the ratings and
    try:
        cur.execute("SELECT AVG(sentiment_rating) FROM sentiments")
        average_value = cur.fetchall()
   
        conn.commit()
        
        try: 
               
           sentiments_average = float((average_value[0][0]))
            
        except ValueError as err:
            print("Error converting SQL tuple result to integer", err)
            
        return {"Average Rating": sentiments_average}
    except Exception as e:
        print("An error occured: ", e)
        return jsonify({"message": "Error completing request"}), 500
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)

# view positive comments only (sentiment label), sepcifically total
@sentiment_bp.route("positive/all", methods=["GET"])
def view_total_positive():
    headers = {'Access-Control-Allow-Origin': '*',
               'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
               'Access-Control-Allow-Headers': 'Content-Type'}
    if request.method.lower() == 'options':
        return jsonify(headers), 200
    

    
    conn_pool, conn, cur = databaseConnection()
    # work on if array is empty
    try:
        cur.execute("SELECT sentiment_label FROM sentiments WHERE sentiment_label='positive'")
        positive_values = len(cur.fetchall())
   
        # conn.commit()
        return {"Positive Sentiments": positive_values}
    except Exception as e:
        print("An error occured: ", e)
        return jsonify({"message": "Error completing request"}), 500
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)


# view negative comments only (sentiment label), sepcifically total
@sentiment_bp.route("negative/all", methods=["GET"])
def view_total_negative():
    headers = {'Access-Control-Allow-Origin': '*',
               'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
               'Access-Control-Allow-Headers': 'Content-Type'}
    if request.method.lower() == 'options':
        return jsonify(headers), 200

    
    conn_pool, conn, cur = databaseConnection()
    # work on if array is empty
    try:
        cur.execute("SELECT sentiment_label FROM sentiments WHERE sentiment_label='negative'")
        negative_values = len(cur.fetchall())
   
        # conn.commit()
        return {"Negative Sentiments": negative_values}
    except Exception as e:
        print("An error occured: ", e)
        return jsonify({"message": "Error completing request"}), 500
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)


# run feedback through sentiment and rating models
# work on cron job implementation

def process_feedback():
    conn_pool, conn, cur = databaseConnection()
    try:
        # Retrieve unprocessed feedback from user_comments. Avoid double selecting
        cur.execute("""
            SELECT id, feedback
            FROM user_comments
            WHERE id NOT IN (SELECT user_comment_id FROM sentiments)
        """)
        feedback_list = cur.fetchall()
        # print(feedback_list)

        if not feedback_list:
            print("No new feedback to process.")
            return

        # Run each feedback through sentiment pipelines (to get rating result and emotion result).. add tests
        for feedback_id, feedback_text in feedback_list:
            rating_result = rating_pipeline(feedback_text)
            emotion_result = emotion_sentiment_pipeline(feedback_text)

            try:
                
            #Extract results (maybe work on the names lol)
                sentiment_label = emotion_result[0]["label"]  # e.g., 'positive'
                sentiment_rating_text = rating_result[0]["label"]   # e.g., '4.2'
            
            # convert sentiment rating to numerical instead text
            # split from '5 stars' to 5 as an integer
                sentiment_rating = int(sentiment_rating_text.split()[0])
                
            except Exception as e:
                print("Error extracting rating: ", e)
            except IndexError as index_e:
                print("Error as array is out of range: ", index_e)
            except  ValueError as value_e:
                print("Error converting to integer", value_e)
            

            # Insert the sentiment analysis result into the sentiments table
            cur.execute("""
                INSERT INTO sentiments (
                    user_comment_id, sentiment_rating, sentiment_label
                )
                VALUES (%s, %s, %s)
            """, (
                feedback_id, 
                sentiment_rating, 
                sentiment_label, 
            ))

     
        conn.commit()
        print(f"Processed {len(feedback_list)} feedback entries.")
   
    except Exception as e:
        conn.rollback()
        print(f"Error processing feedback: {e}")

    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)
        


@sentiment_bp.route("/process", methods=["POST"])
def process_feedback_route():
    
    try:
        process_feedback()
        return jsonify({"message": "Feedback processing completed."}), 200
    except Exception as e:
        return jsonify({'Process failed': e}), 500
        
   

