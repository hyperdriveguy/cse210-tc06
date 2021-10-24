class Turn:
    """A maneuver in the game. 
       The responsibility of Turn is to keep track of the guess and corresponding hint.
    
    Stereotype: 
        Information Holder

    Attributes:
        _guess (str): The guess to compare code to
        _code (str): The number the player trys to guess
        
    """
    def __init__(self, guess, code):
        """The class constructor.
        
        Args:
            self (Turn): an instance of Turn.
        """
        self._guess = guess
        self._code = code
        


    def get_guess(self):
        """Returns the guess to compare the code to 

        Args:
            self (Turn): an instance of Turn.
        """

        return self._guess

    def get_hint(self):
        """Generates a hint based on the given code and guess.

        Args:
            self (Turn): An instance of Turn.

        Returns:
            string: A hint in the form [xxxx]
        """ 
        hint = ''
        for index, letter in enumerate(self._guess):
            if self._code[index] == letter:
                hint += "x"
            elif letter in self._code:
                hint += "o"
            else:
                hint += "*"
        return hint


