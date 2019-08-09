from sys import stdin, stdout


class Interaction:
    """A component which prompts a user and then takes some input
    """

    def __init__(self, prompt, options):
        """
        Args:
            prompt (str): The text with which the user will be prompted
            options (list of str): the choices the user will be presented with
        """
        self.prompt = prompt
        self.options = options

    def show_prompt(self):
        """Displays the prompt to the user
        """
        stdout.write(self.prompt)
        stdout.flush()

    def validate(self, to_check):
        """Checks if the input recieved is valid, i.e. one of the options
        
        Args:
            to_check (str): the input we want to validate is in the set of options
        
        Returns:
            bool: True if to_check is one of the options, else False
        """
        return to_check in self.options

    def translate(self, raw):
        """Takes in the raw input from the prompt and returns a more usable form.
        This particular function just exists to be overridden in a subclass.
        
        Args:
            raw (any): data to be translated
        
        Returns:
            any: the data again
        """
        return raw

    def show_result(self, value):
        """Prints the result back to the user
        
        Args:
            value (str): data to be written
        """
        stdout.write(value)
        stdout.flush()

    def prompt_user(self):
        """Prompts the user with a querry, takes input, and validates it.
        If the input received is valid, the output is displayed and value returned.
        If the input is not valid, the user is prompted again.
        
        Returns:
            [type]: [description]
        """
        self.show_prompt()
        received = stdin.readline().strip()
        if self.validate(received):
            value = self.translate(received)
            self.show_result(value)
            return value
        return self.prompt_user()
