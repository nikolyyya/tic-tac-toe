import uuid
from domain.model.board import Board

class Game:
    def __init__(self, id, board: Board):
        self.id = id
        self.board = board

    @staticmethod
    def new():
        new_id = str(uuid.uuid4())
        return Game(new_id, Board.empty())
    
