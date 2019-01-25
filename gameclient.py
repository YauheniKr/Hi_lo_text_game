from client.api import GameService
from game_logic import game_service

def main():
    svc = GameService()
    print("Game app! (client)")
    print()

    game_id = svc.create_game().get('game_id')
    the_number = svc.create_game().get('the_number')
    player_input = input("Please, insert your name: ")
    player = svc.find_user(player_input)
    player_dict = {"user": player_input}
    if player == 404:
        player = svc.create_user(**player_dict)
    is_over = False
    while not is_over:
        name = player.get('name')
        roll = input('Insert you move: ')
        print()
        rnd = svc.play_round(game_id=game_id, user=name, move=roll, the_number=the_number)
        if rnd['status'] == 'HIGH':
            print('Sorry {}, your guess of {} was too HIGH.'.format(name, roll))
        elif rnd['status'] == 'LOW':
            print('Sorry {}, your guess of {} was too LOW.'.format(name, roll))
        else:
            print('Excellent work {}, you won, it was {}!'.format(name, the_number))
            break


if __name__ == '__main__':
    main()