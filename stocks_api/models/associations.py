from sqlalchemy import Table, Column, Integer, ForeignKey
from .meta import metadata

roles_association = Table(
    'roles_association',
    metadata,
    Column('account_id', Integer, ForeignKey('accounts.id')),
    Column('role_id', Integer, ForeignKey('account_roles.id')),
)

portfolios_stocks_association = Table(
    'portfolios_stocks_association',
    metadata,
    Column('stock_id', Integer, ForeignKey('stocks.id')),
)

# Equivalent to above
# from .meta import Base
# class RolesAssociation(Base):
#     __tablename__ = 'roles_association'
#     account_id = Column(Integer, ForeignKey('accounts.id'))
#     role_id = Column(Integer, ForeignKey('account_roles.id'))
