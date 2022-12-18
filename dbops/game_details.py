from .base import Base


class game_details(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "game_detail")

    def create(self, game):
        self.cursor.execute(
            f"INSERT INTO  {self.table_name} VALUES(NULL, ?, ?)",
            (game["awayTeam"], game["homeTeam"]),
        )
        self.conn.commit()

    def update(self, game_stats):
        self.cursor.execute(
            f"UPDATE  {self.table_name} SET name=?, surname=? WHERE id=?",
            (
                game_stats["awayTeam"],
                game_stats["awayTeam"],
                game_stats["id"],
            ),
        )
        self.conn.commit()

    def get_by_id(self, id):

        game_details = {}
        try:
            row = super().get_by_id(id)

            game_details["comment"] = row["comment"]
            game_details["minute"] = row["minute"]
            game_details["nickName"] = row["nickName"]
            game_details["city"] = row["city"]
            game_details["startingPosition"] = row["startingPosition"]
            game_details["gameID"] = row["gameID"]
            game_details["id"] = row["id"]

        except:
            print("HERERERER")
            game_details = None

        return game_details

    def get_all(self):
        game_stats = []
        try:
            rows = super().get_all()

            for row in rows:
                game_stat = {}
                game_stat["awayTeam"] = row["awayTeam"]
                game_stat["awayTeam"] = row["awayTeam"]
                game_stat["id"] = row["id"]
                game_stats.append(game_stat)
        except:
            game_stats = None
        return game_stats

    def get_by_team(self, id):
        game_stats = []
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE awayTeam=?", (id,)
            )
            rows = self.cursor.fetchall()

            for row in rows:
                game_stat = {}
                game_stat["awayTeam"] = row["awayTeam"]
                game_stat["awayTeam"] = row["awayTeam"]
                game_stat["id"] = row["id"]
                game_stats.append(game_stat)
        except:
            game_stats = None
        return game_stats


GameDetails = game_details("testing.db")
