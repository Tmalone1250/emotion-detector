# emotion_detection.py

import json
import requests

def emotion_detector(text_to_analyze):
    """
    Detects emotions in a given text using the Watson NLP Emotion Detection API.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        dict: A dictionary containing scores for anger, disgust, fear, joy, sadness,
              and the dominant emotion, or None values if the input is empty.
    """
    # Check if text is blank
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send the POST request with a timeout and error handling
    response = requests.post(url, headers=headers, data=json.dumps(input_json), timeout=10)
    
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Process the response for valid requests
    response_dict = response.json()
    emotions = response_dict.get('emotion_predictions', [{}])[0].get('emotion_scores', {})

    # Extract specific emotions
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }



if __name__ == "__main__":
    TEXT = "I am so happy I am doing this."
    RESULT = emotion_detector(TEXT)
    print(RESULT)


