# Language Learner's App (JavaScript Learning Site)

This project is the third milestone project that I have done on the Full Stack Software Development Course at Code Institute. The main focus of this project was to have a website with instructions of how JavaScript works, so that users can learn it. The project is published [here](https://language-learners-app.herokuapp.com/)

## Purpose of This Project
This is a website that teaches how to use JavaScript. One can go through the different lesson pages, add their own lessons, plan what and when they want to learn something through the time-manager and post interesting discoveries about codes on the community page.

- Here is a list of the sections that the website has:
- Home page: Shows everything that the site has to offer, so lesson pages, a task-manager page, a community page and a form, with which a user can send me an email for inquiries. It includes nice pictures and an animation
- Login/registration page: Allow users to sign in or sign up. The website persists between each user’s login
- Lesson pages: Those pages have content about how to use JavaScript and the Advanced Learning page has a section at the bottom, where users can add their own lessons. Only the author of the lesson can edit and delete the added lessons, but a lesson can be views from any user account.
- Add lesson page: Enables a user to add a new lesson
- Edit lesson page: Enables a user to edit their created lesson
- Task-Manager: Users can add multiple tasks to plan what lessons they need to learn, when they want to learn it and they can add a description to it. Each user can only see, edit and delete their own added tasks, not the tasks of any other user account
- Add task page: Enables a user to add a new task to the task manager
- Edit task page: Enables a user to edit their created task
- Community: Users can post about interesting discoveries or thoughts on JavaScript codes for others to see. A user can edit and delete only their own posts, not the posts of any other account
- Add community page: Enables a user to add a new post about JavaScript to the community page
- Edit community page: Enables a user to edit their posted posts

## UX
### User Stories
- As a user, I would like to learn JavaScript for free
- As a user, I would like to register and login
- As a user, I would like to see what topics of JavaScript are covered on the website, through the home page
- As a user, I would like to be able to add lessons, if something important about JavaScript could be added to the website
- As a user, I would like to have a task-manager, on which I can plan my time
- As a user, I would like to specify in a task-manager which lessons I want to learn, add quick notes to remember for next time in a small description field, and include a date of when I plan to proceed the learning
- As a user, I would like to share ideas or discoveries with others about JavaScript and edit or delete the posts, if I want to
- As a user, I would like to contact the creator of the website for questions about the website and or JavaScript
- I would like to find contact and social media information of the creator or brand of the website in the footer

## Front-End Design
The main colours that I chose to use for this website are light blue and white. The font-family that I used was the default sans serif because I found that it fit the website well. My goal was to make the website look simple with simple looking colours and many pictures in a way that it looks modern. I tried to add motion through an animation on the home page and had the background-image of the boxes on the home page that link to the task-manager and community page attached as fixed. I wanted to do so in order to make the website feel more lively.

## Wireframes
- [Login page](https://github.com/Rian1010/Language-Learners-App/blob/master/wireframes/flask-login-page-wireframe.jpeg)
- [Registration page](https://github.com/Rian1010/Language-Learners-App/blob/master/wireframes/flask-registration-page-wireframe.jpeg)
- [Homepage](https://github.com/Rian1010/Language-Learners-App/blob/master/wireframes/flask-homepage-wireframe.jpeg)
- [Task-manager page](https://github.com/Rian1010/Language-Learners-App/blob/master/wireframes/flask-task-manager-wireframe.jpeg)
- [Community page](https://github.com/Rian1010/Language-Learners-App/blob/master/wireframes/flask-community-wireframe.jpeg)
- [Lesson Pages](https://github.com/Rian1010/Language-Learners-App/blob/master/wireframes/flask-lessons-wireframe.jpeg)
- [Pages to add or edit lessons, tasks or posts](https://github.com/Rian1010/Language-Learners-App/blob/master/wireframes/flask-add-edit-wireframe.jpeg)

Some of the ideas that are shown in the wireframes have been changed throughout the process of the website for better design and logic.

## Utilised Technologies
### Languages
- HTML5: As mark-up language
- CSS3: For styling
- JavaScript: To add functionalities and animations in the front-end
- Python3: To add functionalities through the back-end

### Frameworks
- Bootstrap 4: For responsive web designing 

### Database
- MongoDB: To store information into a database

### API
- EmailJS: Allow users to send me a well formatted email 

### Validators
- [PEP8 Validator](http://pep8online.com/)
- [JavaScript Validator](https://jshint.com/)
- [CSS Validator](http://csslint.net/)
- [HTML Validator](https://www.freeformatter.com/html-validator.html)

### Other Tools
- jQuery: JavaScript library
- Github: hosts the website
- Git: version control
- VSCode: code editor
- Flask: Python framework to work with in the back-end
- Jinja2: Python web template engine

## Features
### Existing Features
- EmailJS API for users to send me emails
- Users can add their own lessons, tasks and posts 
- Users can edit and delete posts, tasks and lessons only from their own accounts, these cannot be edited or deleted from any other user account
- Users can view other's posts and lessons
- Users can only see their own tasks and no tasks of other accounts
- Every lesson that a user adds gets included into the option list on the add tasks page and the edit tasks page 

### Future Features and Unsolved Problems
I did not manage to allow users to write in seperate paragraphs in whatever they want to insert to add or edit their own lessons, tasks or posts. I did not have enough time to work on it, but I am planning to implement that in the future through JavaScript.

Something else that I wanted to do was to colour specific words in the lesson boxes of all the lesson pages to make it look a bit like in a code editor. Here is the JavaScript code that I tried:

```javascript
let words = document.querySelectorAll('.words');
console.log(words);

words.forEach(word => {
    let blueWords = ["true", "function", "return", "break", "continue"];
    let purpleWords = ["for", "forEach", "while", "false", "+", "-", "*", "/", "%"]
    let orangeWords = ["if", "else"];
    let yellowWords = ["switch", "case"];
    let redWords = ["let", "var", "const"];

    let blue = "blue";
    let purple = "purple";
    let orange = "orange";
    let yellow = "yellow";
    let red = "red";

    function wordColour(array, theColour) {
        for (i = 0; i <= array.length; i++) {
            if (word.innerHTML.includes(array[i])) {
                word.style.color = theColour;
            }
        }
    }
    wordColour(blueWords, blue);
    wordColour(purpleWords, purple);
    wordColour(orangeWords, orange);
    wordColour(yellowWords, yellow);
    wordColour(redWords, red);
})
```

I tried using this function and forEach loop that I made by myself, but it would turn an entire paragraph to the colour that is supposed to be assigned to the word, instead of just the single word. Due to the little amount of time that I had left for this project, I did not continue trying it. 

Also, I want to add more content to the lessons in the future. I planned to add more than there currently are, but I did not manage to write more because of timing. 

## Process
### Flask 
I learned almost all of the code that I wrote with flask at [Code Institute](https://codeinstitute.net/). However, there were some things I tried to do through lots of research and the help of tutors and Slack members from Code Institute. Two of those things were the login and registration functionalities.

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
This is the code that I had tried at first for the registration functionality from the video. It gave me an idea of how to get new inputed user information, grab their given details and how to create a session, all if the user did not exist in the database already. Otherwise, if those details did match, the new user would not be able to registrate with that information. This code did not work, so I used print statements to try to debug it and researched more about it, but the sources that I found became quite complicated and I had little time to finish the project, as it was one of the last things that I was trying to do. Therefore, I was trying to find another easier way to do it, although I liked that it would be so easy to encrypt passwords in the database through bcrypt.

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

So, after multiple days of lots of research and trying things out, a Slack member, called Sipo from the Code Institute course helped me and so, I managed to find a way to get the registration function to work. He helped me by using the knowledge he got from doing [his third milestone project](https://github.com/sipostudent/Veggit-Online-Cookbook-/blob/master/run.py). 

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

This is the code that I have now. It works just fine, I tested if the correct error shows up, if I enter registration details that already exist and it worked. Also, registering a new user worked correctly too. The reason why Sipo helped me through his own third milestone project is because another student from Code Institute and I were trying to get user authentication to work on our projects, so we talked about it and researched for days, while we both needed to hurry. On around the fifth day of working on it and loads of research and not finding a solution that works correctly, Sipo helped us to get it to work correctly. 

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

I used the help of the tutors to understand flask login functionalities better and with their help I wrote this code above. However, since it did not work, I tried to make sense of it again and got this code below:

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

This code works correctly and the logic behind it, is basically that it checks if the inputed username and password can be found in the database or not. If it is found, a user can login, if not, then an error message that says, 'Invalid email or password', is shown. This then means that a user has either entered wrong login information or still needs to register. I tried having the functionality that a user can enter either a username or an email address by including the following two variables: `username = request.form["username"]` and `user = mongo.db.users.find_one({"username": username})`. The `username` variable should grab the inputed username, while the `user` variable should be included into the if statement, such as would be, `if userEmail and user and mongo.db.users.find_one({"password": password}):`, so that it would check if the entered username is already in the database or not. However, as I kept getting errors through this, I removed this part because of the little time that I had left for this project. 

Another code that I found out with the help of [Stackoverflow](https://stackoverflow.com/questions/49408509/signout-after-user-disconnects-on-flask) and [W3Schools](https://www.w3schools.com/python/ref_dictionary_pop.asp) is for a user to logout.

```python
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/signin')
```

This function causes a user to be able to logout. I connected this function to a logout button in the navigation bar that only appears, if a user is logged in. If a logged in user clicks on it, the function removes the username session and replaces it with `None`.

Something else that I wanted to do on the community page is to save the time of when each post is posted and to display it on the posts. 

```python
def community():
    posts = mongo.db.posts.find()
    eachPost = mongo.db.posts.find_one()
    initDate = eachPost['initDate'].strftime("%A %D %H:%M")
    return render_template('community.html', posts=posts, eachPost=eachPost, initDate=initDate, lesson=mongo.db.lessons.find())
```

This code above, is what I tried first with the help of the course videos, the tutors from Code Institute and [the strftime website](https://strftime.org/). It did not work, but what I was trying to do is to get the time of when the post was posted from the database with the `eachPost` variable, in the format I chose with `strftime`, but as it did not work correctly, I had to find another way of doing it. So, I asked the tutors from Code Institute to help me get a better understanding of what I am trying to do, in order to be lead to the right solution. As a result, I got the following code, which works just fine:

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

The `initDate` key, saves the current time with datetime.today(), while the `edit_today` key sets its value to 'Edit: None', to show that no edits have been commited after the initial version of the post. The rest of the code correctly saves the information of the session username, lesson name and post content.

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

What I first tried to do here was to let an update of the lesson name and post content happen for the session username, if a user wanted to change something. This worked, but what did not work was to change the date of the `edit_today` key, withouth affect the `initDate` key's value. So, I had to find a way to keep the `initDate` value the same, while allowing everything else to change.

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

After trying out multiple ways that did not work rightly, I got it to work like in this code above. The `$set` operator is used to update the specific fields that are being updated in the function and the `edit_today` key correctly saves the latest time that the post was edited on. I used the [PyMongo Documentation](https://api.mongodb.com/python/current/api/pymongo/collection.html), the [mongoDB Documentation](https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/) tutors from Code Institute and Slack members to lead me to the correct way of doing this. However, I wanted to format the saved time to only display the day, month and the year with the help of [this W3Schools web page](https://www.w3schools.com/python/python_datetime.asp) and the [strftime website](https://strftime.org/). I tried doing the following:

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

As for the JavaScript EmailJS API, I used the same code as in my second milestone project for it as I had already done the code that I wanted to work on this website. 

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
- Tried adding a post to the community page, editing it and deleting it
    - Tests worked as posts got added displaying the correct information and times of when they were posted and showed that it had not been edited yet
    - Edits displayed the correct information on the community page and the time of when they were edited was displayed rightly
    - Deleting posts worked fine too
- Tried using a different account to edit or delete another account's posts
    - Test worked correctly, as one account could not edit or delete someone else's posts
    - Other accounts can only see the posts of other accounts, as they are supposed to
- Tested if sending an email worked from the section at the bottom of the homepage
    - Test worked well, as I received the email
- Tested if all the links in the footer link to the correct pages by clicking on them
    - Tests worked correctly
- Tested if the phone and email contact information worked rightly from the footer by clicking on them
    - Tests worked rightly
- Tested the responsiveness of the website through a phone and the Chrome DevTools on desktop 
- Tested if any page from the navigation bar can be reached without loging in
    - Test worked as those pages could not be reached

## Environment and Configuration Variables
#### Local Variables
The local variables that I have for this project are in an env.py file. The environment variables that I have in that file are called 'SECRET_KEY', 'MONGO_URI' and 'DEVELOPMENT', which have the values that are required in the app.py file for the mongo URI password, the secret key password and the debug value. As 'DEVELOPMENT' takes care of the debug value, it is set to True locally.

#### Heroku Configuration Variables
The configuration variables that I have on Heroku are the 'IP', 'PORT', 'SECRET_KEY', 'MONGO_URI' and 'DEVELOPMENT' variables. The 'SECRET_KEY' and 'MONGO_URI' contain the same passwords on Heroku as they do locally in the env.py file. The 'DEVELOPMENT' variable is set to 1, while I am working on it, but it is set to False when submitting the project, after working on it.

## Deployments and Installations
### How to Install Flask
- sudo pip3 install flask

### Connection Python to MongoDB
- sudo pip3 install flask-pymongo
- sudo pip3 install dnspython

### Deployment onto Heroku and Github
#### Install Homebrew
- /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

#### Install Heroku
- brew tap heroku/brew && brew install heroku

#### Login to Heroku 
- heroku login 

#### Add requirements.txt
- sudo pip3 freeze -- local > requirements.txt

#### Deployment onto Github
- git add .
- git status
- git commit -m ""
- git push heroku master
- heroku git:remote -a language-learners-app

#### Add a Procfile and make the website work on Heroku
- echo web: python app.py > Procfile
- git add .
- git commit -m "Added Procfile"
- git push heroku master
- heroku ps:scale web=1
- For the website to work on Heroku, the statics must be disabled, through `DISABLE_COLLECTSTATIC=1`


## Resources
### Lesson contents
- [SoloLearn](https://www.sololearn.com/)
- [W3Schools](https://www.w3schools.com/)
- [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)

#### Images on index.html
- [Pixabay](https://pixabay.com/photos/notebook-workplace-desk-iphone-336634/)
- [Pixabay](https://pixabay.com/de/photos/code-javascript-programmieren-3337044/)
- [pxhere](https://pxhere.com/en/photo/1446103)
- [pxhere](https://pxhere.com/en/photo/1366348)
- [pxhere](https://pxhere.com/en/photo/860609)
- [pxhere](https://pixabay.com/de/photos/sch%C3%BCler-eingabe-tastatur-text-849825/)
- [pxhere](https://pxhere.com/en/photo/1434873)
- [pxhere](https://pxhere.com/en/photo/1435021)
- [Pixabay](https://pixabay.com/de/illustrations/netz-netzwerk-programmierung-3706562/)

#### Lesson pages banner picture
- [pxhere](https://pxhere.com/en/photo/693080)

#### More Resources Used In Reasearch
- [strftime website](https://strftime.org/)
- [this W3Schools web page](https://www.w3schools.com/python/python_datetime.asp)
- [mongoDB Documentation](https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/)
- [PyMongo Documentation](https://api.mongodb.com/python/current/api/pymongo/collection.html)
- [Stackoverflow](https://stackoverflow.com/questions/49408509/signout-after-user-disconnects-on-flask)
- [W3Schools](https://www.w3schools.com/python/ref_dictionary_pop.asp)
- [Stackoverflow](https://stackoverflow.com/questions/49408509/signout-after-user-disconnects-on-flask)
- [W3Schools](https://www.w3schools.com/python/ref_dictionary_pop.asp)
- [PyMongo Documentation](https://api.mongodb.com/python/current/api/pymongo/collection.html)
- [this W3Schools web page](https://www.w3schools.com/python/python_datetime.asp)
- [Code Institute](https://codeinstitute.net/)
- [YouTube video](https://www.youtube.com/watch?v=vVx1737auSE)
- [PrettyPrinted](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)
- [his third milestone project](https://github.com/sipostudent/Veggit-Online-Cookbook-/blob/master/run.py)
- [this W3Schools web page](https://www.w3schools.com/python/python_datetime.asp)
- [mongoDB Documentation](https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/)
- [PEP8 Validator](http://pep8online.com/)
- [JavaScript Validator](https://jshint.com/)
- [CSS Validator](http://csslint.net/)
- [HTML Validator](https://www.freeformatter.com/html-validator.html)

## Acknowledgements 
I was inspired to do this project by [Code Institute](https://codeinstitute.net/). Thank you to my mentors, Antonija Šimić  Brian Macharia to guide me throughout the process of the project! Thank you to the tutors, Michael, Tim, Xavier, Anna, Stephan, Kevin, Samantha, Haley, Luca and Niel for helping me with the problems that I encountered.
