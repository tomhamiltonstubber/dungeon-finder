from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class GameBase(BaseModel):
    name: str
    description: str
    start_date: datetime
    creator_id: int


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int
    players: list = []

    class Config:
        orm_mode = True


class GameMasterBase(BaseModel):
    user_id: int
    created_games: List[Game]


class GameMasterCreate(GameMasterBase):
    pass


class GameMaster(GameMasterBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    first_name: str
    last_name: str
    gamemaster: Optional[GameMaster]
    games: list = []

    class Config:
        orm_mode = True


class GamePlayer(BaseModel):
    user: User
    game: Game

    class Config:
        orm_mode = True
