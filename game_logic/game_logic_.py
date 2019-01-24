from collections import defaultdict
from typing import List, Optional

from game_logic import game, game_decider
from game_logic.game_decider import Decision
from model.move import Move
# noinspection PyPackageRequirements
from model.player import Player
# noinspection PyPackageRequirements
#from model.roll import Roll
from global_init import create_session

def get_game_history(game_id: str) -> List[Move]:
    session = create_session()

    query = session.query(Move) \
        .filter(Move.game_id == game_id) \
        .order_by(Move.number) \
        .order_by(Move.count) \
        .all()

    moves = list(query)

    session.close()

    return moves


def is_game_over(game_id: str) -> bool:
    history = get_game_history(game_id)
    return any([h.is_over for h in history])

#todo: переделать на подсчет кол-во попыток
def get_win_count(player: Player) -> int:
    session = create_session()

    wins = session.query(Move) \
        .filter(Move.player_id == player.id). \
        count()

    session.close()

    return wins


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


def all_players() -> List[Player]:
    session = create_session()

    players = list(session.query(Player).all())
    session.close()
    return players


def record_roll(player, move: 'Move', game_id: str, is_over: bool, roll_num: int):
    session = create_session()

    move = Move()
    move.player_id = player.id
    move.roll_id = move.id
    move.game_id = game_id
    move.is_winning_play = is_over
    move.roll_number = roll_num
    session.add(move)

    session.commit()
    session.close()


def all_rolls() -> List[Move]:
    session = create_session()

    query = session.query(Move).order_by(Move.number).order_by(Move.count).all()
    rolls = list(query)

    session.close()

    return rolls


def find_roll(name: str) -> Optional['Move']:
    session = create_session()

    roll = session.query(Move).filter(Move.number == name).first()

    session.close()
    return roll

def find_player_by_id(player_id: int) -> Player:
    session = create_session()
    player = session.query(Player).filter(Player.id == player_id).first()
    session.close()

    return player

'''
def count_round_wins(player_id: int, game_id: str) -> int:
    history = get_game_history(game_id)
    wins = 0
    grouped_moves = defaultdict(list)

    for h in history:
        grouped_moves[h.roll_number].append(h)

    for rnd_num, moves in grouped_moves.items():
        player_move = [m for m in moves if m.player_id == player_id][0]
        opponent_move = [m for m in moves if m.player_id != player_id][0]

        player_roll = find_roll_by_id(player_move.roll_id)d)

        outcome = game_decider.decide(player_roll, opponent_roll)
        if outcome == Decision.win:
            wins += 1

    return wins
'''