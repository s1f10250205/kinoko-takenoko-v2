from flask import Flask, render_template, request
app = Flask(__name__)
import re
from flask import Markup


kinoko_count = 3
takenoko_count = 5
messages = ['Kinoko is wonderful!', 'Takenoko is awesome!']

@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    kinoko_percent = kinoko_count / (kinoko_count + takenoko_count) * 100
    takenoko_percent = takenoko_count / (kinoko_count + takenoko_count) * 100
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)

def linkify(text):
    url_pattern = r'(https?://[^\s]+)'
    return Markup(re.sub(url_pattern, r'<a href="\\1" target="_blank">\\1</a>', text))

@app.route('/vote', methods=['POST'])
def answer():
    kinoko_percent = kinoko_count / (kinoko_count + takenoko_count) * 100
    takenoko_percent = takenoko_count / (kinoko_count + takenoko_count) * 100

    messages_with_links = [linkify(m) for m in messages]
    return render_template('vote.html', messages=messages_with_links,
                           kinoko_count=kinoko_count,
                           takenoko_count=takenoko_count,
                           kinoko_percent=kinoko_percent,
                           takenoko_percent=takenoko_percent)

