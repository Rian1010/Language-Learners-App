import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myFirstCluster'
app.config["MONGO_URI"] = 'mongodb+srv://Rian:j4JWQ1Ntzc9u0U7m@myfirstcluster-ges2b.mongodb.net/learner-app-data?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/task_manager')
def task_manager():
    return render_template('task-manager.html', tasks=mongo.db.tasks.find())

@app.route('/add_tasks')
def add_tasks():
    return render_template('add-tasks.html', lessons=mongo.db.lessons.find(), task=mongo.db.task.find())

@app.route('/insert_task', methods=['POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('task_manager'))

@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit-task.html', task=the_task, lessons=mongo.db.lessons.find(), categories=all_categories)

@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    return redirect(url_for('task_manager'))

@app.route('/community')
def community():
     posts = mongo.db.posts.find()
     return render_template('community.html', posts=posts, lesson=mongo.db.lessons.find())

@app.route('/add_posts')
def add_posts():
    return render_template('add-posts.html', posts=mongo.db.posts.find(), lessons=mongo.db.lessons.find())

@app.route('/insert_post', methods=['POST'])
def insert_post():
    posts = mongo.db.posts
    posts.insert_one(request.form.to_dict())
    return redirect(url_for('community'))

@app.route('/edit_post/<post_id>')
def edit_post(post_id):
    the_post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template('edit-post.html', posts=the_post, lessons=mongo.db.lessons.find())

@app.route('/delete_post/<post_id>')
def delete_post(post_id):
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    return redirect(url_for('community'))

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

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
