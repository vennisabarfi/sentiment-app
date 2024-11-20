from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return{"messsage": "API endpoint is healthy"}

if __name__ == '__main__':
    app.run(debug=True)