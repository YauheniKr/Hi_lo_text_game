
import datetime
import sqlalchemy

from model.model_base import ModelBase
from model.player import Player

class Move(ModelBase):
    __tablename__ = 'moves'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    game_id = sqlalchemy.Column(sqlalchemy.String, index=True)
    count = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    player_id = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    number = sqlalchemy.Column(sqlalchemy.Integer)
    guess = sqlalchemy.Column(sqlalchemy.Integer)
    is_over = sqlalchemy.Column(sqlalchemy.BOOLEAN)

    def to_json(self, player):

        return {
            'id': self.id,
            'created': self.created.isoformat(),
            'player_id': self.player_id,
            'player': player.name,
            'roll_number': self.count,
            'move':self.guess,
            'number':self.number,
            'is_over': self.is_over,
        }