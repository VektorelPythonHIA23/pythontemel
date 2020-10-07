import sqlite3 as sql
db = sql.connect("MEmin\chinook.db")
cur = db.cursor()
cur.execute(""" SELECT COUNT(firstname), Country
FROM Customers
GROUP BY Country
HAVING COUNT(firstname) > 2;
""")
print(cur.fetchall())
