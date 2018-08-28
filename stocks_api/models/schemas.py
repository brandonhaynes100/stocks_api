
# In your models/ directory, create a file called schemas.py for your model serializers.

# You will define two Marshmallow schemas in this file, one for PortfolioSchema and one for StockSchema.
# Each of these will simply define the model they require for serialization (we’ll further define these later in the course…)
# In your views/portfolio.py file, you will further define the following View Class Controllers:
# PortfolioAPIView - Controller interactions with your Portfolio model/schema
# StockAPIView - Controller interactions with your Stock model/schema
# CompanyAPIView - 3rd-party API interactions for requesting company data for your portfolio
# You will be using the requests library and a free API from IEX TRADING, which does not require the use of an API key at this point.
# We are specifically interested in the Company Info and the Time Series info, both of which are accessible via an API call using a companies Stock Symbol.
# Using your model class methods, formulate an appropriate serialized response for each available endpoint / method that we configured in our last lab for this application. You may want to refer back to the LAB.md specification for each of those endpoints to review the functionality required.
#
# Redeploy your application, and verify that you are able to make requests to your site from an HTTP client like Postman or HTTPie.

from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
# TODO
from . import WeatherLocation, Account, AccountRole


class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account


# TODO
class WeatherLocationSchema(ModelSchema):
    # This is really just an example of multiple fields being defined on this schema
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    account = fields.Nested(AccountSchema, exclude=(
        'password', 'locations', 'roles', 'date_created', 'date_updated',
    ))


    class Meta:
        model = WeatherLocation
