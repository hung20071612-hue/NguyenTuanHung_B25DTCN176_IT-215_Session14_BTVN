from database import *
from models import *
from schemas import *
from service import *

from fastapi import FastAPI,status,HTTPException,Depends
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def run_api():
    return s_run_api()

@app.get("/games",response_model=list[GameResponse],status_code=status.HTTP_200_OK)
def display_game(db: Session = Depends(get_db)):
    return s_display_game(db)

@app.get("/games/{game_id}",response_model=GameResponse,status_code=status.HTTP_200_OK)
def display_game_detail(game_id: int,db: Session = Depends(get_db)):
    game = s_display_game_detail(game_id,db)
    if game == 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy game"
        )
    return game

@app.post("/games",response_model=GameResponse,status_code=status.HTTP_201_CREATED)
def add_game(game: GameCreate,db: Session = Depends(get_db)):
    return s_add_game(game,db)

@app.put("/games/{game_id}",response_model=GameResponse,status_code=status.HTTP_200_OK)
def update_game(gameupdate: GameUpdate,game_id: int,db: Session = Depends(get_db)):
    game = s_update_game(gameupdate,game_id,db)
    if game == 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy game"
        )
    return {
        "message": "Cập nhật thành công",
        "data": game
    }
    
@app.delete("/games/{game_id}",response_model=GameResponse,status_code=status.HTTP_200_OK)
def delete_game(game_id: int,db: Session = Depends(get_db)):
    game = s_delete_game(game_id,db)
    if game == 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Không tìm thấy game"
        )
    return {
        "message": "Cập nhật thành công",
        "data": game
    }