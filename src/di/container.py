from datasource.repository.constructor_repository import GameRepository
from datasource.service.game_service_impl import GameServiceImpl
from datasource.database import SessionLocal as session_factory
class Container:
    def __init__(self):
        self.repository = GameRepository(session_factory)
        self.service = GameServiceImpl(self.repository)

container = Container()