
from typing import Optional,List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import users,members

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
