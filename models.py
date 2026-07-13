from database import Base
from sqlalchemy import Column,Integer,String,Float

class GamestoreModel(Base):
    __tablename__="games"
    id = Column(Integer,primary_key=True,autoincrement=True)
    game_name = Column(String(100),nullable=False)
    developer = Column(String(100),nullable=False)
    genre = Column(String(100),nullable=False)
    price = Column(Float(12,2),nullable=False)
    release_year = Column(Integer,nullable=False)
