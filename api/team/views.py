from flask import Blueprint, jsonify
from dbops.team import Team

api = Blueprint("team_api", __name__)


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    user = Team.get_by_id(id)
    if not user:
        return jsonify({"status": "fail", "message": "user does not exist"})
    return jsonify({"status": "success", "data": user})

    # html 


@api.route("/create", methods=["POST", "GET"])
def createTeam():
    team = Team.create("teamData")
    return True


@api.route("/get/all", methods=["GET", "POST"])
def get_all():
    data = Team.get_all()
    print(data)
    return jsonify({"status": "success", "data": data})


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    Team.delete(id)
    return jsonify({"status": "success"})


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):

    team = Team.update("teamData")
    return jsonify({"status": "success"})