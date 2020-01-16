# Third Milestone Project

## How to Install Flask
- sudo pip3 install flask

## Deployment onto Heroku
- Install Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

- Install Heroku
brew tap heroku/brew && brew install heroku
12:03 am

- Login to Heroku 
heroku login

- Connect to Github
git init 

- Add Procfile requirements.txt
sudo pip3 freeze -- local > requirements.txt

- Deployment onto Github
git add .
git status
git commit -m ""
$ heroku git:remote -a language-learners-app
git push -u origin master


