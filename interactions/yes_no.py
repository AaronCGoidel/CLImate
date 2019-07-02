from sys import stdin, stdout

from .interaction import Interaction
from styler import Styler

s = Styler()


class YesNo(Interaction):
    """Presents a Yes or No question to the user in the following format.
    [!] Question goes here [y/n]: 

    User input of 'y' will lead to a truthy response, while 'n' will be falsey.
    If no input is given (i.e. the user simply hits return) the default truthiness will be given
    """

    def __init__(self, prompt, default="y"):
        """Constructor for YenNo interaction
        
        Args:
            prompt (str): The question to display to the user.
            default (str, optional): What value to assume if user gives no input. Defaults to "y".
        """
        self.flag = s.apply("!", s.colors.yellow)  # default flag is a yellow bang, [!]

        self.options = ["y", "n"]  # this is a yes or no question
        self.default = True if default == "y" else False  # set default value

        Interaction.__init__(self, prompt, self.options)  # super constructor

    def show_prompt(self):
        """Displays the prompt to the user
        """
        # copy the list of options so we can format them without getting in the way of input validation
        options = self.options[:]
        if self.default:  # if the default is true, make the y option capital
            options[0] = "Y"
        else:  # if the default return is false, capitalize the n option
            options[1] = "N"

        options[0] = s.apply(options[0], s.colors.green)  # display y as green
        options[1] = s.apply(options[1], s.colors.red)  # display n as red

        display_options = "[{}/{}]".format(*options)  # format [y/n]
        stdout.write(
            "[{}] {} {}: ".format(self.flag, self.prompt, display_options)
        )  # print formatted prompt
        stdout.flush()

    def validate(self, to_check):
        """Checks if the input was expected
        
        Args:
            to_check (str): The value inputted by the user
        
        Returns:
            bool: Wether or not the input was acceptable
        """
        return (to_check.lower() in self.options) or (to_check == "")

    def show_result(self, value):
        """Goes back in the terminal and replaces the prompt and answer with a neatly formatted result
        """
        CURSOR_UP = "\x1b[1A"
        DELETE = "\x1b[2K"

        # Delete last line of output
        stdout.write(CURSOR_UP)
        stdout.write(DELETE)

        # Write out the flag (which is the choice the user made) and the prompt
        stdout.write("[{}] {}\n".format(self.flag, self.prompt))
        stdout.flush()

    def translate(self, raw):
        """Takes in the raw output from the user and translates it into a more useful form
        
        Args:
            raw (str): The value recieved from stdin
                       we know it to be either 'y', 'n', or ''
        
        Returns:
            bool: The boolean decision based on user input
                  True: if the user said 'y' or if default is True and user said nothing
                  False: if the user said 'n' or if default value is used and is set to False
        """
        if raw == "":  # if the input was just enter, return default
            value = self.default
        elif raw.lower() == "y":  # user said yes
            value = True
        elif raw.lower() == "n":  # user said no
            value = False
        if value:
            self.flag = s.apply(
                u"\N{check mark}", s.colors.green
            )  # set the flag to a green check
        else:
            self.flag = s.apply("x", s.colors.red)  # set the flag to a red x
        return value
