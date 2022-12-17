from .base import Base


class game_stats(Base):
    def _init_(self, db_name):
        Base._init_(self, db_name, "games")

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

        game_stat = {}
        try:
            row = super().get_by_id(id)

            game_stat["awayTeam"] = row["awayTeam"]
            game_stat["awayTeam"] = row["awayTeam"]
            game_stat["id"] = row["id"]

        except:
            game_stat = None

        return game_stat

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


GameStats = game_stats("testing.db")
# {"name": "apo", "surname": "simsek", "teamID": 1}
# Player.create({"name": "abdullah", "surname": "yildirim", "teamID": 3})
# # print(Player.get_all())

# print(Player.get_by_team(3))
