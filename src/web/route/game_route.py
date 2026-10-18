from web.module.flask_app import app
from flask import request, jsonify, abort
from di.container import container
from web.mapper.game_mapper import domain_to_web, web_to_domain
from web.model.board import Board
from web.model.game import Game
from domain.model.game import Game as DomainGame

service = container.service

@app.route('/game/<id>', methods=['POST'])
def handle_game_move(id):
    data = request.json
    cells = data["cells"]
    board = Board(cells)
    game = Game(id, board)
    domain_game = web_to_domain(game)
    if not service.validate_board(domain_game):
        abort(400, "The board is not validated")
    else:
        container.repository.save(domain_game)

        if service.is_game_over(domain_game):
            winner = service.get_winner(domain_game)
            web_game = domain_to_web(domain_game)
            return jsonify({"id": web_game.id, "cells": web_game.board.cells, "game_over": True, "winner": winner})

        new_game = service.get_next_move(domain_game)
        container.repository.save(new_game)
        if service.is_game_over(new_game):
            winner = service.get_winner(new_game)
            web_game = domain_to_web(new_game)
            return jsonify({"id": web_game.id, "cells": web_game.board.cells, "game_over": True, "winner": winner})
        else:
            web_game = domain_to_web(new_game)
            return jsonify({"id":web_game.id, "cells": web_game.board.cells})
    
@app.route('/game', methods=['POST'])
def create_game():
    new_game = DomainGame.new()
    container.repository.save(new_game)
    web_game = domain_to_web(new_game)
    return jsonify({"id":web_game.id, "cells":web_game.board.cells})
