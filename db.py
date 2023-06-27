import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("mybooks.db")
        self.cur = self.conn.cursor()
        self.create_table()

    def __del__(self):
        self.conn.close()

    def create_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS buy (id INTEGER PRIMARY KEY, product TEXT, price TEXT, comment TEXT)"
        )
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM buy")
        return self.cur.fetchall()

    def insert(self, product, price, comment):
        self.cur.execute(
            "INSERT INTO buy VALUES (NULL,?,?,?)",
            (product, price, comment),
        )
        self.conn.commit()

    def update(self, id, product, price):
        self.cur.execute(
            "UPDATE buy SET product=?, price=? WHERE id=?",
            (product, price, id),
        )
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM buy WHERE id=?", (id,))
        self.conn.commit()

    def search(self, product=""):
        self.cur.execute("SELECT * FROM buy WHERE product=?", (product,))
        return self.cur.fetchall()
