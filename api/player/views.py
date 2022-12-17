from flask import Blueprint, jsonify, request, render_template
from dbops.player import Player

api = Blueprint("player_api", __name__, template_folder="templates")


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    player = Player.get_by_id(id)
    if not player:
        return jsonify({"status": "fail", "message": "player does not exist"})
    return render_template("players.html", Player=player)


@api.route("/create", methods=["POST", "GET"])
def createPlayer():
    if request.method == "POST":
        data = {
            "playerName": request.form["playerName"],
            "position": request.form["position"],
            "age": request.form["age"],
            "leauge": request.form["leauge"],
            "experince": request.form["experince"],
            "teamID": request.form["teamID"],
            "seasonID": request.form["seasonID"],
        }
        player = Player.create(data)
        if not player:
            return jsonify({"status": "fail", "message": "can not be created"})
    return jsonify({"status": "success", "data": player})


@api.route("/get/all", methods=["GET", "POST"])
def get_all():
    players = Player.get_all()
    if not players:
        return jsonify({"status": "fail", "message": "players does not exist"})
    return render_template("players.html", Players=players)


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    Player.delete(id)
    return jsonify({"status": "success"})


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):

    return jsonify({"status": "success"})
