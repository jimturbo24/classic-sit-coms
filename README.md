### About

tv_comedies is a site for fans of classic situational comedies. This site is still under construction.

### How to deploy this app to Heroku
* Clone this repository (Fork it first if you wish to modify it at some point)
* Sign up for a Heroku account if you don't have one, then download the Heroku [toolbelt](https://toolbelt.heroku.com/).
* Login to Heroku at the terminal command line with: $`heroku login`
* In a Python 3 shell (eg. iPython3) run (print a key for use in step 7):
```python
import random
print('DJANGO_SECRET_KEY="' + ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789@#$%^&*(-_=+)') for i in range(50)]) + '"')
```
* At the terminal command line run: $`heroku create`
* Step 4 will create an app with a random name like "damp-taiga-14318"
* At the command line run: $`heroku config:set DJANGO_SETTINGS_MODULE="tv_comedies.settings_production" --app <app name from step 4>`
* Next run: $`heroku config:set DJANGO_SECRET_KEY="<key from step 3>" --app <app name from step 4>`
* Next run: $`heroku git:remote --app <app name from step 4>`
* From the classic-sit-coms directory run: $`git subtree push --prefix tv_comedies/ heroku master`
* Next run: $`heroku ps:scale web=1`
* View the app in a web browser by navigating to: `https://<app name from step 4>.herokuapp.com/login/`

### Design

This file attempts to make sense of some of the design decisions for the site.

### Main classes

Series
Episodes
Characters
Cast/Crew
Reviews
Trivia

### Modify the look/feel of the page
Story: As a user I want to see a clean modern page so that I can enjoy the experience
Estimate: 3 hrs.
Actual: 4.5 hrs.
Pull Request:

### Create New User
Story: As a new user I want create a new account so that I can use the site.
Estimate: 2 hrs.
Actual:
Pull Request:

### Add a user review
Story: As a user I want write a review of the shows so that the world may know.
Estimate: 2 hrs.
Actual:
Pull Request:

### Create links
Story: As a user I want be able to click on links to access data so that I can navigate the site more easily.
Estimate: 3 hrs.
Actual:
Pull Request:

### Add prev/next buttons
Story: As a user I want to browse content by using prev/next button so that I can surf better.
Estimate: 2 hrs.
Actual:
Pull Request:

### Add site search
Story: As a user I want search the site so that I can find content easily.
Estimate: 8 hrs.
Actual:
Pull Request:
