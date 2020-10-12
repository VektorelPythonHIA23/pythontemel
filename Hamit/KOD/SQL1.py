import sqlite3 as sql
db = sql.connect("Hamit/KOD/chinook.db")
cur = db.cursor()
cur.execute("""
SELECT *
  FROM albums
 WHERE artistId IN (
           SELECT artistId
             FROM artists
            WHERE Name LIKE 'A__o%'
       )
AND 
       artistId > 200;

""")
print(cur.fetchall())
