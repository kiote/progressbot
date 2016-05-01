from flask import Flask
from flask import request
import telegram
import os
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Not much to see here"
    elif request.method == 'POST':
        bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN', 'empty_token'))
        user_name = request.json["message"]["chat"]["username"]
        chat_id = request.json["message"]["chat"]["id"]
        bot.sendMessage(chat_id, text="Hi! %s" % user_name)
        return "hi %s" % user_name

if __name__ == "__main__":
    app.run()
