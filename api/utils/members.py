from sqlalchemy.orm import Session

from db.models.member import Member
from pydantic_schemas.member import MemberCreate


def get_member(db: Session, member_id: int):
    return db.query(Member).filter(Member.id == member_id).first()


def get_members(db: Session):
    return db.query(Member).all()


def get_user_members(db: Session, user_id: int):
    members = db.query(Member).filter(Member.user_id == user_id).all()
    return members

def get_user_members(db: Session, user_id: int):
    members = db.query(Member).filter(Member.user_id == user_id).all()
    return members


def create_member(db: Session, member: MemberCreate):
    db_member = Member(
        first_name=member.first_name,
        last_name=member.last_name,
        mobile_number=member.mobile_number,
        user_id=member.user_id
    )
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member