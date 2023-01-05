import sqlite3 as sl

con = sl.connect('tiktok-doggofresco.db')

def insert_into():
    sql = "insert into users(username,type) values (?,?)"

    data = [
        ("latrachyoo", "tk")

    ]

    con.executemany(sql, data)
    con.commit()


row = con.execute("select * from users")

for rw in row:
    print(rw)