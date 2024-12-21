import requests
import json

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP Library.
    :param text_to_analyze: str, text to analyze for emotions
    :return: dict, emotion analysis results
    """
    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Define the input JSON
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Make the POST request
    response = requests.post(url, headers=headers, json=input_json)

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Return the result
    return response.json()

        # Extract emotion scores
    emotions = response_data.get("emotion_predictions", {})
    anger = emotions.get("anger", 0.0)
    disgust = emotions.get("disgust", 0.0)
    fear = emotions.get("fear", 0.0)
    joy = emotions.get("joy", 0.0)
    sadness = emotions.get("sadness", 0.0)


    # Find the dominant emotion
    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Format and return the results
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }