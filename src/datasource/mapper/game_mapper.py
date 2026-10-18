from domain.model.game import Game as DomainGame
from domain.model.board import Board as DomainBoard
from datasource.model.game import Game as DatasourceGame
from datasource.model.board import Board as DatasourceBoard

def domain_to_datasource(domain_game):
    datasource_board = DatasourceBoard(domain_game.board.cells)
    datasource_game = DatasourceGame(domain_game.id, datasource_board)
    return datasource_game

def datasource_to_domain(datasource_game):
    domain_board = DomainBoard(datasource_game.board.cells)
    domain_game = DomainGame(datasource_game.id, domain_board)
    return domain_game