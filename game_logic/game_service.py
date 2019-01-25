from collections import defaultdict
from typing import List, Optional

from global_init import create_session
import random
# noinspection PyPackageRequirements
#from game_logic.game_decider import Decision
from web.views import game_api
from model.move import Move
from model.player import Player


def find_player(name: str) -> Player:
    session = create_session()

    player = session.query(Player).filter(Player.name == name).first()
    session.close()

    return player


def create_player(name: str) -> Player:
    session = create_session()

    player = session.query(Player).filter(Player.name == name).first()
    if player:
        raise Exception("Player already exists")

    player = Player()
    player.name = name
    session.add(player)
    session.commit()
    session.close()

    player = session.query(Player).filter(Player.name == name).first()
    return player


def is_game_over(game_id: str) -> bool:
    history = get_game_history(game_id)
    return any([h.is_over for h in history])


def all_players() -> List[Player]:
    session = create_session()

    players = list(session.query(Player).all())
    session.close()
    return players


def find_player_by_id(player_id: int) -> Player:
    session = create_session()
    player = session.query(Player).filter(Player.id == player_id).first()
    session.close()

    return player


def get_win_count(player: Player) -> int:
    session = create_session()

    wins = session.query(Move) \
        .filter(Move.player_id == player.id) \
        .count()

    session.close()

    return wins


def get_game_history(game_id: str) -> List[Move]:
    session = create_session()

    query = session.query(Move) \
        .filter(Move.game_id == game_id) \
        .all()

    moves = query

    session.close()

    return moves


def init_rolls():
    the_number = random.randint(0, 100)
    return the_number


def all_rolls() -> List[Move]:
    session = create_session()

    query = session.query(Move).order_by(Move.number).order_by(Move.count).all()
    rolls = list(query)

    session.close()

    return rolls

'''
def find_roll(name: str) -> Optional['Move']:
    session = create_session()

    query = session.query(Move).filter(Move.move == name) AND 
    roll = list(query)
    session.close()
    return roll
'''

def record_roll(player, move_ing:'Move', game_id: str, count, the_number, is_over):
    session = create_session()

    move = Move()
    move.player_id = player.id
    move.guess = move_ing
    move.game_id = game_id
    move.count = count
    move.is_over = is_over
    move.number = the_number

    session.add(move)

    session.commit()
    session.close()


def play_init():
    the_number = random.randint(0, 100)
    return the_number


def check_value(guess, the_number):
    if guess < the_number:
        #print('Sorry, your guess of {} was too LOW.'.format(guess))
        return "LOW"
    elif guess > the_number:
        return "HIGH"
    else:
        return True

def find_player_gane(player):
    session = create_session()
    wins = session.query(Move) \
        .filter(Move.player_id == player.id) \
        .count()


def get_game_history_by_player(player_id: int) -> List[Move]:
    session =  create_session()

    query = session.query(Move) \
        .filter(Move.player_id == player_id) \
        .order_by(Move.game_id) \
        .all()

    moves = list(query)

    session.close()

    return moves

def get_game_moves(game_id):
    session = create_session()

    query = session.query(Move) \
        .filter(Move.game_id == game_id) \
        .count()

    num = query
    return num