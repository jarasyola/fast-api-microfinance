
from fastapi import FastAPI
from pydantic import BaseModel

from api import users,members
from db.db_setup import engine
from db.models import user,member

user.Base.metadata.create_all(bind=engine)
member.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API Microfinance",
    description="Microfinance system for managing members and clients (borrowers)",
    version="0.0.1",
    contact={
        "name": "Jarasyola",
        "email": "jarasyola@luso.solutions",
    },
    license_info={
        "name": "MIT",
       
    },
)

app.include_router(users.router)
app.include_router(members.router)
