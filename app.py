import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
messages = []


def add_messages(username, message):
    """Add messages to the messages list and add a timestamp"""
    messages.append("({}) {}: {}".format(now, username, message))
    now = datetime.now().strftime("%H:%M:%S")


def get_all_messages():
    """Get all of the messages and separate them with a 'br'"""
    return "<br>".join(messages)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/basics_lesson')
def basics_lesson():
    return render_template('basics-lesson.html')


@app.route('/', methods=['GET', 'POST'])
def Search():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        _text = request.form['text']
        return render_template('index.html', _anchor="hp-section6", result=_text)


@app.route('/<username>')
def user(username):
    """Display chat messages"""
    return "Hi, {0} - {1}".format(username, get_all_messages())


@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message"""
    add_messages(username, message)
    return redirect("/" + username)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
