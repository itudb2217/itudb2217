from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
    redirect,
    session,
    url_for,
)
from dbops.game_details import GameDetails  # ???

api = Blueprint("gameDetail_api", __name__, template_folder="templates")


@api.route("/get/<id>", methods=["GET", "POST"])
def get(id):
    if "email" in session:
        gameDetail = GameDetails.get_by_id(id)
        print(gameDetail)
        if not gameDetail:
            return jsonify({"status": "fail", "message": "game detail does not exist"})

        return render_template("gameDetail.html", GameDetail=gameDetail)
    return redirect(url_for("auth_api.login"))


@api.route("/get/all", methods=["GET", "POST"])
def get_all():
    if "email" in session:
        gameDetails = GameDetails.get_all()
        if not gameDetails:
            return jsonify({"status": "fail", "message": "game details does not exist"})

        return render_template("gameDetails.html", GameDetails=gameDetails)
    return redirect(url_for("auth_api.login"))


@api.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    if "email" in session:
        gameDetail = GameDetails.delete(id)
        return jsonify({"status": "success"})
    return redirect(url_for("auth_api.login"))


@api.route("/update/<id>", methods=["GET", "POST"])
def update(id):
    if "email" in session:
        gameDetail = GameDetails.update(id)
        return jsonify({"status": "success"})
    return redirect(url_for("auth_api.login"))
