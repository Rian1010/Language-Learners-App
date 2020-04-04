import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__, template_folder='templates')

app.config["MONGO_DBNAME"] = 'myFirstCluster'
app.config["MONGO_URI"] = 'mongodb+srv://Rian:j4JWQ1Ntzc9u0U7m@myfirstcluster-ges2b.mongodb.net/learner-app-data?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'

mongo = PyMongo(app)


@app.route('/')
def index():
    username = session.get('username')
    if username:
        users = mongo.db.users.find()
        return render_template('index.html', users=users)
    return render_template('register.html')


@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        password = request.form['password']
        user = mongo.db.users.find_one({"username": username})
        userEmail = mongo.db.users.find_one({"email": email})

        if user and userEmail and mongo.db.users.find_one({"password": password}):
            session['username'] = user["username"]
            session["email"] = userEmail["email"]
            return render_template('index.html')
        else:
            return 'Invalid email or password'

    return render_template('login.html')

    # First tries
    # if request.method == "POST":
    #     users = mongo.db.users
    #     user_name = users.find_one({'name': request.form['username']})
    #     user_pass = users.find_one({'password': request.form['password']})
    #     print(user_name)
    #     print(user_pass)
    #     username = request.form.get("username")
    #     password = request.form.get("password")
    #     print(username)
    #     print(password)

    #     if not username in user_name:
    #         return "Invalide username"
    #     else:
    #         user = users[username]

    #     if not password in user_pass:
    #         return 'Invalid password'
    #     else:
    #         user = users[username]
    #         session["username"] = user["username"]
    #         return render_template('index.html')

    # return render_template('login.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
    # users = mongo.db.users
    # user_login = users.find_one({'name': request.form['username']})
    # print(user_login)
    # if user_login:
    #     print(request.form['username'])
    #     print(request.form['pass'])
    #     print(session['username'])
    #     print(user_login['password'])
    #     if bcrypt.hashpw(request.form['pass'].encode['utf-8'], user_login['password'].encode('utf-8')) == user_login['password'].encode('utf-8'):
    #         session['username'] = request.form['username']

    #         return render_template('index.html')
    # else:
    #     flash(f'Invalid username')

    # return render_template('Invalid username or password')


@app.route('/register', methods=['POST', 'GET'])
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

    # if request.method == 'POST':
    #     users = mongo.db.users
    #     user_exists = users.find_one({'name': request.form['username']})

    #     if user_exists is None:
    #         hashpass = bcrypt.hashpw(
    #             request.form['pass'].encode('utf-8'), bcrypt.gensalt())
    #         users.insert_one(
    #             {'name': request.form['username'], 'password': hashpass})
    #         session['username'] = request.form['username']
    #         return redirect(url_for('index'))

    #     return 'The username that you have entered already exists!'

    # return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/signin')


@app.route('/task_manager')
def task_manager():
    user = session.get('username')
    if user:
        return render_template('task-manager.html', tasks=mongo.db.tasks.find(), lessons=mongo.db.lessons.find())
    return render_template('login.html')

@app.route('/add_tasks')
def add_task():
    return render_template('add-tasks.html', tasks=mongo.db.tasks.find(), lessons=mongo.db.lessons.find())


@app.route('/insert_task', methods=['GET', 'POST'])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one({
        "username": session['username'],
        "lesson_name": request.form.get('lesson_name'),
        'task_name': request.form.get('task_name'),
        'task_descrip': request.form.get('task_description'),
        'due_date': request.form.get('due_date'),
    })
    # user_lesson = request.form.get('lesson_name')
    # task_name = request.form.get('task_name')
    # task_descrip = request.form.get('task_description')
    # due_date = request.form.get('due_date')
    # task_manager_data = {
    # "lesson_name": user_lesson,
    # "the_task": [  {"task_name": task_name,
    #             "task_descrip": task_descrip,
    #             "due_date": due_date},

    #             {"task_name": task_name,
    #             "task_descrip": task_descrip,
    #             "due_date": due_date}]
    # }
    # task.insert_one(task_manager_data)
    return redirect(url_for('task_manager'))


@app.route('/update_task/<task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = mongo.db.tasks
    task.update({'_id': ObjectId(task_id)},
                {
                "username": session['username'],
                "lesson_name": request.form.get('lesson_name'),
                'task_name': request.form.get('task_name'),
                'task_descrip': request.form.get('task_descrip'),
                'due_date': request.form.get('due_date'),
                })
    
    return redirect(url_for('task_manager'))


@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_lesson = mongo.db.lessons.find()
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template('edit-task.html', task=the_task, lessons=the_lesson)

@app.route('/delete_full_task/<task_id>/<title_id>')
def delete_full_task(task_id, title_id):
    mongo.db.task_title.delete_many({'username': session['username']})
    return redirect(url_for('task_manager'))


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
    initDate = datetime.today().strftime("%A %D")
    return render_template('add-posts.html', posts=mongo.db.posts.find(), lessons=mongo.db.lessons.find(), initDate=initDate)

@app.route('/insert_post', methods=['GET', 'POST'])
def insert_post():
    posts = mongo.db.posts 
    posts.insert_one({
        "username": session['username'],
        "lesson_name": request.form.get("lesson_name"),
        "post_content": request.form.get("post_content"),
        "initDate": datetime.today().strftime("%A %D %H:%M:%S"),
        "edit_today": "Edit: None",
    })
    return redirect(url_for('community'))

@app.route('/update_post/<post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    posts = mongo.db.posts
    # thePost = mongo.db.posts.find_one({"_id": ObjectId(post_id)}
    posts.update_one({'_id': ObjectId(post_id)},
                 { "$set": {
        "username": session['username'],
        'lesson_name': request.form.get('lesson_name'),
        'post_content': request.form.get('post_content'),
        "edit_today": datetime.now().strftime("Edited: %A %D"),
        # "initDate": thePost.initDate,
    }})
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
    addLesson1 = mongo.db.addLesson1.find()
    return render_template('lesson-one.html', addLesson1=addLesson1)


@app.route('/add_new_lesson1')
def add_new_lesson1():
    return render_template('add-lesson-1.html', addLesson1=mongo.db.addLesson1.find())


@app.route('/update_lesson1/<addLesson1_id>', methods=['GET', 'POST'])
def update_lesson1(addLesson1_id):
    addLesson1 = mongo.db.addLesson1
    addLesson1.update({'_id': ObjectId(addLesson1_id)},
                      {
        "username": session['username'],
        'heading1': request.form.get('heading1'),
        'lesson_content1': request.form.get('lesson_content1'),
    }
    )
    return redirect(url_for('advanced_lesson', addLesson1=addLesson1))


@app.route('/insert_lesson1', methods=['GET', 'POST'])
def insert_lesson1():
    addLesson1 = mongo.db.addLesson1
    addLesson1.insert_one({
        "username": session['username'],
        "heading1": request.form.get('heading1'),
        'lesson_content1': request.form.get('lesson_content1'),
    })
    return redirect(url_for('advanced_lesson'))

@app.route('/edit_lesson1/<addLesson1_id>')
def edit_lesson1(addLesson1_id):
    addLesson1 = mongo.db.addLesson1.find_one({"_id": ObjectId(addLesson1_id)})
    return render_template('edit-lesson-1.html', addLesson1=addLesson1)


@app.route('/delete_lesson1/<addLesson1_id>')
def delete_lesson1(addLesson1_id):
    mongo.db.addLesson1.delete_one({"_id": ObjectId(addLesson1_id)})
    return redirect(url_for('advanced_lesson'))


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
    addLesson1 = mongo.db.addLesson1.find()
    return render_template('advanced-lesson.html', add_lesson1=addLesson1)


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
