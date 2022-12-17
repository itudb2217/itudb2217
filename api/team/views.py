from flask import Blueprint, jsonify, render_template, request
from dbops.team import Team

api = Blueprint("team_api", __name__, template_folder="templates")


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    team = Team.get_by_id(id)
    if not team:
        return jsonify({"status": "fail", "message": "team does not exist"})

    return render_template("team.html", Team=team)

    # html


@api.route("/create", methods=["POST", "GET"])
def createTeam():
    if request.method == "POST":
        data = {
            "teamName": request.form["teamName"],
            "playOff": request.form["playOff"],
            "numOfGames": request.form["numOfGames"],
            "matchPoints": request.form["matchPoints"],
            "fieldGoals": request.form["fieldGoals"],
            "percentageFG": request.form["percentageFG"],
            "seasonID": request.form["seasonID"],
        }
        team = Team.create(data)
        if not team:
            return jsonify({"status": "fail", "message": "can not be created"})
    return jsonify({"status": "success", "data": team})


@api.route("/get/all", methods=["GET", "POST"])
def get_all():
    teams = Team.get_all()
    if not teams:
        return jsonify({"status": "fail", "message": "does not exist"})
    return render_template("teams.html", Teams=teams)


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    Team.delete(id)
    return jsonify({"status": "success"})


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):

    team = Team.update("teamData")
    return jsonify({"status": "success"})
