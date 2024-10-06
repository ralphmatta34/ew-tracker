import sqlite3

class Database:
    def __init__(self, url):
        with sqlite3.connect(url) as db:
            cursor = db.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS ew (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                subject TEXT NOT NULL,
                beak TEXT NOT NULL,
                due_date DATE NOT NULL
            );
            """
            cursor.execute(sql)

            sql_insert = """
            INSERT INTO ew (task, subject, beak, due_date) VALUES (?, ?, ?, ?);
            """
            cursor.execute(sql_insert, ("EW1", "Subject1", "ABC", "2024-10-09"))
            db.commit()


    def get_ews(self):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            sql = """
            SELECT * FROM ew;
            """
            cursor.execute(sql)
            ews = cursor.fetchall()
            return ews


    def create_ew(self, task, subject, beak, due_date):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            sql_insert = """
            INSERT INTO ew (task, subject, beak, due_date) VALUES (?, ?, ?, ?);
            """
            cursor.execute(sql_insert, (task, subject, beak, due_date))
            db.commit()


    # EXTRA CREDIT
    def get_ew(self, id):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            sql = """
            SELECT * FROM ew WHERE id = "{0}";
            """.format(id)
            cursor.execute(sql)
            ew = cursor.fetchone() # used ChatGPT for .fetchone() instead of .fetchall()
            return ew
        
    
    def delete_ew(self, id):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            sql = """
            DELETE FROM ew WHERE id = "{0}";
            """.format(id)
            cursor.execute(sql)
            db.commit()
