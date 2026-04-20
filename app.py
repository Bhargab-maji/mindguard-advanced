from flask import Flask, render_template, request, jsonify
from model import analyze_emotion, get_response

app = Flask(__name__)

@app.route('/')
def home():
    # This now assumes your main interaction is in index.html
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data['text']

    emotion = analyze_emotion(text)
    response = get_response(emotion, text)

    return jsonify({
        "emotion": emotion,
        "response": response
    })

if __name__ == "__main__":
    app.run(debug=True)
