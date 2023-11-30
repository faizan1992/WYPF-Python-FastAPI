from fastapi import FastAPI,Request
from routes.user import user
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins =[
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins
)

app.include_router(user)
