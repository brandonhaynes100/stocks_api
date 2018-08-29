# TODO
# example code
# from .weather_location import weather_location
from .associations import roles_association
from sqlalchemy.orm import relationship
from sqlalchemy.exc import DBAPIError
from datetime import datetime as dt
from cryptacular import bcrypt
from .role import AccountRole
from .meta import Base
from sqlalchemy import (
    Column,
    # Index,
    Integer,
    String,
    Text,
    DateTime,
)


manager = bcrypt.BCRYPTPasswordManager()


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    # TODO
    # example code
    # locations = relationship(WeatherLocation, back_populates='accounts')
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email=None, password=None):
        self.email = email
        # takes exponentially more time after 10
        self.password = manager.encode(password, 10)

    @classmethod
    def new(cls, request, email=None, password=None):
        """Register a new user
        """
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)

        # TODO: Assign roles to new user
        # This is unsafe, makes all users admin
        admin_role = request.dbsession.query(AccountRole).filter(
            AccountRole.name == 'admin').one_or_none()

        user.roles.append(admin_role)
        # if flush isn't called, admin_role won't save
        request.dbsession.flush()

        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def one(cls, request, email=None):
        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request, email, password):
        """Validate that user exists and they are who they say they are
        """
        if request.dbsession is None:
            raise DBAPIError

        try:
            account = request.dbsession.query(cls).filter(
                cls.email == email).one_or_none()
        except DBAPIError:
            return None

        if account is not None:
            if manager.check(account.password, password):
                return account

        return None
