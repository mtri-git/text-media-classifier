
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
from underthesea import text_normalize, classify, sentiment

app = Flask(__name__)

@app.route('/')
def default():
    return {
            'message': 'text classifier',
        }

# route for text classier with underthesea with post method input text
@app.route('/text-classifier', methods=['POST'])
def text_classifier():
    data = request.get_json()
    if 'text' in data:
        text = data['text']
        text = text_normalize(text)
        res = classify(text)
        text_sentiment = sentiment(text)
        return jsonify({
            "category": res[0],
            "sentiment": text_sentiment
        }), 200
    else:
        error_message = {'error': 'Invalid request data'}
        return jsonify(error_message), 400