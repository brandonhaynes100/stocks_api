from .stock import Stock
from datetime import datetime as dt
from sqlalchemy.orm import relationship
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)

from .meta import Base


class Portfolio(Base):
    __tablename__ = 'portfolios'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    accounts = relationship('Account', back_populates='portfolios')

    stocks = relationship('Stock', back_populates='portfolios')

    @classmethod
    def new(cls, request=None, **kwargs):
        """ new(): Create a single new instance of the Portfolio class
        """
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
        """ one(): Retrieve a single instance from the database by the primary key for that record
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).get(pk)


# Index('my_index', Portfolio.name, unique=True, mysql_length=255)
