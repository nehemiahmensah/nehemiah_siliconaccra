import random
class Ludo:
    #ATTRIBUTES OR PROPERTIES
    board   = 0
    die     = 0
    token   = 0
    colors  = 0
    players = 0

    #CONSTRUCTOR
    def __init__(self,board,die,token,colors,players):
        self.board   = board
        self.die     = die
        self.token   = token
        self.colors  = colors
        self.players = players

    #METHOD / FUNCTION OF THE CLASS
    def rounds(self):
        game_rounds = self.board
        if self.board > 0:
           return f"You want to play {self.board} no. of games"
        else: 
            return "Number of games not specified"

game1 = Ludo(2,1,8,2,2)
print(f"{game1.rounds()} with {game1.players} players ")

class Dice:
    side_shown  = 0

    # CONSTRUCTOR 
    def __init__(self,side_shown):
        self.side_shown = side_shown

    # METHOD FOR DIE    
    def roll(self):
        self.side_shown = random.randint(1,6)
        side_shown = self.side_shown

        return side_shown

th = input("Enter ' * ' to roll a dice : ")   
trig = Dice("th")
print(f" You rolled {trig.roll()}")

