import csv, sqlite3

con = sqlite3.connect("testing.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY AUTOINCREMENT,playerName TEXT NOT NULL,position TEXT NOT NULL,age INTEGER NOT NULL,leauge TEXT NOT NULL,experince TEXT NOT NULL,teamID INTEGER NOT NULL,seasonID INTEGER NOT NULL,FOREIGN KEY (teamID) REFERENCES TEAMS(id) ON DELETE CASCADE ON UPDATE CASCADE,FOREIGN KEY (seasonID) REFERENCES ENDOFSEASONS(id) ON DELETE CASCADE ON UPDATE CASCADE)"
)

with open("Players.csv", "r") as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (
            i["player"],
            i["pos"],
            i["age"],
            i["lg"],
            i["experience"],
            i["tm"],
            i["seas_id"],
        )
        for i in dr
    ]

cur.executemany(
    "INSERT INTO players (playerName, position, age,  leauge, experince,teamID,seasonID) VALUES (?, ?, ?, ?, ?, ?, ?);",
    to_db,
)

with open("Teams.csv", "r") as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (
            i["team"],
            i["abbreviation"],
            i["playoffs"],
            i["g"],
            i["mp"],
            i["fg"],
            i["fg_percent"],
            i["season"],
        )
        for i in dr
    ]

cur.executemany(
    "INSERT INTO teams (teamName, abbreviation,playOff, numOfGames,  matchPoints, fieldGoals,percentageFG,seasonID) VALUES (?, ?,?, ?, ?, ?, ?, ?);",
    to_db,
)
con.commit()

con.close()
