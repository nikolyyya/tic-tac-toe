from datasource.repository.storage import GameStorage
from datasource.repository.constructor_repository import GameRepository
from datasource.service.game_service_impl import GameServiceImpl
class Container:
    def __init__(self):
        self.storage = GameStorage()
        self.repository = GameRepository(self.storage)
        self.service = GameServiceImpl(self.repository)

container = Container()