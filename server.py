from flask import Flask, request, render_template
from emotion_detection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    text_to_analyse = request.args.get('textToAnalyze')
    emotion_result = emotion_detector(text_to_analyse)
    if not isinstance(emotion_result, dict):
        return f"Błąd analizy: {emotion_result}"

    try:
        anger = emotion_result['anger']
        disgust = emotion_result['disgust']
        fear = emotion_result['fear']
        joy = emotion_result['joy']
        sadness = emotion_result['sadness']
        # Wyznacz dominantę
        dominant_emotion = max(emotion_result, key=emotion_result.get)
    except Exception:
        return "Invalid text! Please try again"

    response_str = f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.
    The dominant emotion is <strong>{dominant_emotion}</strong>."""
    return response_str

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)