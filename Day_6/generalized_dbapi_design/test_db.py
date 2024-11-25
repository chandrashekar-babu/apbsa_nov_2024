from mariadb_config import *
#from sqlite3_config import *


data = [
    ("john", "john123", "John Doe"),
    ("guido", "gvr123", "Guido Van Rossum"),
    ("tim", "pete456", "Tim Peters")
]

with driver.connect(**DSN) as conn:
    cur = conn.cursor()
    cur.execute(CREATE_USER_TABLE)
    cur.executemany(INSERT_USER, data)

    cur.execute(SELECT_ALL_USER)
    for row in cur:
        print(row)