
import re
DSN_REGEX = """
   (                          # Extract `username` and `password` 
     (?P<username>.+?):       # from `username:password@`
     (?P<password>.+?)@
   )?                         # which is optional
    
   (?P<driver>\w+)://         # Extract `driver` from `driver://`
   (                          # Extract hostname:port  
     (?P<host>.+?)
     (:(?P<port>\d+))?        # where `:port` could be optional 
   )?                         # host:port itself could be optional
   /(?P<database>.+)          # Extract database
"""

DSN_PATTERN = re.compile(DSN_REGEX, re.VERBOSE)

class UserDB:
    CREATE_TABLE_SQL = """
    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32) UNIQUE NOT NULL,
        password VARCHAR(32),
        dept VARCHAR(32),
        role VARCHAR(32)
    )
    """

    INSERT_SQL = """
    INSERT INTO users(name, password, dept, role) VALUES(?,?,?,?)
    """

    SELECT_ALL_SQL = """
    SELECT name, dept, role from users
    """

    SELECT_ONE_SQL = """
    SELECT name, dept, role FROM users WHERE name = ?
    """

    DELETE_SQL = """
    DELETE FROM users WHERE name = ?
    """

    def __init__(self, driver, **kwargs):
        from importlib import import_module
        driver_module = import_module(driver)
        driver_args = { k: v for k, v in kwargs.items() if v is not None }
        self.connection = driver_module.connect(**driver_args)

    def create_schema(self):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(self.CREATE_TABLE_SQL)
        except Exception as e:
            self.connection.rollback()
            raise e
        else:
            self.connection.commit()

    def add(self, user_list):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(self.INSERT_SQL, user_list)
        except Exception as e:
            self.connection.rollback()
            raise e
        else:
            self.connection.commit()

    def __iter__(self):
        self.cursor = self.connection.cursor()
        self.cursor.execute(self.SELECT_ALL_SQL)
        return self.cursor


class UserFactory:
    
    def __new__(cls, dsn):
        kwargs = DSN_PATTERN.match(dsn).groupdict()      
        driver_module_name = "userdb_" + kwargs["driver"]
        from importlib import import_module
        driver = import_module(driver_module_name)
        return driver.UserDB(**kwargs)
        


        

