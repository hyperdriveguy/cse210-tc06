from game.safe import Safe
from game.console import Console
from game.turn import Turn
from game.player import Player
from game.roster import Roster

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        safe (Safe): An instance of the class of objects known as Safe.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        guess (Guess): An instance of the class of objects known as Guess.
        roster (Roster): An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._safe = Safe()
        self._console = Console()
        self._keep_playing = True
        self._turn = None
        self._roster = Roster()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _prepare_game(self):
        """Prepares the game before it begins. In this case, that means getting the player names and adding them to the roster.
        
        Args:
            self (Director): An instance of Director.
        """
        for n in range(2):
            name = self._console.get_str_input(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)
        

    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the guess from the current player.

        Args:
            self (Director): An instance of Director.
        """

        #display the game board
        self._console.write(self._safe.turn_to_str())

        # get next player's guess
        player = self._roster.get_current()
        self._console.write(f"{player.get_name()}'s turn:")
        guess = self._console.get_str_input("What is your guess: ")
        turn = Turn(guess, self._safe.get_code())
        player.set_turn(turn)

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the safe with the current guess.

        Args:
            self (Director): An instance of Director.
        """
        player = self._roster.get_current()
        turn = player.get_turn()
        self._safe.apply_turn(turn)


 
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if the guess is correct. 
        If correct, declare the winner.
        If incorrect, give hint and go to next player.

        Args:
            self (Director): An instance of Director.
        """
        if self._safe.is_correct():
            winner = self._roster.get_current()
            name = winner.get_name()
            print(f'\n{name} won!')
        self._roster.next_player()
