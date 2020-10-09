import sqlite3 as sql
db = sql.connect("Hamit/chinook.db")
cur = db.cursor()
cur.execute("""
SELECT *
  FROM ALBUMS
 WHERE artistId IN (
           SELECT artistId
             FROM artists
            WHERE Name LIKE 'A__o%'
       )
AND 
       artistID > 200;
""")
print(cur.fetchall())
