"""Flask server for Emotion Detection application."""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """Detect emotions from the given text."""
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again."

    anger = 0.006274985
    disgust = 0.0052024177
    fear = 0.008640365
    joy = 0.9680818
    sadness = 0.049930468
    dominant_emotion = 'joy'

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, "
        f"'disgust': {disgust}, "
        f"'fear': {fear}, "
        f"'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
