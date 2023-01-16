from flask import Flask

app = Flask (__name__)

@app.route("/")
def hello():
    return"how are you"

@app.route("/home")
def hello2():
    return"how was your day"

# if __name__ == "__main__":
if __name__ == "__main__":
    app.run(debug = True)