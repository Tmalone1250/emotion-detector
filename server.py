# server.py

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector  # Import the modified emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    # Retrieve text from request JSON
    data = request.json
    text_to_analyze = data.get("text", "").strip()
    
    # Validate input and process
    result = emotion_detector(text_to_analyze)
    
    # Check if dominant emotion is None (invalid input or blank)
    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400
    
    # Format the response as required if valid
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    
    # Return the formatted response as JSON
    return jsonify({"message": formatted_response})

# Run the application on localhost:5000
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
