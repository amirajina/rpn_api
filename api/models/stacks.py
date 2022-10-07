from api.models import BaseModel
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType

from sqlalchemy import Column, String, \
    Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Stack(BaseModel):

    __tablename__ = 'stack'
    id = Column(
        UUID(
            as_uuid=True),
        nullable=False,
        unique=True,
        primary_key=True,
        default=uuid.uuid4)
    stack = Column(MutableList.as_mutable(PickleType),
                                  default=[])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def add_data(**kwargs):
        data = Stack(**kwargs)
        data.add_row()
        return data

    def as_dict(self):
        return {"id": self.id,
                "stack": self.stack
                }
