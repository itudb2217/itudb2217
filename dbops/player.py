from .base import Base


class player(Base):
    def __init__(self, db_name):
        Base.__init__(self, db_name, "players")

    def create(self, player):
        self.cursor.execute(
            "INSERT INTO players VALUES(NULL, ?, ?,?,?,?,?,?)",
            player["playerName"],
            player["position"],
            player["age"],
            player["league"],
            player["experience"],
            player["teamID"],
            player["seasonID"],
            
        )
        self.conn.commit()

    def update(self, player):
        self.cursor.execute(
            "UPDATE players SET playerName=?, position=?, age=?, league=?, experience=?, teamID=?,seasonID=? WHERE id=?",
            (
                player["playerName"],
                player["position"],
                player["age"],
                player["league"],
                player["experience"],
                player["teamID"],
                player["seasonID"],
                player["id"],
            ),
        )
        self.conn.commit()

    def get_by_id(self, id):

        Player = {}
        try:
            row = super().get_by_id(id)
            Player["playerName"] = row["playerName"]
            Player["position"] = row["position"]
            Player["age"] = row["age"]
            Player["league"] = row["league"]
            Player["experience"] = row["experience"]
            Player["teamID"] = row["teamID"]
            Player["seasonID"] = row["seasonID"]
            Player["id"] = row["id"]

        except:
            Player = None

        return Player

    def get_all(self):
        Players = []
        try:
            rows = super().get_all()

            for row in rows:
                Player = {}
                Player["playerName"] = row["playerName"]
                Player["position"] = row["position"]
                Player["age"] = row["age"]
                Player["league"] = row["league"]
                Player["experience"] = row["experience"]
                Player["teamID"] = row["teamID"]
                Player["seasonID"] = row["seasonID"]
                Player["id"] = row["id"]
                Players.append(Player)
        except:
            Players = None
        return Players

    def get_by_team(self, id):
        Players = []
        try:
            self.cursor.execute(
                f"SELECT * FROM {self.table_name} WHERE teamID=?", (id,)
            )
            rows = self.cursor.fetchall()

            for row in rows:
                Player = {}
                Player["playerName"] = row["playerName"]
                Player["position"] = row["position"]
                Player["age"] = row["age"]
                Player["league"] = row["league"]
                Player["experience"] = row["experience"]
                Player["teamID"] = row["teamID"]
                Player["seasonID"] = row["seasonID"]
                Player["id"] = row["id"]
                Players.append(Player)
        except:
            Players = None
        return Players


Player = player("testing.db")
