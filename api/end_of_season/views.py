from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
    session,
    redirect,
    url_for,
)
from dbops.endOfSeason import EndOfseason

api = Blueprint("endofSeason_api", __name__)


@api.route("/create", methods=["POST", "GET"])
def createTeam():
    if "email" in session:
        if request.method == "POST":
            data = {
                "type": request.form["type"],
                "teamNo": request.form["teamNo"],
                "position": request.form["position"],
                "voteNo": request.form["voteNo"],
                "birth": request.form["birth"],
                "season": request.form["season"],
                "playerID": request.form["playerID"],
                "seasonID": request.form["seasonID"],
            }
            endOfseason = EndOfseason.create(data)
            if not endOfseason:
                return jsonify({"status": "fail", "message": "can not be created"})
        return jsonify({"status": "success", "data": endOfseason})
    return redirect(url_for("auth_api.login"))


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    if "email" in session:

        endOfseason = EndOfseason.get_by_id(id)
        if not endOfseason:
            return jsonify({"status": "fail", "message": "endOfseason does not exist"})

        return render_template("endOfseason.html", EndOfseason=endOfseason)
    return redirect(url_for("auth_api.login"))


@api.route("/get/season/<season>", methods=["GET", "POST"])
def getBySeason(season):
    if "email" in session:
        print(season)
        endOfseasons = EndOfseason.get_by_season(season)
        print(endOfseasons)
        if not endOfseasons:
            return jsonify({"status": "fail", "message": "does not exist"})
        return render_template("endOfseasons.html", EndOfseasons=endOfseasons)
    return redirect(url_for("auth_api.login"))


@api.route("/get/all", methods=["GET", "POST"])
def get_all():
    if "email" in session:
        endOfseasons = EndOfseason.get_all()
        if not endOfseasons:
            return jsonify({"status": "fail", "message": "endOfseasons does not exist"})

        return render_template("endOfseasons.html", EndOfseasons=endOfseasons)
    return redirect(url_for("auth_api.login"))


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    if "email" in session:

        endOfseason = EndOfseason.delete(id)

        return jsonify({"status": "success"})
    return redirect(url_for("auth_api.login"))


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if "email" in session:

        data = {
            "type": request.form["type"],
            "teamNo": request.form["teamNo"],
            "position": request.form["position"],
            "voteNo": request.form["voteNo"],
            "birth": request.form["birth"],
            "season": request.form["season"],
            "playerID": request.form["playerID"],
            "seasonID": request.form["seasonID"],
            "id": id,
        }
        endOfseason = EndOfseason.update(data)

        return jsonify({"status": "success"})
    return redirect(url_for("auth_api.login"))
