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
        self.render()
    
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
                self.board[move] = self.turn
                return move
            elif move in self.board and self.board[move] != None:
                print("That space is taken, choose another")
            else: 
                print("Invalid move! Please enter an available space on the board.")
    
    def check_for_winner(self):
        if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']):
            self.winner = self.board['a1']
            return True

        elif self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']):
            self.winner = self.board['a2']
            return True
            
        elif self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']):
            self.winner = self.board['a3']
            return True
            
        elif self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']):
            self.winner = self.board['a1']
            return True
            
        elif self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']):
            self.winner = self.board['b1']
            return True
            
        elif self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']):
            self.winner = self.board['c1']
            return True
            
        elif self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']):
            self.winner = self.board['a1']
            return True
            
        elif self.board['c1'] and (self.board['c1'] == self.board['b2'] == self.board['a3']):
            self.winner = self.board['c1']
            return True
        
        return False


    def check_for_tie(self):
        board_full = True
        for pos in self.board:
            if self.board[pos] == "" or self.board[pos] == None:
                board_full = False

        winner_exists = self.check_for_winner()
        
        if board_full and not winner_exists:
            self.tie = True
        
        else:
            self.tie = False

    def switch_turn(self):
        turn_lookup = {'X': 'O', 'O': 'X'}
        self.turn = turn_lookup[self.turn]

    
    def render(self):
        while not self.winner and not self.tie:
            self.print_board()
            self.print_message()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()

            if not self.winner and not self.tie:
                self.switch_turn()
        
        self.print_board()
        self.print_message()
    
    
    def __str__(self):
        return 'This is the Game() class.'

# Instantiate the Game class:
game_instance = Game()

# Invoke the play_game method:
game_instance.play_game()