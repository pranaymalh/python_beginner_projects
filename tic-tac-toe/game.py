class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    def print_board(self,first_time):
        board = self.board
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if first_time:
                    print(str(i*n + j),end="")
                else:
                    print(board[i][j])
                if j < n-1:
                    print(" | ",end="")
            print()
    def update_board(self,i,j,val):
        self.board[i][j] = str(val)

if __name__=='__main__':
    board = Board()
    board.print_board(True)