import csv
from typing import Union
from models import *
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

def init_db():
    Base.metadata.create_all(engine)

def write_users_from_file():
    init_db()
    Session = sessionmaker(bind=engine)
    session = Session()

    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            user = User(
                name=row["name"],
                profile_pic=row["profile_pic"],
                email=row["email"]
            )
            session.add(user)
        session.commit()
    
    session.close()

def read_users_from_file():
    init_db()
    Session = sessionmaker(bind=engine)
    session = Session()

    users = session.query(User).all()

    session.close()
    return users

write_users_from_file()
print(read_users_from_file())

@app.get("/")
def read_root():
    return read_users_from_file()

#Sending the data over URL Params, how do I send as body?
@app.post("/add_user")
def add_user(name: str, email: str, profile_pic: Optional[str] = None):
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        new_user = User(name=name, email=email, profile_pic=profile_pic)
        session.add(new_user)
        session.commit()
        return {"message": "User added successfully", "user": new_user}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

'''
@app.get("/users")
def get_users():
    return get_user_list()
'''
