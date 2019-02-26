# simple_twitter_bot_Heroku_via_Github
This bot is deployed via Github from Heroku website. There are many blog posts about Twitter bot. However, the codes are huge or complicated for beginners who do not know what lines of code are important. This repository is a very simple bot. A beginner can build up a more complex bot from here.

* Go to https://dashboard.heroku.com/apps/ >> create new app >> type a new name >> in ```Deploy```,```Deployment method```, choose ```GitHub``` instead of ```Heroku CLI```
* You have to enter KEYs and VALUEs fromo Twitter Dev app into ```Config Vars``` in ```Settings```.

* Deploy the master branch. It will run ```bot.py``` once.

* Go to ```Overview```>>```Configure Dynos```>> Turn ```woker``` ON, or set up a scheduler.
