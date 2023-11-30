from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,String,Text
from config.db import Base

class Detail(Base):
    __tablename__ = "posts"
    id =  Column(Integer,primary_key=True)
    title = Column(String(255))
    body = Column(Text)
    user_id = Column(Integer)

