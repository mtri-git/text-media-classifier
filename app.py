
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# route for text classier with underthesea with post method input text
@app.route('/text-classifier', methods=['POST'])
def text_classifier():
    from underthesea import text_normalize
    from underthesea import classify
    from underthesea import sentiment
    text = request.form['text']
    text = text_normalize(text)
    res = classify(text)
    text_sentiment = sentiment(text)
    return {
        "category": res[0],
        "sentiment": text_sentiment
    }

