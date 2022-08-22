import datetime

from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base
from app.db import db

class BaseModel:

    __abstract__ = True

    date_created = Column(
        DateTime(timezone=True), nullable=False, default=datetime.datetime.now
    )
    date_updated = Column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )
    created_by = Column(String(100), nullable=False)
    updated_by = Column(String(100), nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    meta = Column(JSON, nullable=True, default=dict, server_default="{}")

    def save(self):
        db.session.add(self)
        db.session.commit()

Base = declarative_base(cls=BaseModel)