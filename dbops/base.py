import sqlite3 as dbapi2


class Base:
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.db_name = db_name
        self.conn = dbapi2.connect(self.db_name, check_same_thread=False)
        self.conn.row_factory = dbapi2.Row
        self.cursor = self.conn.cursor()

    def delete(self, id):
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE id=?", (id,))
        self.conn.commit()

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE id=?", (id,))
        return self.cursor.fetchone()

    def get_all(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        return self.cursor.fetchall()
