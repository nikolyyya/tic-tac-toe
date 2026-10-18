from domain.service.game_service import GameService
from datasource.repository.constructor_repository import GameRepository
from domain.model.game import Game
from domain.model.board import Board

class GameServiceImpl(GameService):
    def __init__(self, repository: GameRepository):
        self.repository = repository

    def is_game_over(self, game: Game):
        current_cells = game.board.cells
        finish = False
        not_empty = 0
        for i in range(3):
            if current_cells[0][i] == current_cells[1][i] and current_cells[2][i] == current_cells[1][i] and current_cells[0][i]!=0:
                finish = True
                break
            
        if not finish:
            for i in range(3):
                if current_cells[i][0] == current_cells[i][1] and current_cells[i][2] == current_cells[i][1] and current_cells[i][0]!=0:
                    finish = True
                    break
                
        if not finish:
            if current_cells[0][0]==current_cells[1][1] and current_cells[1][1]==current_cells[2][2] and current_cells[0][0]!=0:
                finish = True
            
        if not finish:
            if current_cells[0][2]==current_cells[1][1] and current_cells[1][1]==current_cells[2][0] and current_cells[2][0]!=0:
                finish = True

        if not finish:
            for i in range(3):
                for j in range(3):
                    if current_cells[i][j]!=0:
                        not_empty += 1

        if not_empty == 9:
            finish = True
        return finish
    
    def validate_board(self, game: Game):
        current_id = game.id
        current_cells = game.board.cells
        previous_game = self.repository.get(current_id)
        previous_cells = previous_game.board.cells
        expected_symbol = GameServiceImpl.computer_step(previous_cells)
        valid = True
        count_change = 0
        for i in range(3):
            for j in range(3):
                if current_cells[i][j]!=previous_cells[i][j]:
                    if previous_cells[i][j]!=0 or current_cells[i][j]!=expected_symbol:
                        valid = False
                    count_change += 1
        if count_change != 1:
            valid = False
        return valid
    
    @staticmethod
    def computer_step(cells):
        count1 = count2 = 0
        result = 0
        for i in range(3):
            for j in range(3):
                if cells[i][j] == 1:
                    count1 +=1
                if cells[i][j] == 2:
                    count2 +=1
        if count1 == count2:
            result = 1
        else:
            result = 2
        return result
    
    @staticmethod
    def check_winner(cells):
        result = -1
        not_empty = 0
        for i in range(3):
            if cells[0][i] == cells[1][i] and cells[2][i] == cells[1][i] and cells[0][i]==1:
                result = 1
                break
            
        if result==-1:
            for i in range(3):
                if cells[i][0] == cells[i][1] and cells[i][2] == cells[i][1] and cells[i][0]==1:
                    result = 1
                    break

        if result==-1:
            for i in range(3):
                if cells[0][i] == cells[1][i] and cells[2][i] == cells[1][i] and cells[0][i]==2:
                    result = 2
                    break
            
        if result==-1:
            for i in range(3):
                if cells[i][0] == cells[i][1] and cells[i][2] == cells[i][1] and cells[i][0]==2:
                    result = 2
                    break
                
        if result==-1:
            if cells[0][0]==cells[1][1] and cells[1][1]==cells[2][2] and cells[0][0]==1:
                result = 1
        
        if result==-1:
            if cells[0][0]==cells[1][1] and cells[1][1]==cells[2][2] and cells[0][0]==2:

                result = 2
            
        if result==-1:
            if cells[0][2]==cells[1][1] and cells[1][1]==cells[2][0] and cells[2][0]==1:
                result = 1
            
        if result==-1:
            if cells[0][2]==cells[1][1] and cells[1][1]==cells[2][0] and cells[2][0]==2:
                result = 2

        if result==-1:
            for i in range(3):
                for j in range(3):
                    if cells[i][j]!=0:
                        not_empty += 1

        if not_empty == 9:
            result = 0
        return result

    @staticmethod
    def minimax(step, cells, depth, is_maximum):
        result = GameServiceImpl.check_winner(cells)
        if result!=-1:
            if result == step:
                return 100 - depth
            elif result == 0:
                return 0
            else:
                return -100 + depth
        else:
            if is_maximum:
                best = -10**10
                for i in range(3):
                    for j in range(3):
                        if cells[i][j] == 0:
                            cells[i][j] = step
                            score = GameServiceImpl.minimax(step, cells, depth+1, False)
                            best = max(best, score)
                            cells[i][j] = 0
                return best
            else:
                best = 10**10
                for i in range(3):
                    for j in range(3):
                        if cells[i][j] == 0:
                            cells[i][j] = 1 if step == 2 else 2
                            score = GameServiceImpl.minimax(step, cells, depth+1, True)
                            best = min(best, score)
                            cells[i][j] = 0
                return best
        
        
    
    
    def get_next_move(self, game: Game):
        current_cells = game.board.cells
        change_cells = [current_cells[y].copy() for y in range(3)]
        best_score = -10**10
        best_move = None
        step = self.computer_step(change_cells)
        for i in range(3):
            for j in range(3):
                if change_cells[i][j] == 0:
                    change_cells[i][j] = step
                    score = self.minimax(step, change_cells, 0, False)
                    change_cells[i][j] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        change_cells[best_move[0]][best_move[1]] = step
        new_board = Board(change_cells)
        new_game = Game(game.id, new_board)
        return new_game
    
    def get_winner(self, game):
        return GameServiceImpl.check_winner(game.board.cells)