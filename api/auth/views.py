from flask import Blueprint, redirect, render_template, request, session
from flask import flash, url_for, jsonify
from dbops.user import User

api = Blueprint("auth_api", __name__)


@api.route("/register", methods=["GET", "POST"])
def register():
    if "email" in session:
        return redirect(url_for("home_api.home"))
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if User.get_by_email(email):
            flash("Given email already exist!!!")
            return redirect(url_for("auth_api.register"))
        User.create({"email": email, "password": password})

        flash("successfully registered, please login")

        return redirect(url_for("auth_api.login"))

    return render_template("register.html")


@api.route("/login", methods=["GET", "POST"])
def login():
    if "email" in session:
        return redirect(url_for("home_api.home"))
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.get_by_email(email)

        if not user:
            flash("User not found!!!")
            return redirect(url_for("auth_api.login"))
        if password != user["password"]:
            flash("Wrong password!!!")
            return redirect(url_for("auth_api.login"))
        session["email"] = email
        return redirect(url_for("home_api.home"))
    return render_template("login.html")


@api.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop("email", None)
    return render_template("login.html")
