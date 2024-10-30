# Polymorphism - for extensibility,code can be extended without modifying the orginal structure

# Define a base class Player
class Player:
    def play(self):
        # This is a placeholder method that will be overridden by child classes
        pass

# Define a FootballPlayer class that inherits from Player
class FootballPlayer(Player):
    def __init__(self, type):
        # Initialize the FootballPlayer with a type
        self.type = type
    
    def play(self):
        # Override the play method to print what type of football the player plays
        return print(f'Footballer plays {self.type}')

# Define a CricketPlayer class that inherits from Player
class CricketPlayer(Player):
    def __init__(self, type):
        # Initialize the CricketPlayer with a type
        self.type = type
    
    def play(self):
        # Override the play method to print what type of cricket the player plays
        return print(f'Cricketer plays {self.type}')

# Create instances of FootballPlayer and CricketPlayer
type1 = FootballPlayer("Football")
type2 = CricketPlayer("Cricketer")

# Call the play method for each instance
type1.play()  # This will print: Footballer plays Football
type2.play()  # This will print: Cricketer plays Cricketer

print(type1.type)