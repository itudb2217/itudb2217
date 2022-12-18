from .base import Base


class team(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "teams")

    def create(self, team):
        self.cursor.execute(
            "INSERT INTO teams VALUES(NULL, ?,?,?,?,?,?,?,?)",
            (
                team["teamName"],
                team["abbreviation"],
                team["playOff"],
                team["numOfGames"],
                team["matchPoints"],
                team["fieldGoals"],
                team["percentageFG"],
                team["seasonID"],
            ),
        )
        self.conn.commit()

    def update(self, team):
        self.cursor.execute(
            "UPDATE teams SET name=?, season=? WHERE id=?",
            (
                team["teamName"],
                team["abbreviation"],
                team["playOff"],
                team["numOfGames"],
                team["matchPoints"],
                team["fieldGoals"],
                team["percentageFG"],
                team["seasonID"],
                team["id"],
            ),
        )
        self.conn.commit()

    def get_by_id(self, id):
        Team = {}
        try:
            row = super().get_by_id(id)
            Team["teamName"] = row["teamName"]
            Team["abbreviation"] = row["abbreviation"]
            Team["playOff"] = row["playOff"]
            Team["numOfGames"] = row["numOfGames"]
            Team["matchPoints"] = row["matchPoints"]
            Team["fieldGoals"] = row["fieldGoals"]
            Team["percentageFG"] = row["percentageFG"]
            Team["seasonID"] = row["seasonID"]
            Team["id"] = row["id"]

        except:
            Team = None

        return Team

    def get_all(self):
        Teams = []
        try:
            rows = super().get_all()
            for row in rows:
                Team = {}
                Team["teamName"] = row["teamName"]
                Team["abbreviation"] = row["abbreviation"]
                Team["playOff"] = row["playOff"]
                Team["numOfGames"] = row["numOfGames"]
                Team["matchPoints"] = row["matchPoints"]
                Team["fieldGoals"] = row["fieldGoals"]
                Team["percentageFG"] = row["percentageFG"]
                Team["seasonID"] = row["seasonID"]
                Team["id"] = row["id"]
                Teams.append(Team)
        except:
            Teams = None
        return Teams

    def get_by_season(self, id):
        Teams = []
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE seasonID=?", (id,)
            )
            rows = self.cursor.fetchall()
            for row in rows:
                Team = {}
                Team["teamName"] = row["teamName"]
                Team["abbreviation"] = row["abbreviation"]
                Team["playOff"] = row["playOff"]
                Team["numOfGames"] = row["numOfGames"]
                Team["matchPoints"] = row["matchPoints"]
                Team["fieldGoals"] = row["fieldGoals"]
                Team["percentageFG"] = row["percentageFG"]
                Team["seasonID"] = row["seasonID"]
                Team["id"] = row["id"]
                Teams.append(Team)
        except:
            Teams = None
        return Teams


Team = team("testing.db")
