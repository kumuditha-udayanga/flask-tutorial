from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/user/<name>")
def display_user(name):
    print(name)
    return name


@app.route("/total/<int:amount>")
def display_total_amount(amount):
    print(amount)
    return "Amount is " + str(amount)


@app.route("/path/<path:sub_path>")
def take_to_subpath(sub_path):

    print(sub_path)
    return sub_path


@app.route("/key/<uuid:api_key>")
def display_key(api_key):
    print(api_key)
    return "done"


@app.route("/home")
def display_home():
    return render_template('home.html', thing_to_say='hello')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == "Admin":
            print(request.form['username'])
            return 'Login Success'
    return 'login fail'
