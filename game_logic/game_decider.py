from enum import Enum
from web import app

class Decision(Enum):
    win = 2
    lose = 3

    def reversed(self):
        if self == Decision.win:
            return Decision.lose
        if self == Decision.lose:
            return Decision.win

        return Decision.tie

    def __str__(self):
        if self == Decision.win:
            return 'win'
        if self == Decision.lose:
            return 'lose'

        return "UNKNOWN DECISION: {}".format(self)


def decide(move) -> Decision:

    if move == app.build_starter_data():
        return Decision.win
    else:
        return Decision.lose
