class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
     
    def get_str_input(self, prompt):
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        return input(prompt).lower()

    def get_guess_input(self, prompt, hex_code=False):
        """Gets numerical input for the user guessfrom the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.
            hex (bool, optional): Flag whether to accept hexadecimal input.

        Returns:
            str: The user's input as an integer or hex formatted to a string.
        """
        if hex_code:
            highest = '9 and a through f are'
        else:
            highest = '9 is'
        while True:
            raw_str = input(prompt)
            try:
                if len(raw_str) < 4:
                    raise ValueError('Value below minimum number of allowed digits.')
                if hex_code:
                    num = int('0x' + raw_str, 16)
                else:
                    num = int(raw_str)
                if (not hex_code and num > 9999) or (hex_code and num > 0xffff):
                    raise ValueError('Value exceeds number of allowed digits.')
                return raw_str.upper()
            except ValueError:
                self.write(f'Invalid combo. Only 4 digits of 0 through {highest} valid.')


    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)