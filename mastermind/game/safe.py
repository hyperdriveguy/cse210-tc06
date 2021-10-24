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
            _players (list): list of players
            _player_items (compound list): holds code, current guess, and hint for each player
       
       """

    def __init__(self):
        self._code = ''
        self._guess = '----'
        self._hint = '****'
        

    def generate_code(self, hex_code=False):
        if hex_code:
            self._code = str(hex(random.randint(0, int(0xffff))))[2:].upper()
        else:
            self._code = str(random.randint(0, 9999))
        while len(self._code) < 4:
            self._code = '0' + self._code
        print(self._code)

    def get_code(self):
        return self._code

    def apply_turn(self, turn):
        """
        Args:
            turn (Turn): an instance of Turn
        """
        self._guess = turn.get_guess()
        self._hint = turn.get_hint()

    def is_correct(self):
        return (self._guess == self._code)
