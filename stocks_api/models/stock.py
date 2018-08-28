from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime
)

from .meta import Base

# Define each attribute of your class with the appropriate data type and any further restrictions or definitions that each attribute should carry with it into the database table.
# Define three class methods on your Stock class:
# one(): Retrieve a single instance from the database by the primary key for that record
# new(): Create a single new instance of the Stock class
# destroy(): Remove a single instance from the database by the primary key for that record


class Stock(Base):
    __tablename__ = 'stocks'
    # The following attributes are being defined to mirror the data that will be retrieved from the 3rd party API
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    exchange = Column(Text)
    industry = Column(Text)
    website = Column(Text)
    description = Column(Text)
    CEO = Column(Text)
    issueType = Column(Text)
    sector = Column(Text)
    date_created = Column(DateTime)
    date_updated = Column(DateTime)

Index('my_index', Stock.name, unique=True, mysql_length=255)
