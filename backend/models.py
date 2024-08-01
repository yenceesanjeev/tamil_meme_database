from sqlalchemy import create_engine, Integer, String, Column, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    profile_pic = Column(String)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"Movie(id={self.id}, name='{self.name}')"

class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    language = Column(String, nullable=False)

    def __repr__(self):
        return f"Actor(id={self.id}, name='{self.name}', language='{self.language}')"

class Template(Base):
    __tablename__ = 'templates'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    actor_id = Column(Integer, ForeignKey('actors.id'), nullable=False)
    emotion_id = Column(Integer, nullable=False)
    popularity = Column(Enum('1', '2', '3', '4', '5', name='popularity'), nullable=False)
    dialogue = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    user_uploaded_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    description = Column(String)
    image = Column(String)

    movie = relationship("Movie")
    actor = relationship("Actor")
    category = relationship("Category")
    user = relationship("User")

    def __repr__(self):
        return f"Template(id={self.id}, movie_id={self.movie_id}, actor_id={self.actor_id})"

# Database setup
engine = create_engine(os.environ["POSTGRES_URL"], echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()