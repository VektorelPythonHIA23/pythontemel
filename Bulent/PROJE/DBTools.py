import sqlite3 as sql

class DBTool:
    def __init__(self,adres):
        self.db = sql.connect(adres)
        self.cur = self.db.cursor()

    def select(self,sorgu):
        self.cur.execute(sorgu)
        return self.cur.fetchall()


    def idu(self,sorgu):
        try:
            self.cur.execute(sorgu)
            self.db.commit()
            return 1
        except:
            self.db.rollback()
            return -1
        


    def __del__(self):
        self.cur.close()
        self.db.close()