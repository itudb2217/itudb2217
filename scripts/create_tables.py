import sqlite3 as dbapi2

INIT_STATEMENTS = [
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teamName TEXT NOT NULL,
        abbreviation TEXT NOT NULL,
        playOff BOOL NOT NULL,
        numOfGames INTEGER NOT NULL,
        matchPoints INTEGER NOT NULL,
        fieldGoals INTEGER NOT NULL,
        percentageFG FLOAT NOT NULL,
        seasonID INTEGER NOT NULL,
        FOREIGN KEY (seasonID) REFERENCES ENDOFSEASONS(id) ON DELETE CASCADE ON UPDATE CASCADE

    )
    """,
    """
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        playerName TEXT NOT NULL,
        position TEXT NOT NULL,
        age INTEGER NOT NULL,
        leauge TEXT NOT NULL,
        experince TEXT NOT NULL,
        teamID INTEGER NOT NULL,
        seasonID INTEGER NOT NULL,
        FOREIGN KEY (teamID) REFERENCES TEAMS(id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (seasonID) REFERENCES ENDOFSEASONS(id) ON DELETE CASCADE ON UPDATE CASCADE

    )
    """,
    """
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gameDate TEXT NOT NULL,
        gameStatus TEXT NOT NULL,
        homeTeamPoints INTEGER NOT NULL,
        percentageFG INTEGER NOT NULL,
        percentageFT INTEGER NOT NULL,
        homeTeamID INTEGER NOT NULL,
        visitorTeamID INTEGER NOT NULL,
        gameID INTEGER NOT NULL,
        FOREIGN KEY (gameID) REFERENCES GAMES(id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (homeTeamID) REFERENCES TEAMS(id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (visitorTeamID) REFERENCES TEAMS(id) ON DELETE CASCADE ON UPDATE CASCADE

    )
    """,
    """
    CREATE TABLE IF NOT EXISTS stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        teamName TEXT NOT NULL,
        loss BOOL NOT NULL,
        win BOOL NOT NULL,
        age INTEGER NOT NULL,
        winPercentage INTEGER NOT NULL,
        lossPercentage INTEGER NOT NULL,
        abbreviation INTEGER NOT NULL,
        seasonID INTEGER NOT NULL,
        FOREIGN KEY (seasonID) REFERENCES ENDOFSEASONS(id) ON DELETE CASCADE ON UPDATE CASCADE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS game_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comment TEXT NOT NULL,
        minute INTEGER NOT NULL,
        nickName TEXT NOT NULL,
        city TEXT NOT NULL,
        startingPosition TEXT NOT NULL,
        gameID INTEGER NOT NULL,
        FOREIGN KEY (gameID) REFERENCES GAMES(id) ON DELETE CASCADE ON UPDATE CASCADE   
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS endofseasons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        teamNo TEXT NOT NULL,
        position TEXT NOT NULL,
        league INTEGER NOT NULL,
        birth TEXT NOT NULL,
        season INTEGER NOT NULL,
        playerID INTEGER NOT NULL,
        teamID TEXT NOT NULL,
        FOREIGN KEY (playerID) REFERENCES PLAYERS(id) ON DELETE CASCADE ON UPDATE CASCADE,
        FOREIGN KEY (teamID) REFERENCES TEAMS(abbreviation) ON DELETE CASCADE ON UPDATE CASCADE
    )
    """,
]
# enofseason içinde non key olan season ve birth revize edilebilir ekstradan


def create_tables():
    with dbapi2.connect("testing.db") as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            print(statement)
            cursor.execute(statement)
        connection.commit()


create_tables()
