from .weather_location import weather_location
from


#some stuff up here
date_created = Column(DateTime, default=dt.now())
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