from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:525643916096@localhost:5432/hotel'

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_size=20, max_overflow=10)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()


def get_db():
    session = SessionLocal()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()


from database.hotelservice import *
from database.guestservice import *
from database.cardservice import *
from database.booked_room__status_service import *
