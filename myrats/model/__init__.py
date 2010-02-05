"""The application's model objects"""
import sqlalchemy as db
from sqlalchemy import orm

from myrats.model import meta

import datetime
from sqlalchemy import schema, types


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    
    # We are using SQLAlchemy 0.5 so transactional=True is replaced by
    # autocommit=False
    sm = orm.sessionmaker(autoflush=True, autocommit=False, bind=engine)
    
    meta.Session.configure(bind=engine)
    meta.engine = engine

def now():
    return datetime.datetime.now()

ticket_t = db.Table("Ticket", meta.metadata,
    db.Column("id", types.Integer, primary_key=True),
    db.Column("created_at", types.DateTime(), default=now),
    db.Column("description", types.Text, nullable=False),
    )

class Ticket(object):
    pass
	
orm.mapper(Ticket, ticket_t)

## Non-reflected tables may be defined and mapped at module level
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)


## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
