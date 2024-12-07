from flask import Flask, request, jsonify, Blueprint
from database import databaseConnection, close_db
import psycopg2
 

comments_bp = Blueprint("comments_bp", __name__)

@comments_bp.route("/add", methods=["POST"])
def add_comment():
    headers = {'Access-Control-Allow-Origin': '*',
               'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
               'Access-Control-Allow-Headers': 'Content-Type'}
    if request.method.lower() == 'options':
        return jsonify(headers), 200
    
    conn_pool, conn, cur = databaseConnection()
    try:
        data = request.json
        if not data:
            return jsonify({"message": "No data sent in user_comments"}), 400
        
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        feedback = request.json['feedback']
        email = request.json['email']
        product_type = request.json['product_type']
        
        # SQL query to insert data
        insert_query = """
            INSERT INTO user_comments (first_name, last_name, feedback, email, product_type)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
        """
        cur.execute(insert_query, (first_name, last_name, feedback, email,product_type))
        conn.commit()
        comment_id = cur.fetchone()[0]
        return jsonify({"message": "Comment added successfully", "id": comment_id}), 201
    except Exception as err:
        if conn:
            conn.rollback()
        print("Error inserting data:", err)
        return {"message": err}
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)



# view all comments
@comments_bp.route("/view", methods=["GET"])
def view_comment():
    headers = {'Access-Control-Allow-Origin': '*',
               'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
               'Access-Control-Allow-Headers': 'Content-Type'}
    if request.method.lower() == 'options':
        return jsonify(headers), 200
    
    conn_pool, conn, cur = databaseConnection()
    try:
        cur.execute("SELECT * FROM user_comments")
        comments = cur.fetchall()
        conn.commit()
        return {"Comments found": comments}
    except Exception as e:
        print("An error occured: ", e)
        return jsonify({"message": "Error completing request"}), 500
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)
        
# view number of comments
@comments_bp.route("/total", methods=["GET"])
def view_total_comments():
    headers = {'Access-Control-Allow-Origin': '*',
               'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
               'Access-Control-Allow-Headers': 'Content-Type'}
    if request.method.lower() == 'options':
        return jsonify(headers), 200
    
    conn_pool, conn, cur = databaseConnection()
    try:
        cur.execute("SELECT * FROM user_comments")
        comments = cur.fetchall()
        total_comments = len(comments)
        print(total_comments)
        conn.commit()
        return {"Total Feedback": total_comments}
    except psycopg2 as err:
        print("Database error", err)
        return jsonify({"Error Message":f"Database error with this request"}),400
    except Exception as e:
        print("An error occured: ", e)
        return jsonify({"message": "Error completing request"}), 500
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)




# view comments by id
@comments_bp.route("/view/<id>", methods=["GET"])
def view_comments_by_id(id):
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
        cur.execute("SELECT * FROM user_comments WHERE id = %s", (id,))
        comments = cur.fetchall()
        if cur.rowcount==0:
            print("No record found with this id")
            return {"message": "No record found with this id"}
        else:
            conn.commit()
            return {"Comments found": comments}
    except psycopg2 as err:
        print("Database error", err)
        return jsonify({"Error Message":f"Database error with this request"}),400
    except Exception as e:
        print("An error occured: ", e)
        return jsonify({"message": "Error completing request"}), 500
    finally:
        close_db(conn_pool=conn_pool, conn=conn, cur=cur)


#remove comment feature. implement after clerk integration
comments_bp.route("/remove", methods=["DELETE"])
def remove_comment(id):
    pass