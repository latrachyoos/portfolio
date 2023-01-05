import sqlite3
conn = sqlite3.connect("tkcheck.sql", check_same_thread=False)
sql = "insert into users(user,type) values('latrachyoo','tk')"
rows = conn.execute(sql)
conn.commit()
sql="select * from users order by id desc"

rows = conn.execute(sql)

print(rows.fetchall())