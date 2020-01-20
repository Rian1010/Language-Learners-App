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

@app.route('/lesson_one')
def lesson_one():
    return render_template('lesson-one.html')

@app.route('/lesson_two')
def lesson_two():
    return render_template('lesson-two.html')

@app.route('/lesson_three')
def lesson_three():
    return render_template('lesson-three.html')

@app.route('/lesson_four')
def lesson_four():
    return render_template('lesson-four.html')

@app.route('/lesson_five')
def lesson_five():
    return render_template('lesson-five.html')

@app.route('/lesson_six')
def lesson_six():
    return render_template('lesson-six.html')

@app.route('/advanced_lesson')
def advanced_lesson():
    return render_template('advanced-lesson.html')


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
