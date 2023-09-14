from sqlalchemy.orm import Session
import schemas
from models import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_operacaos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Operacao).offset(skip).limit(limit).all()

def get_operacao(db: Session, id: int):
    return db.query(models.Operacao).filter(models.Operacao.id == id).first()


def get_glebas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Gleba).offset(skip).limit(limit).all()

def get_gleba(db: Session, id: int):
    return db.query(models.Gleba).filter(models.Gleba.id == id).first()

