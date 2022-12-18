from .base import Base


class endOfseason(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "endofseasons")

    def create(self, endOfSeason):
        self.cursor.execute(
            "INSERT INTO teams VALUES(NULL, ?, ?,?,?,?,?,?)",
            (
                endOfSeason["type"],
                endOfSeason["teamNo"],
                endOfSeason["position"],
                endOfSeason["league"],
                endOfSeason["birth"],
                endOfSeason["playerID"],
                endOfSeason["teamID"],
                endOfSeason["season"],
            ),
        )
        self.conn.commit()

    def update(self, endOfSeason):
        self.cursor.execute(
            "UPDATE teams SET type=?, teamNO=?,position=?,voteNo=?,birth=?,playerID=?,teamID=?,  WHERE id=?",
            (
                endOfSeason["type"],
                endOfSeason["teamNo"],
                endOfSeason["position"],
                endOfSeason["league"],
                endOfSeason["birth"],
                endOfSeason["playerID"],
                endOfSeason["teamID"],
                endOfSeason["season"],
            ),
        )
        self.conn.commit()

    def get_by_id(self, id):
        endOfSeason = {}
        try:
            row = super().get_by_id(id)
            endOfSeason["type"] = row["type"]
            endOfSeason["season"] = row["season"]
            endOfSeason["teamNo"] = row["teamNo"]
            endOfSeason["position"] = row["position"]
            endOfSeason["league"] = row["league"]
            endOfSeason["birth"] = row["birth"]
            endOfSeason["playerID"] = row["playerID"]
            endOfSeason["teamID"] = row["teamID"]
            endOfSeason["id"] = row["id"]

        except:
            endOfSeason = None

        return endOfSeason

    def get_by_season(self, id):
        endOfSeasons = []
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE season=?", (id,)
            )
            rows = self.cursor.fetchall()
            for row in rows:
                endOfSeason = {}
                endOfSeason["type"] = row["type"]
                endOfSeason["teamNo"] = row["teamNo"]
                endOfSeason["season"] = row["season"]
                endOfSeason["position"] = row["position"]
                endOfSeason["league"] = row["league"]
                endOfSeason["birth"] = row["birth"]
                endOfSeason["playerID"] = row["playerID"]
                endOfSeason["teamID"] = row["teamID"]
                endOfSeason["id"] = row["id"]
                endOfSeasons.append(endOfSeason)
        except:
            endOfSeasons = None
        return endOfSeasons

    def get_all(self):
        endOfSeasons = []
        try:
            rows = super().get_all()
            for row in rows:
                endOfSeason = {}
                endOfSeason["type"] = row["type"]
                endOfSeason["teamNo"] = row["teamNo"]
                endOfSeason["season"] = row["season"]
                endOfSeason["position"] = row["position"]
                endOfSeason["league"] = row["league"]
                endOfSeason["birth"] = row["birth"]
                endOfSeason["playerID"] = row["playerID"]
                endOfSeason["teamID"] = row["teamID"]
                endOfSeason["id"] = row["id"]
                endOfSeasons.append(endOfSeason)
        except:
            endOfSeasons = None
        return endOfSeasons


EndOfseason = endOfseason("testing.db")
