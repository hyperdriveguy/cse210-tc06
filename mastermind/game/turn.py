class Turn:
    """A maneuver in the game. The responsibility of Guess is to keep track of the guess.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (integer): The guess to compare code to
        
    """
    def __init__(self, guess):
        """The class constructor.
        
        Args:
            self (Guess): an instance of Guess.
        """
        self._guess = guess
        


    def get_guess(self):
        """Returns the guess to compare to code to 

        Args:
            self (Move): an instance of Guess.
        """

        return str(self._guess)

    def get_hint(self):
        """Generates a hint based on the given code and guess.

        Args:
            self (Safe): An instance of Safe.
            guess (string): The guess that was made.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = '****'
        for index, letter in enumerate(self._guess):
            if self._code[index] == letter:
                hint += "x"
            elif letter in self._code:
                hint += "o"
            else:
                hint += "*"
        return hint


