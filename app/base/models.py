import datetime
import logging

from sqlalchemy import Column, DateTime, String, Boolean
from sqlalchemy.dialects.postgresql import JSON
from db import db

from app.base.exceptions import DatabaseError


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
    """Commit record to db."""
    session = db.session
    try:
        session.add(self)
        session.commit()
    except Exception as exc:
        session.rollback()
        logging.exception(exc)
        raise DatabaseError(
            f"Problem saving {self.__class__.__name__} record in database"
        )

    return self


def get(self, pk):
    """
    Get a single record given a pk
    """
    session = db.session
    return session.query(self).get(pk)
