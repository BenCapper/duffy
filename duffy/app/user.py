from fastapi import FastAPI
from database.model import User
import logging
 
 
log = logging.getLogger(__name__)
app = FastAPI()
 
 
@app.get("/user/", response_model= User)
async def get_user():
   return {}
 
@app.post("/user/")
async def create_user(user: User):
   return user
 
@app.put("/user/{id}/", response_model= User)
async def update_user(id: int, user: User):
   users[id] = user
 
@app.delete("/user/{id}/")
async def delete_user(id: int):
   return {}

