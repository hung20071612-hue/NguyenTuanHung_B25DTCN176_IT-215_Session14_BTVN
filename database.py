from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

db_url = "mysql+pymysql://root:1234567@Localhost/game_store_db"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()