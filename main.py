from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/servicedetails")
def servicedetails():
    return render_template("service-details.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/blogdetails")
def blogdetails():
    return render_template("blog-details.html")

@app.route("/contact")
def contact():
    return render_template("contact-us.html")

@app.route('/home/<name>')
def welcome_name(name):
    # return 'Welcome ' + name + '!'
    return 'welcoming ' + name + ' you ' + name + ' am correct'


# if __name__ == "__main__":
if __name__ == "__main__":
    app.run(debug = True)