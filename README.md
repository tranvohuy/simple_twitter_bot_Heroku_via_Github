# simple_twitter_bot_Heroku_via_Github
This bot is deployed via Github from Heroku website.

* Go to https://dashboard.heroku.com/apps/ >> create new app >> type a new name >> in ```Deploy```,```Deployment method```, choose ```GitHub``` instead of ```Heroku CLI```
* You have to enter KEYs and VALUEs fromo Twitter Dev app into ```Config Vars``` in ```Settings```.

* Deploy the master branch. It will run ```bot.py``` once.

* Go to ```Overview```>>```Configure Dynos```>> Turn ```woker``` ON, or set up a scheduler.
