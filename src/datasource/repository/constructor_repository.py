from datasource.model.game import Game as DatasourceGame
#from datasource.database import SessionLocal
from datasource.mapper.game_mapper import domain_to_datasource, datasource_to_domain


class GameRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def save(self, domain_game):
        datasource_game = domain_to_datasource(domain_game)
        with self.session_factory() as db:
            db.merge(datasource_game)
            db.commit()

    def get(self, id):
        with self.session_factory() as db:
            game = db.get(DatasourceGame, id)
            if game:
                return datasource_to_domain(game)
            return None


    
