from flask import Flask

app = Flask (__name__)

@app.route("/")
def hello():
    return"how are you"

@app.route("/home")
def hello2():
    return"how was your day"

@app.route('/home/<name>')
def welcome_name(name):
    # return 'Welcome ' + name + '!'
    return 'welcoming ' + name + ' you ' + name + ' am correct'


# if __name__ == "__main__":
if __name__ == "__main__":
    app.run(debug = True)