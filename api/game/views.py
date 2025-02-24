from flask import (
    Blueprint,
    jsonify,
    request,
    redirect,
    render_template,
    url_for,
    session,
)
from dbops.game import Game  # ???
from dbops.stats import Stats  # ???

api = Blueprint("game_api", __name__)


@api.route("/create", methods=["POST", "GET"])
def createTeam():

    if request.method == "POST":
        data = {
            "teamName": request.form["teamName"],
            "loss": request.form["loss"],
            "win": request.form["win"],
            "age": request.form["age"],
            "winPercentage": request.form["winPercentage"],
            "conference": request.form["conference"],
            "abbreviation": request.form["abbreviation"],
            "seasonID": request.form["seasonID"],
            "playerID": request.form["playerID"],
        }
        game = Stats.create(data)
        print(data)
        if not game:
            return jsonify({"status": "fail", "message": "can not be created"})
        return render_template("game_create.html", Game=game)
    return render_template("game_create.html", Game=game)


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    if "email" in session:

        game = Game.get_by_id(id)
        return render_template("game.html", Game=game)
    return redirect(url_for("auth_api.login"))


@api.route("/get/season/<season>", methods=["GET", "POST"])
def getBySeason(season):
    if "email" in session:
        print(season)
        games = Game.get_by_season(season)
        print(games)
        if not games:
            return jsonify({"status": "fail", "message": "does not exist"})
        return render_template("games.html", Games=games)
    return redirect(url_for("auth_api.login"))


@api.route("/get/all", methods=["GET", "POST"])
def get_all():
    if "email" in session:
        games = Game.get_all()
        return render_template("games.html", Games=games)
    return redirect(url_for("auth_api.login"))


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    if "email" in session:
        game = Game.delete(id)
        return jsonify({"status": "success"})
    return redirect(url_for("auth_api.login"))


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if "email" in session:

        if request.method == "POST":
            data = {
                "teamName": request.form["teamName"],
                "loss": request.form["loss"],
                "win": request.form["win"],
                "age": request.form["age"],
                "winPercentage": request.form["winPercentage"],
                "conference": request.form["conference"],
                "abbreviation": request.form["abbreviation"],
                "seasonID": request.form["seasonID"],
                "playerID": request.form["playerID"],
                "id": id,
            }
            stat = Game.update(data)

            if not stat:
                return jsonify({"status": "fail", "message": "can not be created"})
            return jsonify({"status": "success", "data": stat})

        return jsonify({"status": "success"})
    return redirect(url_for("auth_api.login"))
