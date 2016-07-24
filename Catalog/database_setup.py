from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

## db classes:
## Categories
## Items
## Item Descriptions

class User(Base):
  __tablename__  = 'user'

  name = Column(String(80), nullable = False)
  email = Column(String(100), nullable = False)
  picture = Column(String(250))
  id = Column(Integer, primary_key = True)

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id
       }


class Item(Base):
    __tablename__ = 'item'

    ## update column names as needed in serialize too
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    picture = Column(String(250))

    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'  : self.description,
           'picture'      : self.picture,
           'id'           : self.id,
           'category'     : self.category.name,
           'category_id'  : self.category_id
       }

engine = create_engine('postgres://catalog:c@t@log@localhost/catalog')
# engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.create_all(engine)
