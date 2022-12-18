import csv, sqlite3



con = sqlite3.connect("testing.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY AUTOINCREMENT,playerName TEXT NOT NULL,position TEXT NOT NULL,age INTEGER NOT NULL,league TEXT NOT NULL,experience TEXT NOT NULL,teamID INTEGER NOT NULL,seasonID INTEGER NOT NULL,FOREIGN KEY (teamID) REFERENCES TEAMS(id) ON DELETE CASCADE ON UPDATE CASCADE,FOREIGN KEY (seasonID) REFERENCES ENDOFSEASONS(id) ON DELETE CASCADE ON UPDATE CASCADE)"
)

with open("Players.csv", "r", encoding="utf8") as fin:
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
    "INSERT INTO players (playerName, position, age,  league, experience,teamID,seasonID) VALUES (?, ?, ?, ?, ?, ?, ?);",
    to_db,
)

with open("Teams.csv", "r", encoding="utf8") as fin:
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
with open("Stats.csv", "r", encoding="utf8") as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (
            i["team"],
            i["abbreviation"],
            i["w"],
            i["l"],
            i["age"],
            i["pw"],
            i["pl"],
            i["season"],
        )
        for i in dr
    ]

cur.executemany(
    "INSERT INTO stats (teamName, abbreviation,win, loss,  age, winPercentage, lossPercentage,seasonID) VALUES (?,?, ?,?, ?, ?, ?, ?);",
    to_db,
)
con.commit()

with open("endofseasons.csv", "r", encoding="utf8") as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (
            i["type"],
            i["number_tm"],
            i["position"],
            i["lg"],
            i["birth_year"],
            i["season"],
            i["player_id"],
            i["tm"],
        )
        for i in dr
    ]

cur.executemany(
    "INSERT INTO endofseasons (type, teamNo,position, league,  birth, season, playerID,teamID) VALUES (?,?, ?,?, ?, ?, ?, ?);",
    to_db,
)
con.commit()

with open("games.csv", "r", encoding="utf8") as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (
            i["GAME_ID"],
            i["GAME_DATE_EST"],
            i["GAME_STATUS_TEXT"],
            i["PTS_home"],
            i["FG_PCT_home"],
            i["FT_PCT_home"],
            i["HOME_TEAM_ID"],
            i["VISITOR_TEAM_ID"],
            i["SEASON"],
        )
        for i in dr
    ]

cur.executemany(
    "INSERT INTO games (gameID,gameDate, gameStatus,homeTeamPoints, percentageFG,  percentageFT, homeTeamID, visitorTeamID,season) VALUES (?,?, ?,?, ?,?, ?, ?, ?);",
    to_db,
)
con.commit()


with open("games_details.csv", "r", encoding="utf8") as fin:
    dr = csv.DictReader(fin)
    to_db = [
        (
            i["COMMENT"],
            i["MIN"],
            i["NICKNAME"],
            i["TEAM_CITY"],
            i["START_POSITION"],
            i["GAME_ID"],
        )
        for i in dr
    ]

cur.executemany(
    "INSERT INTO game_detail (comment, minute,nickName, city,  startingPosition, gameID) VALUES (?,?, ?,?, ?,?);",
    to_db,
)
con.commit()
con.close()
