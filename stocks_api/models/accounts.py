# TODO
from .weather_location import weather_location
from .associations import roles_association
from sqlalchemy.orm import
# some stuff up here


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    # TODO
    locations = relationship(WeatherLocation, back_populates='accounts')
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')

    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password    # NOTE: THIS IS UNSAFE AND WILL BE FIXED

    @classmethod
    def new(cls, request, email=None, password=None):
        """Register a new user
        """
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)

        #   TODO: Assign roles to new user

        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request, email, password):
        """Validate that user exists and they are who they say they are
        """
        #   TODO: Complete this tomorrow as part of the login process
        pass
