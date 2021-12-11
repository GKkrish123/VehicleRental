from sqlalchemy.ext.declarative import declarative_base, declared_attr

class CustomBase(object):
    # GENERATE __tablename__ AUTOMATICALLY
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

base = declarative_base(cls=CustomBase)