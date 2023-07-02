
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# route for text classier with underthesea with post method input text
@app.route('/text_classifier', methods=['POST'])
def text_classifier():
    from underthesea import classify
    text = request.form['text']
    res = classify(text)
    return {
        "category": res[0],
    }

