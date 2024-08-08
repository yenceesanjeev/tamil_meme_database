import csv
from typing import Union
from models import *
from typing import Optional
from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://tamil-meme-database.vercel.app"],  # Replace with your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def init_db():
    Base.metadata.create_all(engine)

def read_users_from_file():
    init_db()
    Session = sessionmaker(bind=engine)
    session = Session()

    users = session.query(User).all()

    session.close()
    return users

print(read_users_from_file())

@app.get("/")
def read_root():
    return {"Hello":"World"}

class UserCreate(BaseModel):
    name: str
    email: str
    profile_pic: Optional[str] = None

@app.post("/add_user")
def add_user(user: UserCreate):
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        new_user = User(**user.dict())
        session.add(new_user)
        session.commit()
        return {"message": "User added successfully", "user": new_user}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

@app.get("/users")
def get_users():
    return read_users_from_file()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return read_users_from_file()[user_id-1]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return {"message": "User deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

@app.get("/memes")
def get_memes():
    Session = sessionmaker(bind=engine)
    session = Session()

    memes = session.query(TempMeme).all()
    memes = [meme.image_url for meme in memes]

    return memes

    session.close()

class MemeCreate(BaseModel):
    image_url: str
    meme_name: str | None = None

class MemeResponse(BaseModel):
    id: int
    image_url: str
    meme_name: str | None

    model_config = ConfigDict(from_attributes=True)

@app.post("/add-memes")
def add_meme(meme: MemeCreate):
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        new_meme = TempMeme(image_url=meme.image_url, meme_name=meme.meme_name)
        session.add(new_meme)
        session.commit()
        session.refresh(new_meme)
        return MemeResponse.from_orm(new_meme)
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