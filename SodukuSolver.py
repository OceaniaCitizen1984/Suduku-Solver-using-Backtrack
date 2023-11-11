class SudukuSolver:
    def __init__(self):
    
        self.board = [
            [2, 5, 0, 0, 3, 0, 9, 0, 1],
            [0, 1, 0, 0, 0, 4, 0, 0, 0],
            [4, 0, 7, 0, 0, 0, 2, 0, 8],
            [0, 0, 5, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 9, 8, 1, 0, 0],
            [0, 4, 0, 0, 0, 3, 0, 0, 0],
            [0, 0, 0, 3, 6, 0, 0, 7, 2],
            [0, 7, 0, 0, 0, 0, 0, 0, 3],
            [9, 0, 3, 0, 0, 0, 6, 0, 4]
        ]

        self.domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def check_conflict(self, pos, num):
        row, col = pos

        #Check Rows
        for i in range(9):
            if self.board[i][col] == num:
                print('Row conflict ', i , col)
                return False
            
        #Check Columns
        for i in range(9):
            if self.board[row][i] == num:
                return False
                print('Col conflict')

        rowBlockStart = 3 * (row // 3)
        colBlockStart = 3 * (col // 3)

        rowBlockEnd = rowBlockStart + 3
        colBlockEnd = colBlockStart + 3
        for i in range(rowBlockStart, rowBlockEnd):
            for j in range(colBlockStart, colBlockEnd):
                if self.board[i][j] == num:
                    print('Block Conflict')
                    return False
                
        return True
        
    def solve(self):

        for row in range(9):

            for col in range(9):

                if self.board[row][col] == 0:

                    for trail in self.domain:

                        if (self.check_conflict([row, col], trail)):
                            self.board[row][col] = trail
                        
                            if self.solve():
                                return True
                        
                            #Backtracking
                            self.board[row][col] = 0

                    return False
        return True        

    def printBoard(self):
        for row in self.board:
            print(row)
    
game = SudukuSolver()
game.solve()
game.printBoard()