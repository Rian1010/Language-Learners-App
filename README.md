# JavaScript Learning Site

This project is my third milestone project that I have done on the Full Stack Software Development Course at Code Institute. The main focus of this project was to have a website with instructions of how JavaScript works, so that users can learn it.

## Purpose of This Project
This is a website that teaches how to use JavaScript. One can go through the different lesson pages, add their own lessons, plan what and when they want to learn something through the time manager and post interesting discoveries about codes on the community page.

- Here is a list of the sections that the website has:
- Home page: Shows everything that the site has to offer, lesson pages, a task-manager page, a community page and a form, with which a user can send me an email for inquiries. It includes nice pictures and an animation
- Login/registration page: Allows users to sign in or sign up. The website persists between each user’s login
- Lesson pages: Those pages have content about how to use JavaScript and the Advanced Learning page has a section at the bottom, where users can add their own lessons. Only the author of the lesson can edit and delete the added lessons.
- Add lesson page: Enables a user to add a new lesson
- Edit lesson page: Enables a user to edit their created lesson
- Task Manager: Users can add multiple tasks to plan what lessons they need to learn, when they want to learn it and they can add a description to it. Each user can only see, edit and delete their own added tasks, not the tasks of any other account
- Add task page: Enables a user to add a new task to the task manager
- Edit task page: Enables a user to edit their created task
- Community: Users can post about interesting discoveries or thoughts on JavaScript codes for others to see. A user can only edit and delete their own posts, not the posts from any other account
- Add community page: Enables a user to add a new post about JavaScript to the community page
- Edit community page: Enables a user to edit their posted posts

## UX
### User Stories
- As a user, I would like to learn JavaScript for free
- As a user, I would like to register and login
- As a user, I would like to see what topics of JavaScript are covered on the website, through the home page
- As a user, I would like to be able to add lessons, if something important could be added to the website
- As a user, I would like to have a task-manager, on which I can plan my time
- As a user, I would like to specify which lessons I want to learn, add quick notes to remember for next time in a small input field, and include a date of when I plan to proceed the learning
- As a user, I would like to share ideas or discoveries with others about JavaScript and edit or delete the posts, if I want to
- As a user, I would like to contact the admin of the website for questions about the website and or JavaScript
- I would like to find contact and social media informations of the website in the footer

## Front-End Design
The main colours that I chose to use for this website are light blue and white. The font-family that I used was sans serif because I found that it fit the website well. My goal was to make the website look simple with simple looking colours and many pictures in a way that it looks modern. I tried to add motion through an animation on the home page and had the background-image of the boxes on the home page that link to the task-manager and community page attached as fixed.

## Utilised Technologies
### Languages
- HTML5
- CSS3
- JavaScript
- Python3

### Frameworks
- Bootstrap 4

### Database
- MongoDB

### API
- EmailJS

### Validators

### Other Tools
- jQuery
- Github: hosts the website
- Git: version control
- VSCode: code editor
- Flask 
- Pymongo
- BSON

## Process
### Flask 
I learned almost all of the code that I wrote with flask at [Code Institute](https://codeinstitute.net/). However, there were some things I tried to do through research and the help of tutors from Code Institute.

One of those things was the registration functionality.

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