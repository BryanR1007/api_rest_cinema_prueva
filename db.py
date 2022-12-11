from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, Text,  create_engine, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    
    id_movie = Column(Integer, primary_key = True)
    title = Column(String, nullable = False)
    url = Column(Text, nullable = False)
    clasification = Column(Text, nullable = False)
    funcionts = relationship('Function', back_populates = 'movie')


class Function(Base):
    __tablename__ = 'functions'

    id_function = Column(Integer, primary_key = True)
    date = Column(String, nullable = False)
    movie_id = Column(Integer, ForeignKey('movies.id_movie'))
    movie = relationship('Movie', back_populates = 'functions')


#class Useres(Base):
#    __tablename__ = 'users'
#
#    id_user = Column(Integer, primary_key = True)
#    name = Column(String, nullable = False)
#    lastname = Column(String, nullable = False)
#    password = Column(String, nullable = False)
#    email = Column(String, nullable = False)
#    phone = Column(Integer, nullable = False)

class Ticket(Base):
    __tablename__ = 'tickets'

    id_ticket = Column(Integer, primary_key = True)



engine = create_engine('postgresql://postgres:ab1007@localhost/DB_api_rest_cinema')
Base.metadata.create_all
Session = sessionmaker(bind=engine)
session = Session() 
