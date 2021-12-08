import numpy as np
            
class Board():
    
    def __init__(self, file):
        self.Board = []
        self.Win_Turn = 0
        self.Score = 0
        self.last_number = 0
        for line in file:
            line = line.splitlines()
            if line != ['']:
                line = line[0].split(' ') 
                Buffer = [int(element) for element in line if element != '']
                self.Board = np.append(self.Board, Buffer)
                if (len(self.Board) == 25):
                    self.Board = np.reshape(self.Board, [5, 5])
                    self.Board = self.Board.astype(int)
                    break
                
    def play_number(self, number : int):
        self.last_number = number
        for index_line, line in enumerate(self.Board):
            for index_element, element in enumerate(line):
                if element == number:
                    self.Board[index_line, index_element] = 0
    
    def check_result(self):
        is_win = False
        for line in self.Board:
            if sum(line) == 0:
                is_win = True
                
        for col in self.Board.T:
            if sum(col) == 0:
                is_win = True
        
        Diag = []
        for index in range(5):
            Diag.append(self.Board[index, index])
        if sum(Diag) == 0:
            is_win == True
            
        Diag = []
        for index in range(5):
            Diag.append(self.Board[index, -index])
        if sum(Diag) == 0:
            is_win == True
        
        if is_win:
            return sum(sum(self.Board))
        else:
            return 0
        
    def play(self, Commands):
        for command in Commands:
            self.Win_Turn += 1
            self.play_number(int(command))
            self.Score = self.check_result()
            if self.Score != 0:
                return 0
                 
    def getWinTurn(self):
        return self.Win_Turn   
        
if __name__ == '__main__':
    with open('Day4/Boards.csv', 'r') as file:
        file_length = len(file.readlines())
    number_of_board = int((file_length - 1)/6)
    
    Boards = []
    
    with open('Day4/Boards.csv', 'r') as file:
        Commands = file.readline()
        Commands = Commands.splitlines()
        Commands = Commands[0].split(',')
        for Board_number in range(number_of_board):
            Boards.append(Board(file))
            
    win_turns = []
    for Board in Boards:
        Board.play(Commands)
        win_turns.append(Board.getWinTurn())
        
    winning_board = win_turns.index(min(win_turns))
    last_winning_number = Boards[winning_board].last_number
    winning_score = Boards[winning_board].Score
    
    print(f'Solution 1 : Winning Board n°{winning_board}, Last number called : {last_winning_number}, Score : {winning_score}, Answer : {winning_score*last_winning_number}')
    
    losing_board = win_turns.index(max(win_turns))
    last_losing_number = Boards[losing_board].last_number
    losing_score = Boards[losing_board].Score
    
    print(f'Solution 2 : Losing Board n°{losing_board}, Last number called : {last_losing_number}, Score : {losing_score}, Answer : {losing_score*last_losing_number}')

        
    
                