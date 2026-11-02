from datasource.database import Base, SessionLocal, engine
from domain.model.game import Game as DomainGame
from datasource.model.game import Game
from datasource.mapper.game_mapper import domain_to_datasource, datasource_to_domain


Base.metadata.create_all(bind=engine)

game = DomainGame.new()

datasource_game = domain_to_datasource(game)

with SessionLocal() as db:
    db.add(datasource_game)
    db.commit()

with SessionLocal() as db:
    loaded_game = db.get(Game, game.id)

    if loaded_game is None:
        print("Игра не найдена!")
    else:
        restored_game = datasource_to_domain(loaded_game)

        print("Исходный ID:", game.id)
        print("Восстановленный ID:", restored_game.id)

        print("Исходные cells:", game.board.cells)
        print("Восстановленные cells:", restored_game.board.cells)

        print("ID совпадают:", game.id == restored_game.id)
        print("Cells совпадают:", game.board.cells == restored_game.board.cells)

        print("Тип ID:", type(restored_game.id))

        restored_game.board.cells[0][0] = 1
        print(loaded_game.board)