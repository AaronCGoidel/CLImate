from sys import stdin, stdout

from .interaction import Interaction
from styler import Styler


s = Styler()


class UserInput(Interaction):
    """
    User input class
    """
    header_template = "{prompt_string}\n"
    option_template = "{cursor} "

    def __init__(self, prompt_string, cursor = ">"):
        """
        Args:
            prompt (str): The text with which the user will be prompted
        """
        self.cursor = cursor
        self.prompt_string = prompt_string

    def show_prompt(self):
        """Displays the prompt to the user
        """
        stdout.write(
            self.header_template.format(
                prompt_string=self.prompt_string
            )
        )
        stdout.flush()
        # stdout.write("{} ".format(self.prompt))
        stdout.write(self.option_template.format(cursor=self.cursor))
        stdout.flush()
    
    # TODO
    def input_validation(self):
        """
        """
        pass

    def show_result(self, value):
        """Prints the result back to the user

        Args:
            value (str): data to be written
        """
        stdout.write(value)
        stdout.flush()
        
    # might add a way to change the confirm message, confirm_message="\nConfirm your input please!\n"
    def confirm_input(self):
        """Give the user the option to confirm his input 
            EX: Enter email:
                > example@example.com
                confirm or change your email:
                > example@example.com
        """
        # if self.confirm is True:
        self.input_to_confirm = self.user_input

        stdout.write("\nConfirm your input please!\n")
        stdout.flush()
        self.prompt_string = ''

        if self.input_to_confirm == self.prompt_user():
            self.flag = s.apply(u"\N{check mark}", s.colors.green)
            stdout.write('{} They match'.format(self.flag))
            stdout.flush()
        else:
            self.flag = s.apply("x", s.colors.red)
            stdout.write('{} Oups input doesn\'t match!'.format(self.flag))
            stdout.flush()

    def prompt_user(self):
        self.show_prompt()      # display prompt
        self.user_input = stdin.readline().strip()
        return self.user_input
