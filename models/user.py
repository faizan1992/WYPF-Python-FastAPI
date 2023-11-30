from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import Base

class User(Base):
    __tablename__ = "users"
    id =  Column(Integer,primary_key=True)
    name = Column(String(100))
    email = Column(String(50))

