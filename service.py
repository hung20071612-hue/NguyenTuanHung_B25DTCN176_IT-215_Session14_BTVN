from models import GamestoreModel
from schemas import *

from sqlalchemy.orm import Session

def s_run_api():
    return {
        "message": "API đang chạy"
    }

def s_display_game(db: Session):
    return db.query(GamestoreModel).all()

def s_display_game_detail(game_id,db: Session):
    game = db.query(GamestoreModel).filter(GamestoreModel.id == game_id).first()
    if game is None:
        return 1
    return game

def s_add_game(game: GameCreate,db: Session):
    new_game = GamestoreModel(
        game_name = game.game_name,
        developer = game.developer,
        genre = game.genre,
        price = game.price,
        release_year = game.release_year
    )

    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return new_game

def s_update_game(gameupdate: GameUpdate,game_id,db: Session):
    game = db.query(GamestoreModel).filter(GamestoreModel.id == game_id).first()
    if game is None:
        return 1
    game.game_name = gameupdate.game_name
    game.developer = gameupdate.developer
    game.genre = gameupdate.genre
    game.price = gameupdate.price
    game.release_year = gameupdate.release_year

    db.commit()
    db.refresh(game)
    return game

def s_delete_game(game_id,db: Session):
    game = db.query(GamestoreModel).filter(GamestoreModel.id == game_id).first()
    if game is None:
        return 1
    
    db.delete(game)
    db.commit()

    return game