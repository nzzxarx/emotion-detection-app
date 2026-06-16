"""
Flask web server for the Emotion Detection application.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Route that receives text, passes it to the emotion_detector,
    and returns a formatted string with the emotion scores.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    response = emotion_detector(text_to_analyze)

    # Task 7: Handling blank input error message
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Task 6: Required output format string
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the default index template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)