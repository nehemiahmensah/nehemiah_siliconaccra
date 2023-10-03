class Human:
    ##attributes / properties
    number_of_legs    = 0
    number_of_hands   = 0
    energy            = 0
    eyes              = 0
    jumping_ability   = False
    number_of_ears    = 0
    name              = "" 
    nostril           = 0

#constructor

    def __init__(self, name, eyes, number_of_legs, number_of_hands, number_of_ears, mouth):
        self.name = name
        self.eyes = eyes
        self.number_of_legs = number_of_legs
        self.number_of_ears = number_of_ears
        self.number_of_hands = number_of_hands
        self.mouth = mouth

    #def clap(self, num_of_hands):
        #print("Papapa")
    #or
    def clap(self):
        available_hands = self.number_of_hands
        return f"clapping with {available_hands} hands"

Stanley = Human("Stanley", 2, 2, 2, 2, 1)
#print(human1.name)
#print(human1.eyes)
#print(type(human1))
#print(human1.clap(2))

print(f"{Stanley.name} is {Stanley.clap()}")