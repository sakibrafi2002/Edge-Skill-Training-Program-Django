# Define a base class Player
class Player:
    def play(self):
        # This is a placeholder method that will be overridden by child classes
        pass

# Define a FootballPlayer class that inherits from Player
class FootballPlayer(Player):
    def __init__(self, type):
        # Initialize the FootballPlayer with a private type attribute
        self.__type = type
    
    # Override the play method to print what type of football the player plays
    def play(self):
        return print(f'Footballer plays {self.__type}')
    
    # Getter method to access the private type attribute
    def get_type(self):
        return self.__type
    
    # Setter method to modify the private type attribute
    def set_type(self, type):
        self.__type = type

# Define a CricketPlayer class that inherits from Player
class CricketPlayer(Player):
    def __init__(self, type):
        # Initialize the CricketPlayer with a private type attribute
        self.__type = type
    
    # Override the play method to print what type of cricket the player plays
    def play(self):
        return print(f'Cricketer plays {self.__type}')
    
    # Getter method to access the private type attribute
    def get_type(self):
        return self.__type
    
    # Setter method to modify the private type attribute
    def set_type(self, type):
        self.__type = type

# # Create instances of FootballPlayer and CricketPlayer
# football_player = FootballPlayer("Football")
# cricket_player = CricketPlayer("Cricket")

# # Call the play method for each instance
# football_player.play()  # This will print: Footballer plays Football
# cricket_player.play()  # This will print: Cricketer plays Cricket

# # Access and modify the private 'type' using getter and setter
# print("\nUpdating player types using setter...")

# # Using setter to change the 'type' of football_player
# football_player.set_type("Soccer")
# # Using setter to change the 'type' of cricket_player
# cricket_player.set_type("Test Cricket")

# # Using getter to access the updated 'type'
# print(f'Updated FootballPlayer type: {football_player.get_type()}')  # Output: Soccer
# print(f'Updated CricketPlayer type: {cricket_player.get_type()}')  # Output: Test Cricket

# # Check the updated play method after modification
# football_player.play()  # This will now print: Footballer plays Soccer
# cricket_player.play()  # This will now print: Cricketer plays Test Cricket



# Create instances of FootballPlayer and CricketPlayer
type1 = FootballPlayer("Football")
type2 = CricketPlayer("Cricketer")
type2 = CricketPlayer("Cricketer2")
# Call the play method for each instance
type1.play()  # This will print: Footballer plays Football
type2.play()  # This will print: Cricketer plays Cricketer

