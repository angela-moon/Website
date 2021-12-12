from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from flask_login.utils import login_required

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("index.html", user=current_user)

@views.route("/about")
def about():
    return render_template("about.html", user=current_user)

@views.route("/blog")
def blog():
    return render_template("blog.html", user=current_user)

@views.route("/projects")
def projects():
    return render_template("project.html", user=current_user)

@views.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get("text")
        if not text:
            flash("Post cannot be empty.")
        else:
            flash("Post created!")
    return render_template("create_post.html", user=current_user)

