from datasource.mapper.game_mapper import domain_to_datasource, datasource_to_domain
from datasource.repository.storage import GameStorage
class GameRepository:
    def __init__(self, storage: GameStorage):
        self.storage = storage

    def save(self, domain_game):
        datasource_game = domain_to_datasource(domain_game)
        self.storage.save_game(datasource_game)

    def get(self, id):
        datasource_game = self.storage.get_game(id)
        domain_game = datasource_to_domain(datasource_game)
        return domain_game