class Board:
    def __init__(self, cells:list[list[int]]):
        # cells: 3x3 матрица, 0 = пусто, 1 = крестик, 2 = нолик
        self.cells = cells

    @staticmethod
    def empty():
        new_cells = [[0 for i in range(3)] for j in range(3)]
        return Board(new_cells)
    
