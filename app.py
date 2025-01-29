class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
              'a1': None, 'b1': None, 'c1': None,
              'a2': None, 'b2': None, 'c2': None,
              'a3': None, 'b3': None, 'c3': None,
            }
    def play_game(self):
        print(f"Welcome to the game, {self.turn} goes first!")
    
    def print_board(self):
        b = self.board
        print(f"""
              A   B   C
          1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
               ----------
          2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
               ----------
          3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie == True:
            print("Tie game!")
        elif self.winner == "X" or self.winner == "O":
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def get_move(self):
     
       while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            
            if move in self.board and self.board[move] == None:
                return move
            elif move in self.board and self.board[move] != None:
                print("That space is taken, choose another")
            else: 
                print("Invalid move! Please enter an available space on the board.")
    
    def render(self):
        game_instance.print_board()
        game_instance.print_message()
        game_instance.get_move()
    
    
    
    
    def __str__(self):
        return 'This is the Game() class.'


# Instantiate the Game class:
game_instance = Game()

# Invoke the play_game method:
game_instance.play_game()
game_instance.render()

