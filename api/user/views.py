from flask import Blueprint


api = Blueprint("user_api", __name__)

from flask import Blueprint, redirect, render_template, request
from flask import flash, url_for, session, jsonify
from dbops.user import User


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({"status": "fail", "message": "user does not exist"})
    return jsonify({"status": "success", "data": user})


@api.route("/get/all", methods=["GET", "POST"])
def get_all():
    data = User.get_all()
    # print(data)
    return jsonify({"status": "success", "data": data})


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    User.delete(id)
    return jsonify({"status": "success"})


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):

    return jsonify({"status": "success"})
