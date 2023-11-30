from pydantic import BaseModel

class Detail_Schema(BaseModel):
    id:int
    title:str
    body:str
    user_id:int
    
    class Config:
        orm_mode = True