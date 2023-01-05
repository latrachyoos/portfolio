import sqlite3

conn = sqlite3.connect("bot_resender.db", check_same_thread=False)
"""
conn.execute("create table msg("
             "id_admin varchar(20) PRIMARY KEY,"
             "tag varchar(20) PRIMARY KEY,"
             "send bit"
             
             ")")"""

rows = conn.execute("select * from users").fetchall()
for row in rows:
    str = f"codice: {row[0]} - tag: {row[1]}"
    print(row)



