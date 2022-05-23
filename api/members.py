from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schemas.member import Member, MemberCreate
from api.utils.members import get_member, get_members, create_member

router = fastapi.APIRouter(
    prefix='/members',
    tags=['Members']
)


@router.get("/", response_model=List[Member])
async def read_members(db: Session = Depends(get_db)):
    members = get_members(db=db)
    return members


@router.post("/", response_model=Member)
async def create_new_member(member: MemberCreate, db: Session = Depends(get_db)):
    return create_member(db=db, member=member)


@router.get("/{member_id}")
async def read_member(member_id: int, db: Session = Depends(get_db)):
    db_member = get_member(db=db, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_member


@router.patch("/{member_id}")
async def update_member():
    return {"members": []}


@router.delete("/{member_id}")
async def delete_member():
    return {"members": []}


@router.get("/{member_id}/sections")
async def read_member_sections():
    return {"members": []}