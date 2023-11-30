from pydantic import BaseModel

class User_Schema(BaseModel):
    id:int
    name:str
    email:str
    
    class Config:
        orm_mode = True