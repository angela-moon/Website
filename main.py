from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "1234" # temporary secret key

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/projects")
def projects():
    return render_template("project.html")

if __name__ == "__main__":
    app.run(debug=True)