from datetime import datetime
import enum

from sqlalchemy import Enum, Column, ForeignKey, Integer,String, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

from ..db_setup import Base
from .user import User
from .mixins import Timestamp


class Gender(enum.Enum):
    male = 'male'
    female = 'female'
    other = 'other'
    not_given = 'not_given'


class Member(Timestamp, Base):
    __tablename__ = "members"

    id = Column(Integer,primary_key=True, index=True)
    salutation = Column (String(10),nullable=False)
    first_name = Column (String(50), nullable=False)
    middle_name = Column (String(50), nullable=False)
    last_name = Column (String(50), nullable=False)
    mobile_number = Column (String(50), nullable=False)
    physical_address = Column (String(50), nullable=False)
    gender = Column(Enum(Gender))
    national_id = Column (String(50), nullable=False)
    email = Column(EmailType, nullable=True)
    is_client = Column (Boolean, default=False)

    user_id = Column (Integer,ForeignKey("users.id"),nullable=False)
    created_by = relationship(User)

    