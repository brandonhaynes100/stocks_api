from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)

from .meta import Base


# Define each attribute of your class with the appropriate data type and any further restrictions or definitions that each attribute should carry with it into the database table.
# Define two class methods on your Portfolio class:
# one(): Retrieve a single instance from the database by the primary key for that record
# new(): Create a single new instance of the Portfolio class
class Portfolio(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    @classmethod
    def new(cls, request=None, **kwargs):
        if request.dbsession is None:
            raise DBAPIError

        # portfolio = Portfolio({'name': 'some name')
        # Same as above
        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)

        return request.dbsession.query(cls).filter(
            cls.name == kwargs['name']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        if request.dbsession is None:
            raise DBAPIError


Index('my_index', Portfolio.name, unique=True, mysql_length=255)
