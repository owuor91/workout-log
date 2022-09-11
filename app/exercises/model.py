import uuid

from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.users.model import Base


class ExerciseCategory(Base):
    __tablename__ = "exercise_category"
    category_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    category_name = Column(String(50), nullable=False)
    exercises = relationship("Exercise", backref="exercise_category")


class Exercise(Base):
    __tablename__ = "exercise"
    exercise_id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    exercise_name = Column(String(100), nullable=False, unique=True)
    image = Column(String(256), nullable=True)
    category_id = Column(
        UUID(as_uuid=True),
        ForeignKey("exercise_category.category_id"),
        nullable=False,
    )
    description = Column(Text, nullable=True)
