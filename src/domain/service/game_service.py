from abc import ABC, abstractmethod

class GameService(ABC):

    @abstractmethod
    def get_next_move(self, game):
        pass

    @abstractmethod
    def validate_board(self, game):
        pass

    @abstractmethod
    def is_game_over(self, game):
        pass

    @abstractmethod
    def get_winner(self, game):
        pass