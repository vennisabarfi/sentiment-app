from database import databaseConnection
from flask import Blueprint

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health():
    conn, cur = databaseConnection()
  
    return{"messsage": "API endpoint is healthy"}