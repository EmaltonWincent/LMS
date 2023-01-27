import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS books(
            id Integer Primary Key,
            name text,
            isbn text,
            author text,
            publication text,
            status text
            
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, isbn, author, publication, status):
        self.cur.execute("insert into books values (NULL,?,?,?,?,?)",
                         (name, isbn, author, publication, status))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from books")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from books where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, isbn, author, publication, status):
        self.cur.execute(
            "update books set name=?, isbn=?, author=?, publication=?, status=? where id=?",
            (name, isbn, author, publication,status,id))
        self.con.commit()