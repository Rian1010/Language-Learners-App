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