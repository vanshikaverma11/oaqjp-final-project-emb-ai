import requests

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the given text using Watson NLP Library.
    :param text_to_analyze: str, text to analyze for emotions
    :return: dict, emotion analysis results
    """
    # Check for blank text input
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Define the URL and headers
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Define the input JSON
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Make the POST request
    response = requests.post(url, headers=headers, json=input_json)

    # Check for HTTP error status
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Get the response data
    response_data = response.json()

    # Extract the emotion predictions
    emotions = response_data.get("emotionPredictions", [])
    if not emotions:
        return {"error": "No emotion predictions found."}

    # Extract the emotion values from the first prediction
    emotion_values = emotions[0]["emotion"]
    
    # Calculate the dominant emotion
    dominant_emotion = max(emotion_values, key=emotion_values.get)

    # Format and return the results
    return {
        "anger": emotion_values["anger"],
        "disgust": emotion_values["disgust"],
        "fear": emotion_values["fear"],
        "joy": emotion_values["joy"],
        "sadness": emotion_values["sadness"],
        "dominant_emotion": dominant_emotion
    }
