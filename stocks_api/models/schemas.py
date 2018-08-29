from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
# TODO
from accounts import Account
from role import AccountRole
from portfolio import Portfolio
from stock import Stock


class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account


class PortfolioSchema(ModelSchema):
    # This is really just an example of multiple fields being defined on this schema
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    account = fields.Nested(AccountSchema, exclude=(
        'password', 'portfolios', 'roles', 'date_created', 'date_updated'
    ))

    class Meta:
        model = Portfolio


class StockSchema(ModelSchema):
    class Meta:
        model = Stock
