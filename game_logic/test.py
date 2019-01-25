from game_logic import game_service


"""
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


g_p_id = list(set([players.id for players in game_service.all_players()
                   for game in game_service.get_game_history_by_player(players.id)]))

out_players = [game_service.get_game_history_by_player(player_id) for player_id in g_p_id]
mov = {m.game_id for data in out_players for m in data}
hist = [game_service.get_game_history(h) for h in mov]
"""
all_players = {player.id:player.name for player in game_service.all_players()}
out = {game.game_id:all_players[game.player_id] for game in game_service.all_rolls()}
cnt = [(out[k],game_service.get_game_moves(k)) for k in out.keys()]
game_score = sorted(cnt, key=lambda x:x[1])[:3]

for postion, record in enumerate(game_score, 1):
    print(f'{postion}. {record[0]} spend {record[1]} moves')