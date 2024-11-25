from fastapi import FastAPI

api = FastAPI()

@api.get("/time")
def get_time():
    from time import ctime
    return {"time": ctime(), "host": "localhost"}

@api.get("/users")
async def get_users():
      # # users = await cur.execute(SELECT_QUERY)
      # return (u for u in users) 
      return ["john", "sam", "joe"]
    
@api.get("/users/{name}")
def get_user(name):
    return {"username": name.upper(), "role": "developer"}
