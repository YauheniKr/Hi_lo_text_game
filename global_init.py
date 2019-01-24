import sqlalchemy
import sqlalchemy.orm
from model.model_base import ModelBase
from model import move, player

__factory = None


def global_init():
    global __factory

    full_file = 'postgres:31415@192.168.50.17:5432/hi_lo_game'
    conn_str = 'postgresql://' + full_file

    engine = sqlalchemy.create_engine(conn_str, echo=False)
    ModelBase.metadata.create_all(engine)

    __factory = sqlalchemy.orm.sessionmaker(bind=engine)


def create_session():
    global __factory

    if __factory is None:
        global_init()

    return __factory()
