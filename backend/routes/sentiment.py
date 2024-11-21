from flask import request, Blueprint, jsonify
from models import sentiment_model, emotion_sentiment_model

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


# get the emotional sentiment of a comment
@sentiment_bp.route("/sentiment", methods=["POST"])
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

  