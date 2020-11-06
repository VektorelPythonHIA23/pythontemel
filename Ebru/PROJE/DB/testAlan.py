import sqlite3 as sql

db = sql.connect(r"Ibrahim\KOD\chinook.db")
cur = db.cursor()
#select

# sorgu = """
# SELECT * FROM artists 
# where ArtistId > 275
# """

# cur.execute(sorgu)
# # fetchone
# # print(cur.fetchone())
# # fetchmany
# print(cur.fetchmany(5))
# print(cur.fetchmany(5))
# while True:
    
#     aralik1 = input("Başlangıç giriniz:")
#     aralik2 = input("Bitiş Giriniz:")
#     if aralik1 != "-1":
#         sorgu = f"""
#         SELECT * FROM artists 
#         where ArtistId BETWEEN {aralik1} AND {aralik2}
#         """
#         cur.execute(sorgu)
#         print(cur.fetchall())
#     else:
#         break
aralik1 = input("Pattern giriniz:")
sorgu = f"""
SELECT * FROM artists 
where Name LIKE '{aralik1}';
"""
cur.execute(sorgu)
print(cur.fetchall())