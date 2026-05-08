from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from services.user_service.database import Base, engine, SessionLocal
from services.user_service.models import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Service")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "User Service Running with SQLite"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/users")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User with this email already exists"
        )

    user = User(name=name, email=email)

    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        for user in users
    ]