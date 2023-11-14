from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import SQLALCHEMY_DATABASE


engine = create_engine(SQLALCHEMY_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
