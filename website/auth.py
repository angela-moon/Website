from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user
from flask_login.utils import login_required
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    admin_user = User(password=generate_password_hash("adminpass", method="sha256"))
    db.session.add(admin_user)
    db.session.commit()
    
    if request.method == "POST":
        password = request.form.get("password")
        
        if check_password_hash(admin_user.password, password):
            flash("Logged in successfully.", category="success")
            login_user(admin_user, remember=True)
            return redirect(url_for("views.home"))  
        else:
            flash("Incorrect password.", category="error")      

    return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", category="success")
    return redirect(url_for("views.home"))

