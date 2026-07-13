from pydantic import BaseModel,Field

class GameResponse(BaseModel):
    id: int
    game_name: str
    developer: str
    genre: str
    price: float
    release_year: int

class GameCreate(BaseModel):
    game_name: str = Field(...)
    developer: str = Field(...)
    genre: str = Field(...)
    price: float = Field(...,ge=0)
    release_year: int = Field(...,ge=2000)

class GameUpdate(BaseModel):
    game_name: str = Field(...)
    developer: str = Field(...)
    genre: str = Field(...)
    price: float = Field(...,ge=0)
    release_year: int = Field(...,ge=2000)