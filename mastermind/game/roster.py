class Roster:
    """A collection of players. The responsibility of Roster is to keep track of the players.
    
    Stereotype: 
        Structurer/Information Holder

    Attributes:
        _current (integer): The index of the current player.
        _players (list): A list of Player objects.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Roster): an instance of Roster.
        """
        self.current = 0
        self.players = []
        
    def add_player(self, player):
        """Adds the given player to the roster
        
        Args:
            self (Roster): An instance of Roster.
            player (Player): The player object to add.
        """
        if player not in self.players:
            self.players.append(player)

    def get_players(self):
        """Gets the list of players.
        
        Args:
            self (Roster): An instance of Roster.
            
        Returns:
            Players: the list of players
        """
        return self.players

    def get_current(self):
        """Gets the current player object.
        
        Args:
            self (Roster): An instance of Roster.
        
        Returns:
            Player: The current player.
        """
        return self.players[self.current]
    
    def next_player(self):
        """Advances the turn to the next player.
        
        Args:
            self (Roster): An instance of Roster.
        """
        self.current = (self.current + 1) % len(self.players)
   
    def player_turn_to_str(self):
        """"""

        text = '\n------------------------'
        for player in self.get_players():
            last_turn = player.get_turn()
            text += f'\nPlayer {player.get_name()}: {last_turn.get_guess()}, {last_turn.get_hint()}'
        text += '\n------------------------'
        return text    