import uuid
from domain.model.board import Board

class Game:
    def __init__(self, id: uuid.UUID, board: Board):
        self.id = id
        self.board = board

    @staticmethod
    def new():
        new_id = uuid.uuid4()
        return Game(new_id, Board.empty())
    
