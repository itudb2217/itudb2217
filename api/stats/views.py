from flask import Blueprint, jsonify, request, render_template
from dbops.stats import Stats

api = Blueprint("stats_api", __name__, template_folder="templates")


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    stat = Stats.get_by_id(id)
    if not stat:
        return jsonify({"status": "fail", "message": "stat does not exist"})

    return render_template("stat.html", Stat=stat)

    # html


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
        stat = Stats.create(data)
        print(stat)
        if not stat:
            return jsonify({"status": "fail", "message": "can not be created"})
        return render_template("stat.html", Game=stat)
    return jsonify({"status": "fail", "message": "cadsdasdasd"})


@api.route("/get/all", methods=["GET", "POST"])
def get_all():
    stats = Stats.get_all()
    if not stats:
        return jsonify({"status": "fail", "message": "stats does not exist"})
    return render_template("stats.html", Stats=stats)


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    if request.method == "POST":
        Stats.delete(id)
        return jsonify({"status": "success"})
    return True


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):
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
        stat = Stats.update(data)
        return jsonify({"status": "success"})
    return True
