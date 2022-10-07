from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime
import datetime


def load():
    from models import BaseModel  # noqa
    from models.stacks import Stack  # noqa


db = SQLAlchemy()


class BaseModel(db.Model):

    __abstract__ = True

    create_date = Column(
        DateTime(
            timezone=True),
        default=datetime.datetime.now)
    update_date = Column(
        DateTime(True),
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now)
    _session = None

    @classmethod
    def create_session(cls, session):
        cls._session = session

    @classmethod
    def get_session(cls):
        return cls._session

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def get_single(cls, filters={}):
        try:
            result = cls._session.query(cls).filter_by(**filters).first()
        except BaseException:
            cls._session.rollback()
            return None
        return result

    @classmethod
    def get_all(cls, filters={}):
        try:
            result = cls._session.query(cls).filter_by(**filters).all()
        except BaseException:
            cls._session.rollback()
            return None
        return result

    def add_row(self):
        try:
            self._session.add(self)
            self._session.commit()
        except BaseException:
            self._session.rollback()
            raise

    def delete_row(self):
        try:
            self._session.delete(self)
            self.update()
        except BaseException:
            self._session.rollback()

    def update_row(self, data):
        try:
            for name, value in data.items():
                if hasattr(self, name) and value:
                    setattr(self, name, value)
            self.update()
        except BaseException:
            self._session.rollback()

    def update(self):
        try:
            self._session.commit()
        except BaseException:
            self._session.rollback()


def init_db_session(session):
    BaseModel.create_session(session)
