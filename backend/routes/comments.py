from flask import Flask, request, jsonify, Blueprint
from database import databaseConnection
import psycopg2
 

comments_bp = Blueprint("comments_bp", __name__)

@comments_bp.route("/add", methods=["POST"])
def add_comment():
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
        conn.rollback()
        print("Error inserting data:", err)
        return {"message": err}
    finally:
        cur.close()
        conn_pool.putconn(conn)



# view all comments
@comments_bp.route("/view", methods=["GET"])
def view_comment():
    conn_pool, conn, cur = databaseConnection()
    try:
        cur.execute("SELECT * FROM user_comments")
        comments = cur.fetchall()
        conn.commit()
        return {"Comments found": comments}
    except Exception as err:
        conn.rollback()
        print("Error retrieving data from database", err)
        return jsonify({"message":f"Error retrieving data from database, {err}"})
    finally:
        cur.close()
        conn_pool.putconn(conn)

       
# view comments by id
@comments_bp.route("/view/<id>", methods=["GET"])
def view_all_comments(id):
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
        if len(comments)==0:
            print("No record found with this id")
            return {"message": "No record found with this id"}
        else:
            conn.commit()
            return {"Comments found": comments}
    except psycopg2.Error as e:
        print("Error with SQL Request", e)
        return jsonify({"message": f"Comment with this ID not found: {e}"})
    except Exception as err:
        conn.rollback()
        print("Error retrieving data from database", err)
        return jsonify({"message":f"Error retrieving data from database, {err}"})
    finally:
        cur.close()
        conn_pool.putconn(conn)

