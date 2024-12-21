from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    """
    This function handles the POST request to analyze emotions from the input text.
    It calls the emotion_detector function to perform the analysis and returns the result.
    
    Returns:
        JSON: The emotion analysis results or an error message if no dominant emotion is found.
    """
    # Get the input text from the JSON payload
    input_data = request.get_json()
    text_to_analyze = input_data.get('text', '')

    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None
    if result.get('dominant_emotion') is None:
        # If dominant_emotion is None, return an error message
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Return the emotion analysis result if everything is okay
    return jsonify(result)

if __name__ == '__main__':
    """
    Start the Flask application on port 4002.
    """
    app.run(debug=True, port=4002)
