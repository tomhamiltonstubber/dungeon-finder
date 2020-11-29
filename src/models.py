from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True)

    hashed_password = Column(String)
    gamemaster = relationship('GameMaster', back_populates='user')
    games = relationship('GamePlayer', back_populates='player')


class GameMaster(Base):
    __tablename__ = 'gamemasters'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship(User, back_populates='gamemaster')
    created_games = relationship('Game', back_populates='creator')


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    description = Column(Text)
    start_date = Column(DateTime)
    creator_id = Column(Integer, ForeignKey('gamemasters.id'), nullable=False)

    creator = relationship('GameMaster', back_populates='created_games')
    players = relationship('GamePlayer', back_populates='game')


class GamePlayer(Base):
    __tablename__ = 'game_players'

    id = Column(Integer, primary_key=True, index=True)

    player_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    game_id = Column(Integer, ForeignKey('games.id'), nullable=False)

    player = relationship('User', back_populates='games')
    game = relationship('Game', back_populates='players')
