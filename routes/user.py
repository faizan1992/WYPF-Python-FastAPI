from fastapi import APIRouter,Depends
from config.db import Base,engine,get_db
from models.index import User,Detail
from schemas.index import User_Schema,Detail_Schema
from sqlalchemy.orm import Session

user = APIRouter()

# This is for creating database
@user.get("/Create_Database")
async def create_data():
    Base.metadata.create_all(bind=engine)

# This is for fetching all data
@user.get("/All_User",response_model=list[User_Schema])
async def fetch_all_data(db:Session = Depends(get_db)):
    return db.query(User).all()

# This is for fetching all data
@user.get("/Single_User/{id}",response_model=User_Schema)
async def fetch_single_User(id:int,db:Session = Depends(get_db)):
    user= db.query(User).filter(User.id == id).first()
    return user


# This is for fetching all Post By user id
@user.get("/post/{post_id}",response_model=list[Detail_Schema])
async def fetch_post(post_id:int,db:Session = Depends(get_db)):
    post= db.query(Detail).filter(Detail.user_id == post_id).all()
    return post

# This is for inserting
@user.post("/Insert_Data",response_model=User_Schema)
async def insert_data(user:User_Schema,db:Session=Depends(get_db)):
    u = User(email = user.email,name = user.name,id = user.id)
    db.add(u)
    db.commit()
    return u
