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
I learned almost all of the code that I wrote with flask at [Code Institute](https://codeinstitute.net/). However, there were some things I tried to do through research and the help of tutors from Code Institute. Two of those things were the login and registration functionalities.

At first, I tried to research how to make a login functionality and found a [YouTube video](https://www.youtube.com/watch?v=vVx1737auSE) by [PrettyPrinted](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)that showed how to do it, using bcrypt. 

```python
if request.method == 'POST':
        users = mongo.db.users
        user_exists = users.find_one({'name': request.form['username']})

        if user_exists is None:
            hashpass = bcrypt.hashpw(
                request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one(
                {'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'The username that you have entered already exists!'

    return render_template('register.html')
```
This is the code that I had tried at first for the registration functionality from the video. It gave me an idea of how to get new inputed user information and grab their given details and how to create a session, all if the user did not exist in the database already. Otherwise, if those details did match, the new user would not be able to register with that information. This code did not work, so I used print statements to try to debug it and researched more about it, but the sources that I found became quite complicate and I had little time to finish the project, as it was one of the last things that I was trying to do. Therefore, I was trying to find another easier way to do it, although I liked that it would be so easy to encrypt passwords in the database through bcrypt.

On the other hand, I had also tried to make a login functionality by using the same video for bcrypt and it worked! Here is the code that I had firstly used with bcrypt: 

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    users = mongo.db.users
    user_login = users.find_one({'name': request.form['username']})
    if user_login:
        if bcrypt.hashpw(request.form['pass'].encode['utf-8'], user_login['password'].encode('utf-8')) == user_login['password'].encode('utf-8'):
            session['username'] = request.form['username']

            return render_template('index.html')
    else:
        flash(f'Invalid username')

    return render_template('Invalid username or password')
```

I changed it later on, because bcrypt for registration looked quite complicated on other sources, while I did not have much time left to finish the project, so I found simpler ways of making a login and registration forms.

So, after multiple days of lots of research and trying things out a Slack member, called Sipo from the Code Institute course helped me and so, I managed to find a way to get the registration function to work. He helped me by using the knowledge he got from doing [his third milestone project](https://github.com/sipostudent/Veggit-Online-Cookbook-/blob/master/run.py). 

```python
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
```

This is the code that I have now. It works just fine, I tested if the correct error shows up, if I enter registration details that already exist, as a test and it worked. Also, registerin a new user also worked correctly. The reason why Sipo helped me through his own third milestone project is because another student from Code Institute were trying to do the same thing, so we talked about it and researched for days, while we both needed to hurry. On around the fifth day of working on it and loads of research and not finding a solution that works correctly, Sipo helped us to get it to work correctly. 

As for the login page, I tried to make sense of it and used the code below, but it did not work.

```python
    if request.method == "POST":
        users = mongo.db.users
        user_name = users.find_one({'name': request.form['username']})
        user_pass = users.find_one({'password': request.form['password']})
        username = request.form.get("username")
        password = request.form.get("password")

        if not username in user_name:
            return "Invalide username"
        else:
            user = users[username]

        if not password in user_pass:
            return 'Invalid password'
        else:
            user = users[username]
            session["username"] = user["username"]
            return render_template('index.html')

    return render_template('login.html')
```

I used the help of the tutors to understand flask login functionalities better and with their help I wrote this code above. However, since it did not work, I tried a make sense of it again with the some help on Slack and got this code below:

```python
@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form['password']
        userEmail = mongo.db.users.find_one({"email": email})

        if userEmail and mongo.db.users.find_one({"password": password}):
            session['username'] = userEmail["username"]
            session["email"] = userEmail["email"]
            return render_template('index.html')
        else:
            return 'Invalid email or password'

    return render_template('login.html')
```

This code works correctly and the logic behind it is basically that it checks if the inputed username and password can be found in the database or not. If it is found, a user can login, if not, then an error message that says, 'Invalid email or password', is shown. This then means that user has either entered wrong login information or still needs to register. I tried having the functionality that a user can enter either a username or and email address by including the following two variables: `username = request.form["username"]` and `user = mongo.db.users.find_one({"username": username})`. The `username` variable should grab the inputed username, while the `user` variable should be included into the if statement, such as in, `if userEmail and user and mongo.db.users.find_one({"password": password}):`, so that it would check if the entered username is already in the database or not. However, as I kept getting errors through this, I removed this part because of the little time that I had left for this project. 

Another code that I found out with the help of [Stackoverflow](https://stackoverflow.com/questions/49408509/signout-after-user-disconnects-on-flask) and [W3Schools](https://www.w3schools.com/python/ref_dictionary_pop.asp) is for a user to logout.

```python
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/signin')
```

This function causes a user to be able to logout. I connect this function to a logout button in the navigation bar that only appears, if a user is logged in. If a logged in user clicks on it, the function removes the username session and replaces it with None, as the default value.

Something else that I wanted to do on the community page is to save the time of when each post is posted and to display it on the posts. 

```python
def community():
    posts = mongo.db.posts.find()
    eachPost = mongo.db.posts.find_one()
    initDate = eachPost['initDate'].strftime("%A %D %H:%M")
    return render_template('community.html', posts=posts, eachPost=eachPost, initDate=initDate, lesson=mongo.db.lessons.find())

```

This code above, is what I tried first with the help of the course videos, the tutors from Code Institute and [the strftime website](https://strftime.org/). It did not work, but what I was trying to do is to ge the time of when the post was posted from the database with the `eachPost` variable, in the formate I chose with strftime, but as it did not work correctly, I had to find another way of doing it. So, I asked the tutors from Code Institute to help get a better understanding of what I am trying to do, in order to be lead to the right solution. As a result, I got the following code, which works just fine:

```python
@app.route('/community')
def community():
    posts = []
    for result in mongo.db.posts.find():
        result["initDate"] = result['initDate'].strftime("%A %D %H:%M")
        posts.append(result)
    return render_template('community.html', posts=posts, lesson=mongo.db.lessons.find())
```

I iterated through the 'posts' collection of the database to return the values of each `initDate` key and tested the variables through print statements.

In order to save the information of the time when a post was posted, I came up with the following function: 

```python 
@app.route('/insert_post', methods=['GET', 'POST'])
def insert_post():
    # returns the community page
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
```

The `initDate` key, save the current time with datetime.today(), while the `edit_today` key sets its value to 'Edit: None', to show that now edits have been commited after the post. The rest of the code correctly saves the information of the session username, lesson name and post content.

```python
@app.route('/update_post/<post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    # Allows a post to be updated
    posts = mongo.db.posts
    thePost = mongo.db.posts.find_one({"_id": ObjectId(post_id)}
    posts.update_one({'_id': ObjectId(post_id)},
        "author": session['username'],
        'lesson_name': request.form.get('lesson_name'),
        'post_content': request.form.get('post_content'),
        "edit_today": "Edited: {}.{}.{}".format(the_date.strftime("%d"), the_date.strftime("%m"),the_date.strftime("%y")),
        "initDate": thePost.initDate,
    })
    return redirect(url_for('community'))
```

What I first tried to do here was to let a update of the lesson name and post content happen for the session username, if a user wanted to change something. This worked, but what did not work was to change the date of the `edit_today` key, withouth affect the `initDate` key's value. So, I had to find a way to keep the `initDate` value the same, while allowing everything else to change.

```python
@app.route('/update_post/<post_id>', methods=['GET', 'POST'])
def update_post(post_id):
    # Allows a post to be updated
    posts = mongo.db.posts
    posts.update_one({'_id': ObjectId(post_id)},
                 { "$set": {
        "author": session['username'],
        'lesson_name': request.form.get('lesson_name'),
        'post_content': request.form.get('post_content'),
        "edit_today": "Edited: {}".format(datetime.now()),
    return redirect(url_for('community'))
```

After trying out multiple ways that did not work rightly, I got it to work like in this code above. The `$set` operator is used to update the specific fields that are being updated in the function and the `edit_today` key correctly saves the latest time that the post was edited on. I used the [PyMongo Documentation](https://api.mongodb.com/python/current/api/pymongo/collection.html), the [mongoDB Documentation](https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/), [W3Schools](https://www.w3schools.com/nodejs/nodejs_mongodb_update.asp) tutors from Code Institute and Slack members to lead me to the correct way of doing this. However, I wanted to format the saved time to only display the day, month and the year with the help of [this W3Schools web page](https://www.w3schools.com/python/python_datetime.asp) and the [strftime website](https://strftime.org/). I tried doing the following:

```python
date_time = datetime.datetime.now()
```
Then, in the `$set` operator for the `edit_today` key I tried doing this:

```python
"edit_today": "Edited: {}.{}.{}".format(date_time.strftime("%d"), date_time.strftime("%m"), date_time.strftime("%y")),
```

However, this did not work rightly, so I put it back to the following way that I got it to work correctly before because of the little amount of time I had left to complete this project:

```python
"edit_today": "Edited: {}".format(datetime.now()),
```

## Testing
- Print statements were used to test and debug python code
- `console.log()` was used to test JavaScript code
- Tried registering with a new account
    - Test worked and MongoDB picked up the right details
- Tried logging in with the previously registered account
    - Test worked and logged me in correctly
- Tried logging in with false information
    - The correct error message occured
- Tried registering with user information that already exists
    - The correct error message occured
- Checked if all the hover effects on the navigation bars work correctly and if each button in the navigation bar links to the right web page, after logging in
    - Both tests worked rightly
- Checked if the JavaScript animation and all the css hover effects on the homepage were working correctly 
    - All tests went well
- Checked if each link on the home page lead to the correct web page
    - All links lead to the right web page
- Tested if adding lessons to the advanced lessons page worked and if one was able to delete and edit them only through the account of the author of that lesson, not through any other account
    - Tests worked rightly, as I was able to add, edit and delete only lessons from my account and no other account
- Tested if adding a task to the task manager and deleting and editing it worked correctly
    - Tests worked fine, as I was able to do all of it
- Tested if other accounts could see the tasks added by other accounts
    - Test worked rightly, as each account could only see their own added tasks
- Tested if lessons that are added by users would appear in the lesson option list on the add tasks page
    - Test worked, as it appeared in the option list
- Tested if removing a lesson that is added by a user would disappear from the lesson option list on the add tasks page
    - Test worked, as it disappeared from the option list 
- Tested 




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