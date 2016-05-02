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
        update = telegram.Update.de_json(request.json)
        text = "Hi, %s!" % update.message.chat.username
        bot.sendMessage(update.message.chat_id, text=text)
        return text

if __name__ == "__main__":
    app.run()
