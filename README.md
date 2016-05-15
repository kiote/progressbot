[![Build Status](https://travis-ci.org/kiote/progressbot.svg?branch=master)](https://travis-ci.org/kiote/progressbot)

# Progress Bot

Telegram bot for tracking (and improve!) your daily habits. You say what you've done, ProgressBot remembers it and gives you a good overview every month.

There are a lot of the same apps created already: https://exist.io/blog/habit-apps/ but I want a bot! So here it is. It based on a simple idea: track your progress every day (see [Seinfeld's method](http://lifehacker.com/281626/jerry-seinfelds-productivity-secret))

### Running locally

1. set PYTHONPATH with `export PYTHONPATH=.` under project's directory
2. set DATABASE_URL with `eport DATABASE_URL=postgresql://progressbot:123456@localhost:5432/progressbot` (this is default url, change to your own)

## Telegram API

it's based on [getting updates](https://core.telegram.org/bots/api#getting-updates) with callbacks from Telegram API.

# Trello board

https://trello.com/b/Yr8UsSec/progress-bot

# Mind Map

https://www.mindmeister.com/686860905/progress-bot

# Try it

https://telegram.me/Progress2Bot

# Heroku App

https://progress2bot.herokuapp.com/
