from flask import Flask, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def sent_statement():
    text_to_analyze = request.args.get("text")
    if not text_to_analyze:
        return "Error: No text provided", 400

    result = emotion_detector(text_to_analyze)

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']}, and "
        f"'sadness': {result['sadness']}. The dominant emotion is "
        f"{result['dominant_emotion']}."
    )
    return response

if __name__ == "__main__":
    app.run(port=5000)