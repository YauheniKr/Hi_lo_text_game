import random
import uuid

import flask
from game_logic import game_service
from game_logic.game import GameRound


def build_views(app):

    @app.route('/api/game/users/<user>', methods=['GET'])
    def find_user(user: str):
        player = game_service.find_player(user)
        if not player:
            return flask.jsonify(404)#flask.abort(404)
        return flask.jsonify(player.to_json())


    @app.route('/api/game/users', methods=['PUT'])
    def create_user():

        try:
            if not flask.request.json \
                    or 'user' not in flask.request.json \
                    or not flask.request.json.get('user'):
                raise Exception("Invalid request: no value for user.")

            username = flask.request.json.get('user').strip()
            player = game_service.create_player(username)
            return flask.jsonify(player.to_json())

        except Exception as x:
            flask.abort(flask.Response(
                response="Invalid request: {}".format(x),
                status=400
            ))

    @app.route('/api/game/games', methods=['POST'])
    def create_game():
        return flask.jsonify({'game_id': str(uuid.uuid4()),
                              'the_number': game_service.play_init()})

    @app.route('/api/game/<game_id>/status', methods=['GET'])
    def game_status(game_id: str):
        is_over = game_service.is_game_over(game_id)
        history = game_service.get_game_history(game_id)

        if not history:
            flask.abort(404)

        roll_lookup = {r.id: r for r in game_service.all_rolls()}
        player_lookup = {p.id: p for p in game_service.all_players()}
        player = game_service.find_player_by_id(history[0].player_id)

        data = {
            'is_over': is_over,
            'moves': [h.guess for h in history],
            'player': player.to_json(),
            'number':history[0].number
        }

        return flask.jsonify(data)

    @app.route('/api/game/top_scores', methods=['GET'])
    def top_scores():
        players = game_service.all_players()
        wins = [
            {'player': p.to_json(), 'score': game_service.get_win_count(p)}
            for p in players
        ]

        wins.sort(key=lambda wn: -wn.get('score'))
        return flask.jsonify(wins[:10])

    @app.route('/api/game/play_round', methods=['POST'])
    def play_round():

        try:
            move, db_user, game_id, the_number = validate_round_request()
            game = GameRound(game_id, db_user, move, the_number)
            game.play()

            return flask.jsonify({
                'move': game.p_move,
                'player': db_user.to_json(),
                'status': game.status,
                'is_over': game.is_over,
        })

        except Exception as x:
            flask.abort(flask.Response(response='Invalid request: {}'.format(x), status=400))

    def validate_round_request():
        if not flask.request.json:
            raise Exception("Invalid request: no JSON body.")
        game_id = flask.request.json.get('game_id')
        if not game_id:
            raise Exception("Invalid request: No game_id value")
        the_number = flask.request.json.get('the_number')
        user = flask.request.json.get('user')
        if not user:
            raise Exception("Invalid request: No user value")
        db_user = game_service.find_player(user)
        if not db_user:
            raise Exception("Invalid request: No user with name {}".format(user))
        move = flask.request.json.get('move')
        if not move:
            raise Exception("Invalid request: No roll value")
        db_move = move
        is_over = game_service.is_game_over(game_id)
        if is_over:
            raise Exception("This game is already over.")
        return db_move, db_user, game_id, the_number
