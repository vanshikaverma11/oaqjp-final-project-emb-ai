import requests

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
