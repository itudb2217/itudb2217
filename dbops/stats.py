from .base import Base


class stats(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "stats")

    def create(self, stats):
        print(stats)

        self.cursor.execute(
            f"INSERT INTO  {self.table_name} VALUES(NULL, ?, ?,?, ?, ?,?, ?, ?,?)",
            (
                stats["teamName"],
                stats["loss"],
                stats["win"],
                stats["age"],
                stats["winPercentage"],
                stats["conference"],
                stats["abbreviation"],
                stats["seasonID"],
                stats["playerID"],
            ),
        )
        self.conn.commit()
        return stats

    def update(self, stats):
        self.cursor.execute(
            f"UPDATE  {self.table_name} SET teamName=?, loss=? ,win=?, age=? ,win=? winPercentage=? ,conference=?,win=? abbreviation=? ,seasonID=?,playerID=? WHERE id=?",
            (
                stats["teamName"],
                stats["loss"],
                stats["win"],
                stats["age"],
                stats["winPercentage"],
                stats["conference"],
                stats["abbreviation"],
                stats["seasonID"],
                stats["playerID"],
                stats["id"],
            ),
        )
        self.conn.commit()

    def get_by_id(self, id):

        Stat = {}
        try:
            row = super().get_by_id(id)

            Stat["teamName"] = row["teamName"]
            Stat["loss"] = row["loss"]
            Stat["win"] = row["win"]
            Stat["age"] = row["age"]
            Stat["winPercentage"] = row["winPercentage"]
            Stat["lossPercentage"] = row["lossPercentage"]
            Stat["abbreviation"] = row["abbreviation"]
            Stat["seasonID"] = row["seasonID"]
            Stat["id"] = row["id"]

        except:
            Stat = None

        return Stat

    def get_all(self):
        Stats = []
        try:
            rows = super().get_all()

            for row in rows:
                Stat = {}

                Stat["teamName"] = row["teamName"]
                Stat["loss"] = row["loss"]
                Stat["win"] = row["win"]
                Stat["age"] = row["age"]
                Stat["winPercentage"] = row["winPercentage"]
                Stat["lossPercentage"] = row["lossPercentage"]
                Stat["abbreviation"] = row["abbreviation"]
                Stat["seasonID"] = row["seasonID"]
                Stat["id"] = row["id"]
                Stats.append(Stat)
        except:
            Stats = None
        return Stats

    def get_by_team(self, teamName):
        Stats = []
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE teamName=?", (teamName,)
            )
            rows = self.cursor.fetchall()

            for row in rows:
                Stat = {}
                Stat["teamName"] = row["teamName"]
                Stat["loss"] = row["loss"]
                Stat["win"] = row["win"]
                Stat["age"] = row["age"]
                Stat["winPercentage"] = row["winPercentage"]
                Stat["lossPercentage"] = row["lossPercentage"]
                Stat["abbreviation"] = row["abbreviation"]
                Stat["seasonID"] = row["seasonID"]
                Stat["id"] = row["id"]
                Stats.append(Stat)
        except:
            Stats = None
        return Stats

    def get_by_team_and_season(self, teamName, season):
        Stats = []
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE teamName=? AND seasonID=?",
                (teamName, season),
            )
            rows = self.cursor.fetchall()

            for row in rows:
                Stat = {}
                Stat["teamName"] = row["teamName"]
                Stat["loss"] = row["loss"]
                Stat["win"] = row["win"]
                Stat["age"] = row["age"]
                Stat["winPercentage"] = row["winPercentage"]
                Stat["conference"] = row["conference"]
                Stat["abbreviation"] = row["abbreviation"]
                Stat["seasonID"] = row["seasonID"]
                Stat["id"] = row["id"]
                Stats.append(Stat)
        except:
            Stats = None
        return Stats


Stats = stats("testing.db")
