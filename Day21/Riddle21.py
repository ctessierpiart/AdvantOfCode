from typing import Type

class Player():
    def __init__(self, pos, score = 0):
        self.point = score
        self.pos = pos
        self.turn = 0

class Dirac_dice():
    
    def __init__(self, pos_1 : int, pos_2 : int, score_1 = 0, score_2 = 0):
        self.Player_1 = Player(pos_1, score_1)
        self.Player_2 = Player(pos_2, score_2)
        
        self.previous_player = 0
        
        self.deterministic_dice = 0
        self.nb_roll = 0
    
    def update_pos(self, player : Type[Player], dice_result : int):
        remaining_score = player.pos + dice_result
        while remaining_score > 10:
            remaining_score -= 10
        player.pos = remaining_score
            
    
    def play_turn(self, dice = None):
        dice_result = 0
        dice_result = self.roll_dice(dice)
        dice_result = self.roll_dice(dice)
        dice_result = self.roll_dice(dice)

        if self.previous_player == self.Player_1:
            player = self.Player_2
        else:
            player = self.Player_1
        
        self.update_pos(player, dice_result)
        player.turn += 1
        player.point += player.pos
        
        self.previous_player = player
            
    def roll_dice(self, dice = None):
        dice_result = 0
        if dice is 'deterministic':
            self.deterministic_dice += 1
            self.nb_roll += 1
            dice_result += self.deterministic_dice
            return dice_result
        if isinstance(dice, int):
            return dice
        
if __name__ == '__main__':
    
    # Part 1
    Game = Dirac_dice(1, 10)
    while Game.Player_1.point < 1000 and Game.Player_2.point < 1000:
        Game.play_turn(dice = 'deterministic')
        
    # Part 2
    Games = []
    for rolls in range(3, 9):
        Games.append()
        
min_score = min([Game.Player_1.point, Game.Player_2.point])
print(f'Solution 1 : {min_score * Game.nb_roll}')