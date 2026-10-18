from domain.model.game import Game as DomainGame
from domain.model.board import Board as DomainBoard
from web.model.game import Game as WebGame
from web.model.board import Board as WebBoard

def domain_to_web(domain_game):
    web_board = WebBoard(domain_game.board.cells)
    web_game = WebGame(domain_game.id, web_board)
    return web_game

def web_to_domain(web_game):
    domain_board = DomainBoard(web_game.board.cells)
    domain_game = DomainGame(web_game.id, domain_board)
    return domain_game