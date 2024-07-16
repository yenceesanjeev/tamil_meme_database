import csv
from typing import Union
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker # what is session maker

from fastapi import FastAPI

#Why am I importing everything? 
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True) #Got the integer is not defined error. 
    name = Column(String)
    profile_pic = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}')"

# I understand this but not a lot
engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('users.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Create a User object from the CSV row
        user = User(
            name=row['name'],
            profile_pic=row['profile_pic'],
            email=row['email']
        )

        # Add the user to the session
        session.add(user)

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


app = FastAPI()


@app.post("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}