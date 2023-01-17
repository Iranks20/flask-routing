from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/home/<name>')
def welcome_name(name):
    # return 'Welcome ' + name + '!'
    return 'welcoming ' + name + ' you ' + name + ' am correct'


# if __name__ == "__main__":
if __name__ == "__main__":
    app.run(debug = True)