from sqlalchemy.orm import relationship
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime
)

from .meta import Base


class Stock(Base):
    __tablename__ = 'stocks'
    # The following attributes are being defined to mirror the data that will be retrieved from the 3rd party API
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    companyName = Column(Text)
    exchange = Column(Text)
    industry = Column(Text)
    website = Column(Text)
    description = Column(Text)
    CEO = Column(Text)
    issueType = Column(Text)
    sector = Column(Text)
    date_created = Column(DateTime)
    date_updated = Column(DateTime)

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

    @classmethod
    def destroy(cls, request=None, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).filter(
            cls.id == pk).delete()


Index('my_index', Stock.name, unique=True, mysql_length=255)
