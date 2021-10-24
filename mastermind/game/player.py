from game.turn import Turn

class Player:
    """A person taking part in a game. The responsibility of Player is to keep track of their identity and last guess.
    
    Stereotype: 
        Information Holder

    Attributes:
        _name (string): The player's name.
        _guess (Guess): The player's last guess.
    """
    def __init__(self, name):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self._name = name
        self._turn = Turn('----', '****')
        
    def get_turn(self):
        """Returns the player's last turn (guess and hint) (an instance of Turn). If the player 
        hasn't taken a turn yet this method returns None.

        Args:
            self (Player): an instance of Player.
        """
        return self._turn

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._name.title()

    def set_turn(self, turn):
        """Sets the player's last turn (guess and hint) to the given instance of Turn.

        Args:
            self (Player): an instance of Player.
            turn (Turn): an instance of turn
        """
        self._turn = turn