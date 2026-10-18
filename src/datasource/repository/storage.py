from domain.model.game import Game
from threading import Lock

class GameStorage:
    def __init__(self):
        self.dict = {}
        self._lock = Lock()

    def get_game(self, id):
            with self._lock:
                 return self.dict[id]
    
    def save_game(self, game: Game):
        with self._lock:
             self.dict[game.id] = game