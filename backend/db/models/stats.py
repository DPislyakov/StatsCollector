from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Date

from db.base_class import Base


class Stats(Base):
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    views = Column(Integer, nullable=True)
    clicks = Column(Integer, nullable=True)
    cost = Column(Float, nullable=True)
