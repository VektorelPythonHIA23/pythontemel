import sqlite3 as sql
db = sql.connect("MEmin\chinook.db")
cur = db.cursor()
cur.execute(""" SELECT *
  FROM albums AS alb
       INNER JOIN
       artists AS art ON alb.title = art.Name;
""")
print(cur.fetchall())