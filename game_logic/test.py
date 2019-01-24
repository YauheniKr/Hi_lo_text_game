from game_logic import game_service


for players in game_service.all_players():
    games_player_id = []
    num_moves = []
    print(players.id, players.name)
    games = game_service.get_game_history_by_player(players.id)
    for game in games:
        games_player_id.append(game.game_id)
        games_player_id = list(set(games_player_id))
    for game_player_id in games_player_id:
        num_moves.append(game_service.get_game_moves(game_player_id))
    try:
        num_player = min(num_moves)
    except ValueError:
        num_player = 'Not played'
    print(num_player)