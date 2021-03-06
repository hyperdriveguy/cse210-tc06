import random

class Safe:

    """The place where the code is stored. 
       The responsiblity of this class is to generate the code and compare it to the guesses.
       Stores players guess and hint
       
       Stereotype:
            Information Holder

        Attributes:
            _code (string): four-digit code stored as a string
            _guess (string): four-digit guess stored as string
            _hint (string): hint for player stored as a string
       
       """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Safe): an instance of Safe.
        """
        self._code = ''
        self._guess = '----'
        self._hint = '****'
        


    def generate_code(self, hex_code=False):
        """Generates the code. 
        
        Args:
            self (Safe): An instance of Safe
            hex_code (bool): If false, generate code with only numbers
              if true, generate code with letters and numbers
        """    
        if hex_code:
            self._code = str(hex(random.randint(0, int(0xffff))))[2:].upper()
        else:
            self._code = str(random.randint(0, 9999))
        while len(self._code) < 4:
            self._code = '0' + self._code


    def get_code(self):
        """Gets the code.
        
        Args:
            self (Safe): An instance of Safe

        Return (str): Returns the code as a string
        """
        return self._code

    def apply_turn(self, turn):
        """Executes a turn, setting the guess and hint

        Args:
            safe (Safe): an instance of Safe
        """
        self._guess = turn.get_guess()
        self._hint = turn.get_hint()

    def is_correct(self):
        """Determine if the guess matches the code
        
        Args:
            self (Safe): An instance of Safe

        Return (bool): If guess matches code return true 
        """
        return (self._guess == self._code)
