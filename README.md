[![Build Status](https://travis-ci.org/kiote/progressbot.svg?branch=master)](https://travis-ci.org/kiote/progressbot)

# Progress Bot

This Telegram bot helps you to develop your habits. They say you need 21 days to create a new habit, so this bot will track you 21 days long until you succeed. 

There are a lot of the same apps created already: https://exist.io/blog/habit-apps/ but I want a bot! So here it is. It based on a simple idea: track your progress every day (see [Seinfeld's method](http://lifehacker.com/281626/jerry-seinfelds-productivity-secret))

### Running locally

1. set PYTHONPATH with `export PYTHONPATH=.` under project's directory
2. set DATABASE_URL with `export DATABASE_URL=postgresql://progressbot:123456@localhost:5432/progressbot` (this is default url, change to your own)
3. Initialize database with `python chat/models/creator.py`

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
