from flask import Blueprint, redirect, render_template, request, session
from flask import flash, url_for, jsonify
from dbops.user import User

api = Blueprint("home_api", __name__)


@api.route("/home", methods=["GET", "POST"])
def home():
    if "email" in session:
        return render_template("main.html")
    return redirect(url_for("auth_api.login"))
