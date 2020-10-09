from os import PRIO_PGRP
import sqlite3 as sql

db = sql.connect("Hamit/KOD/chinook.db")
cur = db.cursor()
#select
#275 ten sonrasini istersem none oluyor 
#sorgu = """
#SELECT * FROM artists WHERE ArtistId > 260 
#"""
#cur.execute(sorgu)
#fetchone
#print(cur.fetchone())
#print(cur.fetchone())
#print(cur.fetchmany(3))
#print(cur.fetchall())
#while True:
#    aralik1 = input("Baslangic giriniz:")
#    aralik2 = input("Bitis giriniz:")
#    if aralik1 != "-1":
#        sorgu = f"""
#        SELECT * FROM artists 
#        WHERE ArtistId BETWEEN {aralik1} AND {aralik2} 
#        """
#        cur.execute(sorgu)
#        print(cur.fetchall())
#    else:
#        break


aralik1 = input("Pattern giriniz:")
sorgu = f"""
SELECT * FROM artists 
WHERE Name LIKE '{aralik1}'
"""
cur.execute(sorgu)
print(cur.fetchall())