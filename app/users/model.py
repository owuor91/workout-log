from sqlalchemy import (
    Column,
    String,
    Enum,
    Date,
    Float,
    Integer,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
import uuid

from sqlalchemy.ext.declarative import declarative_base

from app.base.enums import SexEnum

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone_number = Column(String(50), nullable=False, unique=True)
    password = Column(String(256), nullable=False)


class Profile(Base):
    __tablename__ = "profile"
    profile_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("user.user_id"), nullable=False
    )
    sex = Column(Enum(SexEnum), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Integer, nullable=False)
