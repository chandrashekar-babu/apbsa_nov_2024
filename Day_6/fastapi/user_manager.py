from fastapi import FastAPI
#from userdb import UserDB, SQLiteConfig, sqlite3, User, UserOpt
#users = UserDB(driver=sqlite3, config=SQLiteConfig)

from userdb_mongo import UserDB, MongoConfig, User, UserOpt
users = UserDB(config=MongoConfig)

# Better suggestion
# from userdb import UserDB
# from sqlite_config import SQLiteConfig
# from mongo_config import MongoConfig

# user = UserDB(config=SQLiteConfig)
# users = UserDB(config=MongoConfig)

users.connect()

# ASGI / WSGI compliant object
app = FastAPI()


@app.get("/users")
async def get_users():
    return users.get()

@app.post("/users")
async def add_user(user: User):
    users.add(user)

@app.get("/users/{name}")
async def get_user(name):
    r = users.get(name)
    print(r)
    return r

@app.delete("/users/{name}")
async def delete_user(name):
    users.delete(name)

@app.patch("/users/{name}")
async def update_user(name: str, user: UserOpt):
    users.update(name, user)

@app.put("/users/{name}")
async def replace_user(name: str, user: User):
    users.replace(name, user)