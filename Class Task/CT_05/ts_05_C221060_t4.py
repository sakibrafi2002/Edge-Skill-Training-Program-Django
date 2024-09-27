# Abstraction is like template class that defines what methods or shape the child classes will look like
# ABC and abstractmethod means that all the child of parent(Player) must have the "play" method defined,otherwise its an error
# alternative of this is in the next tast "TS_05.C221046.05.py" (alternative)

from abc import ABC, abstractmethod
# Define a base class Player
class Player(ABC):
    @abstractmethod
    def play(self):
        # This is a placeholder method that will be overridden by child classes
        pass

# Define a FootballPlayer class that inherits from Player
class FootballPlayer(Player):
    def play(self):
        # Override the play method to print what type of football the player plays
        return print(f'Footballer plays {self.type}')


# Create instances of FootballPlayer and CricketPlayer
type1 = FootballPlayer("Football")

# Call the play method for each instance
type1.play()  # This will print: Footballer plays Football
