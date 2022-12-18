from .base import Base


class game(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "games")

    def create(self, game):
        self.cursor.execute(
            f"INSERT INTO  {self.table_name} VALUES(NULL, ?, ?,?,?,?,?)",
            game["gameDate"],
            game["gameStatus"],
            game["homeTeamPoints"],
            game["percentageFG"],
            game["percentageFT"],
            game["homeTeamID"],
            game["visitorTeamID"],
            game["id"],
        )
        self.conn.commit()

    def update(self, game):
        self.cursor.execute(
            f"UPDATE  {self.table_name} SET gameDate=?, gameStatus=?, homeTeamPoints=?, percentageFG=?, percentageFT=?, homeTeamID=?,visitorTeamID=? WHERE id=?",
            (
                game["gameDate"],
                game["gameStatus"],
                game["homeTeamPoints"],
                game["percentageFG"],
                game["percentageFT"],
                game["homeTeamID"],
                game["visitorTeamID"],
                game["id"],
            ),
        )
        self.conn.commit()

    def get_by_id(self, id):

        Game = {}
        try:
            row = super().get_by_id(id)

            Game["gameDate"] = row["gameDate"]
            Game["gameStatus"] = row["gameStatus"]
            Game["homeTeamPoints"] = row["homeTeamPoints"]
            Game["percentageFG"] = row["percentageFG"]
            Game["percentageFT"] = row["percentageFT"]
            Game["homeTeamID"] = row["homeTeamID"]
            Game["visitorTeamID"] = row["visitorTeamID"]
            Game["id"] = row["id"]

        except:
            Game = None

        return Game

    def get_all(self):
        Games = []
        try:
            rows = super().get_all()

            for row in rows:
                Game = {}
                Game["gameDate"] = row["gameDate"]
                Game["gameStatus"] = row["gameStatus"]
                Game["homeTeamPoints"] = row["homeTeamPoints"]
                Game["percentageFG"] = row["percentageFG"]
                Game["percentageFT"] = row["percentageFT"]
                Game["homeTeamID"] = row["homeTeamID"]
                Game["visitorTeamID"] = row["visitorTeamID"]
                Game["id"] = row["id"]
                Games.append(Game)
        except:
            Games = None
        return Games

    def get_by_team(self, id):
        Games = []
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE awayTeam=?", (id,)
            )
            rows = self.cursor.fetchall()

            for row in rows:
                Game = {}
                Game["gameDate"] = row["gameDate"]
                Game["gameStatus"] = row["gameStatus"]
                Game["homeTeamPoints"] = row["homeTeamPoints"]
                Game["percentageFG"] = row["percentageFG"]
                Game["percentageFT"] = row["percentageFT"]
                Game["homeTeamID"] = row["homeTeamID"]
                Game["visitorTeamID"] = row["visitorTeamID"]
                Game["id"] = row["id"]
                Games.append(Game)
        except:
            Games = None
        return Games


Game = game("testing.db")
