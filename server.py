import os
import telegram

from flask import request

from chat.cerebrum import Cerebrum
from init import app


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Not much to see here"
    elif request.method == 'POST':
        bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN', 'empty_token'))
        update = telegram.Update.de_json(request.json)
        text = Cerebrum(update).get_respond()
        bot.sendMessage(update.message.chat_id, text=text, parse_mode='Markdown')
        return text

if __name__ == "__main__":
    app.run()
