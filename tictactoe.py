###

class TicTacToe:
    
    PLAYERS = ('O','X')
    N = 3
    
    def __init__(self):
        self.board = [[j for j in range((i*self.N)+1,(i*self.N)+1+self.N)] for i in range(self.N)]
    
    def reset_board(self):
        self.board = [[j for j in range((i*self.N)+1,(i*self.N)+1+self.N)] for i in range(self.N)]
    
    def render_board(self):
        return f" {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} \n---------\n{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} \n---------\n{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} "
    
    def make_move(self, player_index, cell_index):
        checker = self.PLAYERS[player_index]
        self.board[(int(cell_index//3.5))][(cell_index%self.N)-1] = checker
    
    def is_valid_move(self, cell_index):
        return True if type(self.board[(int(cell_index//3.5))][(cell_index%self.N)-1]) == int else False
    
    def is_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if type(self.board[i][j]) == int:
                    return False
        return True
    
    def get_winner(self):
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
        for i in range(len(self.board)):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[0][i]
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        elif self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        return -1
    
    def game(self):
        print("Welcome to TicTacToe.")
        p1c = int(input("Player 1 choose your mark:\n1.O\n2.X\n: "))

        if p1c == 2:
            self.PLAYERS = ("X", "O")
        
        print(f"Player 1 will play as {self.PLAYERS[0]}.")
        print(f"Player 1 will play as {self.PLAYERS[1]}.")

        print("Ready?")
        print("")
        print(self.render_board().strip())
        print("")
        
        turn = 1
        
        while self.is_full() != True:
            p = 1 if turn%2==0 else 0
            print(f"Move of player {p+1}")
            move = int(input("Enter index of where you want to play: "))
            print("")
            
            if self.is_valid_move(move):
                self.make_move(p, move)
                print(self.render_board().strip())
                print("")
                turn += 1
                
                if self.get_winner() != -1:
                    print("Game Over!")
                    print(f"Player {p+1} wins!")
                    break
            
            else:
                print("Invalid move. Square is already taken.")
                print("Try again?")
        
        if self.is_full():
            print("Game Over!")
            print("That's a draw.")
        
        print("")
        cont = input("Play again? (y/n): ")
        print("")
        if cont == "y":
            self.reset_board()
            self.game()
        else:
            print("Thanks for playing!")
                

a = TicTacToe()
a.game()