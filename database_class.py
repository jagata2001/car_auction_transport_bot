import sqlite3 as sql

class Database:
    def __init__(self,db_name):
        self.conn = sql.connect(db_name)
        cnx = self.conn.cursor()
        cnx.execute("""CREATE TABLE IF NOT EXISTS data (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                order_id INTEGER
               )""")
        cnx.close()
        self.conn.commit()

    def insert(self,order_ids = []):
        cnx = self.conn.cursor()
        cnx.execute("INSERT INTO data (order_id) VALUES (?)",(order_ids,))
        self.conn.commit()
        cnx.close()

    def check_order_id(self,order_id):
        cnx = self.conn.cursor()
        cnx.execute("SELECT COUNT(*) FROM data where order_id='%s'" % order_id)
        return cnx.fetchone()[0]
        cnx.close()
