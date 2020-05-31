import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__, template_folder='templates')

# MongoDB cluster and URI information to connect to it
app.config["MONGO_DBNAME"] = 'myFirstCluster'
app.config["MONGO_URI"] = 'mongodb+srv://Rian:j4JWQ1Ntzc9u0U7m@myfirstcluster-ges2b.mongodb.net/learner-app-data?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'

mongo = PyMongo(app)

@app.route('/')
# Renders the home page, if the user is logged in, otherwise it renders the registration page
def index():
    username = session.get('username')
    if username:
        users = mongo.db.users.find()
        return render_template('index.html', users=users)
    return render_template('register.html')


@app.route('/signin', methods=["GET", "POST"])
# User login
def signin():
    username = session.get('username')
    if username:
        users = mongo.db.users.find()
        return render_template('index.html', users=users)
    else:
        if request.method == 'POST':
            email = request.form["email"]
            password = request.form['password']
            userEmail = mongo.db.users.find_one({"email": email})

            if userEmail and mongo.db.users.find_one({"password": password}):
                session['username'] = userEmail["username"]
                print(session['username'])
                return render_template('index.html')
            else:
                return 'Invalid email or password'

        return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
# User registration
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = {'username': username, 'email': email, 'password': password}

        if mongo.db.users.find_one({"username": username, "email": email}):
            return 'User already exists'
        else:
            mongo.db.users.insert_one(user)
            session['username'] = request.form['username']
            return render_template('index.html', user=user, password=password)

    return render_template('register.html')

@app.route('/logout')
# Allows a user to logout 
def logout():
    session.pop('username', None)
    return redirect('/signin')

@app.route('/task_manager')
# Renders the task-manager page with the required information from the database in mongoDB, if a user is logged in
# If a user is not logged in, the login page is rendered instead
def task_manager():
    user = session.get('username')
    if user:
        return render_template('task-manager.html', tasks=mongo.db.tasks.find(), lessons=mongo.db.lessons.find())
    return render_template('login.html')

@app.route('/add_tasks')
# Renders the add-task page
def add_task():
    return render_template('add-tasks.html', tasks=mongo.db.tasks.find(), lessons=mongo.db.lessons.find())

@app.route('/insert_task', methods=['GET', 'POST'])
# Allows users to add their own task
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one({
        "task_owner": session['username'],
        "task_lesson_name": request.form.get('lesson_name'),
        'task_name': request.form.get('task_name'),
        'task_description': request.form.get('task_description'),
        'due_date': request.form.get('due_date'),
    })
    return redirect(url_for('task_manager'))

@app.route('/update_task/<task_id>', methods=['GET', 'POST'])
# Allows users to edit their own task
def update_task(task_id):
    task = mongo.db.tasks
    task.update({'_id': ObjectId(task_id)},
                {
                "task_owner": session['username'],
                "task_lesson_name": request.form.get('lesson_name'),
                'task_name': request.form.get('task_name'),
                'task_description': request.form.get('task_description'),
                'due_date': request.form.get('due_date'),
                })
    
    return redirect(url_for('task_manager'))

@app.route('/edit_task/<task_id>')
# Allows users to edit their own task
def edit_task(task_id):
    the_lesson = mongo.db.lessons.find()
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template('edit-task.html', task=the_task, lessons=the_lesson)

@app.route('/delete_task/<task_id>')
# Allows users to delete their own task
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    return redirect(url_for('task_manager'))

@app.route('/community')
# Returns the community page with its required information from mongoDB
def community():
    posts = []
    for result in mongo.db.posts.find():
        result["initDate"] = result['initDate'].strftime("%A %D %H:%M")
        print(result['initDate'])
        posts.append(result)
    return render_template('community.html', posts=posts, lesson=mongo.db.lessons.find())

@app.route('/add_posts')
# renders the add-posts page along with its required information from mongoDB
def add_posts():
    initDate = datetime.today().strftime("%A %D")
    return render_template('add-posts.html', posts=mongo.db.posts.find(), initDate=initDate, lessons=mongo.db.lessons.find())

@app.route('/insert_post', methods=['GET', 'POST'])
# redirects to the community page
def insert_post():
    posts = mongo.db.posts 
    posts.insert_one({
        "author": session['username'],
        "lesson_name": request.form.get("lesson_name"),
        "post_content": request.form.get("post_content"),
        # the code below saves the date of posted posts and indicates that a post has not been edited 
        "initDate": datetime.today(),
        "edit_today": "Edit: None",
    })
    return redirect(url_for('community'))

@app.route('/update_post/<post_id>', methods=['GET', 'POST'])
# Allows a post to be updated and redirects to the community page
def update_post(post_id):
    posts = mongo.db.posts
    posts.update_one({'_id': ObjectId(post_id)},
                 { "$set": {
        "author": session['username'],
        'lesson_name': request.form.get('lesson_name'),
        'post_content': request.form.get('post_content'),
        "edit_today": "Edited: {}".format(datetime.now()),
    }})
    return redirect(url_for('community'))


@app.route('/edit_post/<post_id>')
# renders the edit-post page with the required information from mongoDB
def edit_post(post_id):
    the_post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template('edit-post.html', posts=the_post, lessons=mongo.db.lessons.find())

@app.route('/delete_post/<post_id>')
# Deletes an added lesson by a user
def delete_post(post_id):
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    return redirect(url_for('community'))

@app.route('/lesson_one')
# Renders the lesson-one page with the lessons information from mongoDB
def lesson_one():
    addLesson = mongo.db.lessons.find()
    return render_template('lesson-one.html', addLesson=addLesson)

@app.route('/add_new_lesson')
# Renders the add-lesson page with the lessons information from mongoDB
def add_new_lesson():
    return render_template('add-lesson.html', addLesson=mongo.db.lessons.find())

@app.route('/update_lesson/<addLesson_id>', methods=['GET', 'POST'])
# Allows users to update their own added lessons
def update_lesson(addLesson_id):
    addLesson = mongo.db.lessons
    addLesson.update({'_id': ObjectId(addLesson_id)},
                      {
        "username": session['username'],
        'lesson_name': request.form.get('heading'),
        'heading': request.form.get('heading'),
        'lesson_content': request.form.get('lesson_content'),
    }
    )
    return redirect(url_for('advanced_lesson', addLesson=addLesson))

@app.route('/insert_lesson', methods=['GET', 'POST'])
# Allows users to add their own lessons to the advanced-lesson page
def insert_lesson():
    addLesson = mongo.db.lessons
    addLesson.insert_one({
        "username": session['username'],
        'lesson_name': request.form.get('heading'),
        "heading": request.form.get('heading'),
        'lesson_content': request.form.get('lesson_content'),
    })
    return redirect(url_for('advanced_lesson'))

@app.route('/edit_lesson/<addLesson_id>')
# Allows users to edit their own added lessons with the lessons information from mongoDB
def edit_lesson(addLesson_id):
    addLesson = mongo.db.lessons.find_one({"_id": ObjectId(addLesson_id)})
    return render_template('edit-lesson.html', addLesson=addLesson)

@app.route('/delete_lesson/<addLesson_id>')
# Allows users to delete their own added lesson
def delete_lesson(addLesson_id):
    mongo.db.lessons.delete_one({"_id": ObjectId(addLesson_id)})
    return redirect(url_for('advanced_lesson'))

@app.route('/lesson_two')
# Renders the lesson-two page
def lesson_two():
    return render_template('lesson-two.html')

@app.route('/lesson_three')
# Renders the lesson-three page
def lesson_three():
    return render_template('lesson-three.html')

@app.route('/lesson_four')
# Renders the lesson-four page
def lesson_four():
    return render_template('lesson-four.html')

@app.route('/lesson_five')
# Renders the lesson-five page
def lesson_five():
    return render_template('lesson-five.html')

@app.route('/lesson_six')
# Renders the lesson-six page
def lesson_six():
    return render_template('lesson-six.html')

@app.route('/advanced_lesson')
# Renders the advanced-lesson page with the required lessons information from mongoDB
def advanced_lesson():
    addLesson = mongo.db.lessons.find()
    return render_template('advanced-lesson.html', add_lesson=addLesson)

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)