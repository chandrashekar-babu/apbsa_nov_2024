class User:
    def __init__(self, name, role, dept):
        self.name, self.role, self.dept = name, role, dept

    def __str__(self):
        return f"<User: name='{self.name}' role='{self.role}', dept='{self.dept}'>"

    def testfn(self):
        print("Invoked testfn on User(name='{self.name}')")
