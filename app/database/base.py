from sqlalchemy.ext.declarative import declarative_base, declared_attr
from .queries import add_table_query, fetch_table_query, edit_table_query


class CustomBase(object):
    # GENERATE __tablename__ AUTOMATICALLY
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    # DECLARE COMMON MODEL METHODS
    def get(cls, primeid):
        try:
            return fetch_table_query(cls.__class__, getbyprimeid=primeid)
        except Exception:
            raise

    def fetch(cls, filters=[]):
        try:
            return fetch_table_query([cls.__class__], filters=filters)
        except Exception:
            raise

    def add(cls, tablevalues, session_close=True):
        try:
            return add_table_query(cls.__class__, tablevalues, session_close=session_close)
        except Exception:
            raise

    def edit(cls, filters, tablevalues, session_close=True):
        try:
            return edit_table_query(
                cls.__class__, filters, tablevalues, session_close=session_close
            )
        except Exception:
            raise


base = declarative_base(cls=CustomBase)
