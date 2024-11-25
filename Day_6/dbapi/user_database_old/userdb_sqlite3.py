import userdb

class UserDB(userdb.UserDB):
    CREATE_TABLE_SQL = """
    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(32) UNIQUE NOT NULL,
        password VARCHAR(32),
        dept VARCHAR(32),
        role VARCHAR(32)
    )
    """

    def __init__(self, **kwargs):
        import sqlite3
        self.connection = sqlite3.connect(kwargs["database"])
        
