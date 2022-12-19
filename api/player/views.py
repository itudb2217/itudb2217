from flask import (
    Blueprint,
    jsonify,
    request,
    render_template,
    session,
    redirect,
    url_for,
)
from dbops.player import Player

api = Blueprint("player_api", __name__, template_folder="templates")


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    if "email" in session:
        player = Player.get_by_id(id)
        print(player)
        if not player:
            return jsonify({"status": "fail", "message": "player does not exist"})
        return render_template("player.html", Player=player)
    return redirect(url_for("auth_api.login"))


@api.route("/get/team/<id>", methods=["GET", "POST"])
def get_by_team(id):
    if "email" in session:
        players = Player.get_by_team(id)
        print(players)
        if not players:
            return jsonify({"status": "fail", "message": "player does not exist"})
        return render_template("players.html", Players=players)
    return redirect(url_for("auth_api.login"))


@api.route("/create", methods=["POST", "GET"])
def createPlayer():
    if "email" in session:
        if request.method == "POST":
            data = {
                "playerName": request.form["playerName"],
                "position": request.form["position"],
                "age": request.form["age"],
                "league": request.form["league"],
                "experience": request.form["experience"],
                "teamID": request.form["teamID"],
                "seasonID": request.form["seasonID"],
            }
            print(data)
            player = Player.create(data)
            return redirect(url_for("home_api.home"))

        return render_template("create_player.html")

    return redirect(url_for("auth_api.login"))


@api.route("/get/all", methods=["GET", "POST"])
def get_all():
    if "email" in session:
        players = Player.get_all()
        if not players:
            return jsonify({"status": "fail", "message": "players does not exist"})
        return render_template("players.html", Players=players)
    return redirect(url_for("auth_api.login"))


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):

    if "email" in session:
        Player.delete(id)
        return redirect(url_for("home_api.home"))

    return redirect(url_for("auth_api.login"))


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if "email" in session:
        player = Player.get_by_id(id)
        print(player)
        if request.method == "POST":
            data = {
                "playerName": request.form["playerName"],
                "position": request.form["position"],
                "age": request.form["age"],
                "league": request.form["league"],
                "experience": request.form["experience"],
                "teamID": request.form["teamID"],
                "abbreviation": request.form["abbreviation"],
                "seasonID": request.form["seasonID"],
                "id": id,
            }
            print("deneme")
            player = Player.update(data)
            return render_template("update_player.html", Player=player)
        return render_template("update_player.html", Player=player)

    return redirect(url_for("auth_api.login"))
