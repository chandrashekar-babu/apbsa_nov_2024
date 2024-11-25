from . import sqlite as userdb
#import userdb_mariadb as userdb
#import userdb_postgres as userdb

data = [
 ('guido', 'guido123', 'IT', 'Developer'),
 ('emily', 'em345', 'IT', 'Developer'),
 ('david', 'dave234', 'IT', 'Support')
]


if __name__ == '__main__':
    conn = userdb.driver.connect(**userdb.CONNECTION)
    cursor = conn.cursor()

    cursor.execute(userdb.CREATE_TABLE_SQL)

    cursor.executemany(userdb.INSERT_SQL, data)

    cursor.execute(userdb.SELECT_ALL_SQL)
    for row in cursor:
        print(row)

    conn.commit()
    conn.close()

