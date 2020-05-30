# Third Milestone Project

### Python Chat
The Python codes for the chat are the same as in the lessons of Code Institute. Click [here]() to find the link.

## Get the .gitignore file
- touch .gitignore

## How to Install Flask
- sudo pip3 install flask

## Connection Python to MongoDB
- sudo pip3 install flask-pymongo
- sudo pip3 install dnspython

## Deployment onto Heroku
- Install Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

- Install Heroku
brew tap heroku/brew && brew install heroku

- Login to Heroku 
heroku login

- Connect to Github
git init 

- Add requirements.txt
sudo pip3 freeze -- local > requirements.txt

- Deployment onto Github
git add .
git status
git commit -m ""
git push heroku master
heroku git:remote -a language-learners-app

- Add Procfile 
echo web: python app.py > Procfile
git add .
git commit -m "Added Procfile"
git push heroku master
heroku ps:scale web=1

```python
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
```

- Images on index.html
[Pixabay](https://pixabay.com/photos/notebook-workplace-desk-iphone-336634/)
[Pixabay](https://pixabay.com/de/photos/code-javascript-programmieren-3337044/)
[pxhere](https://pxhere.com/en/photo/1446103)
[pxhere](https://pxhere.com/en/photo/1366348)
[pxhere](https://pxhere.com/en/photo/860609)
[pxhere](https://pixabay.com/de/photos/sch%C3%BCler-eingabe-tastatur-text-849825/)
[pxhere](https://pxhere.com/en/photo/1434873)
[pxhere](https://pxhere.com/en/photo/1435021)
[Pixabay](https://pixabay.com/de/illustrations/netz-netzwerk-programmierung-3706562/)
[pxhere](https://pxhere.com/en/photo/693080)

planner
[Pixabay](https://pixabay.com/de/photos/routenplaner-2019-jahr-kalender-3820633/)