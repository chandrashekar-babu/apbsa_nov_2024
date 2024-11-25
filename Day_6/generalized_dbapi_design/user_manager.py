
class User:
    def __init__(self, driver_config):
        #import driver_config  # TODO: Try and make this code dynamic by accepting config_module as a string
        self.config = driver_config
        
    def connect(self):
        self.conn = self.config.driver.connect(**self.config.DSN)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, et, ev, tb):
        if et is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.close()
        

    def add(self, *args):
        self.cursor.execute(self.driver.INSERT_USER, args)

    def fetch(self, name):
        self.cursor.execute(self.driver.SELECT_ONE_USER, (name,))
        return self.cursor
    
    def delete(self, name):
        self.cursor.execute(self.driver.DELETE_USER, (name,))

    # TODO: Implement support for create_schema(), replace(), update(), fetch_all()
    
    