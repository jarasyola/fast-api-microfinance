from typing import Optional

from pydantic import BaseModel


class MemberBase(BaseModel):
    first_name: str
    last_name: str
    mobile_number: str
    user_id: int
    


class MemberCreate(MemberBase):
    ...


class Member(MemberBase):
    id: int

    class Config:
        orm_mode = True