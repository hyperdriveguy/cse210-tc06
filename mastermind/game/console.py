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
        return input(prompt.title())

    def get_num_input(self, prompt, error_msg):
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.
            error_msg (string): The message to display if user enters invalid inputs

        Returns:
            integer: The user's input as an integer.
        """
        while not prompt.isdigit() and prompt != 4:
            print()
            print(error_msg)
            print()
            prompt = int(input(prompt))
        
        else:
            prompt = int(input(prompt))
        
        return prompt
        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """
        print(text)