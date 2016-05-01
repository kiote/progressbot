from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Not much to see here"
    elif request.method == 'POST':
        return "hi"

if __name__ == "__main__":
    app.run()
