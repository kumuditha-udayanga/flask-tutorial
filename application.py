from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/user/<name>")
def display_user(name):
    print(name)


@app.route("/total/<int:amount>")
def display_total_amount(amount):
    print(amount)


@app.route("/path/<path:sub_path>")
def take_to_subpath(sub_path):

    print(sub_path)


@app.route("/key/<uuid:api_key>")
def display_key(api_key):
    print(api_key)