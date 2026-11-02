from web.module.flask_app import app
from flask import request, jsonify, render_template
from di.container import container
from web.mapper.game_mapper import domain_to_web, web_to_domain
from web.model.board import Board
from web.model.game import Game
from domain.model.game import Game as DomainGame
from domain.exception.game_not_found_error import GameNotFoundError

service = container.service



@app.route('/game/<id>', methods=['POST'])
def handle_game_move(id):
    try:
        data = request.json
        cells = data["cells"]
        board = Board(cells)
        game = Game(id, board)
        domain_game = web_to_domain(game)

        if not service.validate_board(domain_game):
            return jsonify({'error': "The board is not validated"}), 400

        container.repository.save(domain_game)

        if service.is_game_over(domain_game):
            winner = service.get_winner(domain_game)
            web_game = domain_to_web(domain_game)
            return jsonify({
                "id": web_game.id,
                "cells": web_game.board.cells,
                "game_over": True,
                "winner": winner
            })

        new_game = service.get_next_move(domain_game)
        container.repository.save(new_game)

        if service.is_game_over(new_game):
            winner = service.get_winner(new_game)
            web_game = domain_to_web(new_game)
            return jsonify({
                "id": web_game.id,
                "cells": web_game.board.cells,
                "game_over": True,
                "winner": winner
            })
        else:
            web_game = domain_to_web(new_game)
            return jsonify({
                "id": web_game.id,
                "cells": web_game.board.cells
            })

    except GameNotFoundError:
        return jsonify({'error': 'Game not found'}), 404
    
@app.route('/game', methods=['POST'])
def create_game():
    new_game = DomainGame.new()
    container.repository.save(new_game)
    web_game = domain_to_web(new_game)
    return jsonify({"id":web_game.id, "cells":web_game.board.cells})

@app.route('/game/<id>', methods=['GET'])
def show_game(id):
    return render_template('game.html', game_id=id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<game_id>/state', methods=['GET'])
def get_game_state(game_id):
    domain_game = container.repository.get(game_id)
    web_game = domain_to_web(domain_game)

    response = {"id": web_game.id, "cells": web_game.board.cells}
    if service.is_game_over(domain_game):
        response["game_over"] = True
        response["winner"] = service.get_winner(domain_game)
    return jsonify(response)
