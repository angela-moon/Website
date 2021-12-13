from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask.helpers import url_for
from flask_login import current_user
from flask_login.utils import login_required
from .models import Post
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return render_template("index.html", user=current_user)

@views.route("/about")
def about():
    return render_template("about.html", user=current_user)

@views.route("/blog")
def blog():
    posts = Post.query.all()
    return render_template("blog.html", user=current_user, posts=posts)

@views.route("/projects")
def projects():
    return render_template("project.html", user=current_user)

@views.route("/create-post", methods=["GET", "POST"])
@login_required
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("text")
        if not title:
            flash("Title cannot be empty.")
        elif not text:
            flash("Post cannot be empty.")
        else:
            post = Post(title=title, text=text)
            db.session.add(post)
            db.session.commit()
            flash("Post created!")
            return redirect(url_for("views.blog"))
    return render_template("create_post.html", user=current_user)

@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    
    if not post:
        flash("Post does not exist.")
    else:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted.")
        
    return redirect(url_for("views.home"))

@views.route("/post/<id>")
def view_post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template("post.html", user=current_user,post=post)
    