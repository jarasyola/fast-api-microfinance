from typing import List

import fastapi
from fastapi import Depends, HTTPException,status
from sqlalchemy.orm import Session

from db.db_setup import get_db
from pydantic_schemas.member import Member, MemberCreate
from api.utils.members import get_member, get_members, create_member, destroy_member_by_id,update_member_by_id

router = fastapi.APIRouter(
    prefix='/v1/members',
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
        raise HTTPException(status_code=404, detail=f"Member with id {member_id} is not found")
    return db_member


@router.delete("/{member_id}")
async def Delete_Member_by_id(member_id: int, db: Session = Depends(get_db)):
    message= destroy_member_by_id(db=db, member_id=member_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Member with id {member_id} does not exist")
    return {"Detail": "Successfully deleted the member"}



@router.put("/{member_id}")
def update_member(member_id:int, member:MemberCreate,db:Session=Depends(get_db)):
    user_id = 1
    message = update_member_by_id(member_id=member_id, member=member, db=db,user_id=user_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Member with id {member_id} does not exist")
    return {"detail":"Successfully updated member data."}

