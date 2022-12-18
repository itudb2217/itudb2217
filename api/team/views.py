from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
    session,
    redirect,
    url_for,
)
from dbops.team import Team
from dbops.stats import Stats


api = Blueprint("team_api", __name__, template_folder="templates")


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    if "email" in session:
        team = Team.get_by_id(id)
        print(team)
        if not team:
            return jsonify({"status": "fail", "message": "team does not exist"})

        return render_template("team.html", Team=team)
    return redirect(url_for("auth_api.login"))

    # html


@api.route("/create", methods=["POST", "GET"])
def createTeam():
    if "email" in session:
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
    return redirect(url_for("auth_api.login"))


@api.route("/get/all", methods=["GET", "POST"])
def getAll():
    if "email" in session:
        teams = Team.get_all()
        if not teams:
            return jsonify({"status": "fail", "message": "does not exist"})
        return render_template("teams.html", Teams=teams)
    return redirect(url_for("auth_api.login"))


@api.route("/get/season/<season>", methods=["GET", "POST"])
def getBySeason(season):
    if "email" in session:
        teams = Team.get_by_season(season)
        if not teams:
            return jsonify({"status": "fail", "message": "does not exist"})
        return render_template("teams.html", Teams=teams)
    return redirect(url_for("auth_api.login"))


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    if "email" in session:
        Team.delete(id)
        return jsonify({"status": "success"})
    return redirect(url_for("auth_api.login"))


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if "email" in session:
        team = Team.update("teamData")
        return jsonify({"status": "success"})
    return redirect(url_for("auth_api.login"))
