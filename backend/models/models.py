from transformers import pipeline


# leaves a star review for products
def sentiment_model():
    sentiment_pipeline = pipeline("text-classification", model="LiYuan/amazon-review-sentiment-analysis")
    return sentiment_pipeline

# detects overall mood of user comments
def emotion_sentiment_model():
    emotion_pipeline = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student")
    return emotion_pipeline
   