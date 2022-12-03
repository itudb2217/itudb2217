from flask import Flask, jsonify, request, render_template, flash
from api.auth.views import api as auth_api
from api.team.views import api as team_api
from api.player.views import api as player_api
from api.user.views import api as user_api
from api.stats.views import api as stats_api
from api.game_detail.views import api as gameDetail_api
from api.end_of_season.views import api as endOfSeason_api
from api.game.views import api as game_api


app = Flask(__name__)
app.config["SECRET_KEY"] = "somesecretkey"


app.register_blueprint(blueprint=auth_api, url_prefix="/api/auth")
app.register_blueprint(blueprint=user_api, url_prefix="/api/user")
app.register_blueprint(blueprint=team_api, url_prefix="/api/team")
app.register_blueprint(blueprint=player_api, url_prefix="/api/player")
app.register_blueprint(blueprint=stats_api, url_prefix="/api/stats")
app.register_blueprint(blueprint=gameDetail_api, url_prefix="/api/gamedetail")
app.register_blueprint(blueprint=endOfSeason_api, url_prefix="/api/endofseason")
app.register_blueprint(blueprint=game_api, url_prefix="/api/game")


if __name__ == "__main__":
    app.run(debug=True)
