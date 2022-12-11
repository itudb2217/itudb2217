from flask import Blueprint, jsonify
from dbops.player import Player

api = Blueprint("player_api", __name__)


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    user = Player.get_by_id(id)
    if not user:
        return jsonify({"status": "fail", "message": "user does not exist"})
    return jsonify({"status": "success", "data": user})


@api.route("/get/all", methods=["GET", "POST"])
def get_all():
    data = Player.get_all()
    print(data)
    return jsonify({"status": "success", "data": data})


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    Player.delete(id)
    return jsonify({"status": "success"})


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):

    return jsonify({"status": "success"})