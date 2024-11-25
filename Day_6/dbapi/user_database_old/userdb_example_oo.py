from userdb import UserFactory  

user_list = [
 ('guido', 'guido123', 'IT', 'Developer'),
 ('emily', 'em345', 'IT', 'Developer'),
 ('david', 'dave234', 'IT', 'Support')
]

SQLITE_DSN = "sqlite3://./users.sqlite"
MYSQL_DSN = "pythonista:w3lc0me@mariadb://localhost/testdb"
MONGO_DSN = "pymongo://localhost/testdb"
# DSN_FORM = "username:password@driver://host:port/database"
# username, password, host, port could be optional

if __name__ == '__main__':
    with UserFactory(SQLITE_DSN) as users:
        users.create_schema() # Invoke CREATE_TABLE_SQL
        users.add(user_list)

        for row in users:  # Invoked SELECT_ALL_SQL and yield rows
            print(row)

 
