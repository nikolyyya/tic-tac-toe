from domain.model.game import Game as DomainGame
from domain.model.board import Board as DomainBoard
from datasource.model.game import Game as DatasourceGame
import copy

def domain_to_datasource(domain_game):
    datasource_game = DatasourceGame(id=domain_game.id, board=copy.deepcopy(domain_game.board.cells))
    return datasource_game

def datasource_to_domain(datasource_game):
    domain_board = DomainBoard(datasource_game.board)
    domain_game = DomainGame(datasource_game.id, copy.deepcopy(domain_board))
    return domain_game