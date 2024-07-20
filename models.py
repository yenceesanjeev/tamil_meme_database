from sqlalchemy import create_engine, Integer, String, Column, Enum
from sqlalchemy.orm import sessionmaker # what is session maker
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True) #Got the integer is not defined error. Then imported it
    name = Column(String)
    profile_pic = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}')"
    
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    language = Column(String)

class Template(Base):
    __tablename__ = 'templates'

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer)
    actor_id = Column(Integer)
    emotion_id = Column(Integer)
    popularity = Column(Enum('1', '2', '3', '4', '5'))
    dialogue = Column(String)
    category_id = Column(Integer)
    user_uploaded_id = Column(Integer)
    description = Column(String)
    image = Column(String)

# I understand this but not a lot
engine = create_engine("sqlite:///./mydatabase.db", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Commit the changes to the database
session.commit()

# Close the session
session.close()

# Reading the data
Session = sessionmaker(bind=engine)
session = Session()

# Query all users
users = session.query(User).all()

# Print the users
for user in users:
    print(f"Name: {user.name}, Email: {user.email}, Profile Pic: {user.profile_pic}")

# Close the session
session.close()
