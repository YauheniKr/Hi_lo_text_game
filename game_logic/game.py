from collections import defaultdict
import random
from game_logic import game_service, game_decider
#from game_logic.game_decider import Decision
from model.player import Player
from model.move import Move


class GameRound:


    def __init__(self, game_id: str, player: Player,
                 p_move, the_number):
        self.p_move = p_move
        self.game_id = game_id
        self.player = player
        history = game_service.get_game_history(game_id)
        self.is_over = game_service.is_game_over(game_id)
        self.the_number = the_number

    def play(self):
        i = 1
        is_over = False
        guess_text = self.p_move
        check_val = game_service.check_value(int(guess_text), self.the_number)
        if check_val == True:
            is_over = True
        else:
            is_over = False
        self.status = check_val
        self.count = i
        self.is_over = is_over
        self.record_roll(self.player, guess_text)

    def record_roll(self, player: Player, move: Move):
        #final_round_candidate = self.round >= self.PLAY_COUNT_MIN and win_count + 1 >= self.WIN_COUNT_MIN
        #wins_game = final_round_candidate and decision == Decision.win

        game_service.record_roll(player, move, self.game_id, self.count, self.the_number, self.is_over)