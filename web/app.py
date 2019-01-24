import flask
from game_logic import game_decider, game_service
from web.views import home, game_api


app = flask.Flask(__name__)


def main():
    build_starter_data()
    build_views()
    run_web_app()


def build_views():
    game_api.build_views(app)
    home.build_views(app)


def build_starter_data():

    ran_number = game_service.init_rolls()
    return ran_number


def run_web_app():
    app.run(host='192.168.88.131', debug=True)


if __name__ == '__main__':
    main()
