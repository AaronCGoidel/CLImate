from sys import stdin, stdout

from .interaction import Interaction
from styler import Styler
import sys, tty, termios

s = Styler()


class Selector(Interaction):
    header_template = "[{picked}/{available}] {prompt}:\n"
    option_template = " {cursor} {option}\n"

    def __init__(self, prompt, options, limit=1):
        self.cursor = ">"
        self.cursor_location = 0
        self.prompt = prompt
        self.flag = s.apply("!", s.colors.yellow)
        self.options = options
        self.limit = limit
        self.mask = [False] * len(options)
        self.selected = []

    def limit_reached(self):
        """Checks if the user has reached the maximum number of items they may select
        
        Returns:
            bool: True if the user has selected the max number of items
        """
        if len(self.selected) >= self.limit:
            return True
        return False

    def show_prompt(self):
        stdout.write(
            self.header_template.format(
                picked=len(self.selected), available=self.limit, prompt=self.prompt
            )
        )
        stdout.flush()
        for i, elt in enumerate(self.options):
            # place cursor if this is the current location
            cursor = self.cursor if self.cursor_location == i else " "
            if self.mask[i] == True:  # make option green if selected
                elt = s.apply(elt, s.colors.green)
            stdout.write(self.option_template.format(cursor=cursor, option=elt))

    def get(self):
        """Code for controlling the user's interactions with the prompt
        
        Raises:
            KeyboardInterrupt: this re-implements the ability to us ^C during prompting
        """
        fd = stdin.fileno()
        default = termios.tcgetattr(fd)

        tty.setraw(stdin.fileno())  # set terminal to raw input mode to get bytes

        while True:  # read in until a key is pressed
            char = ord(stdin.read(1))
            if char != "":
                break
        # logic for keyboard interrupt
        if char == 0x03:  # is the input the interrupt code?
            termios.tcsetattr(fd, termios.TCSADRAIN, default)
            raise KeyboardInterrupt
        # logic for when the user hits enter
        elif char == 0x0D or char == 0x0A:  # enter is one of these depending on system
            marked = self.mask[self.cursor_location]

            # toggle the corresponding spot in the selection mask
            self.mask[self.cursor_location] = not self.mask[self.cursor_location]

            current = self.options[self.cursor_location]
            if marked:  # if the item was previously selected
                self.selected = list(
                    filter(lambda item: item != current, self.selected)
                )  # remove item from selecteed
            else:  # if not
                self.selected.append(current)  # add it to the list of selected options
        # logic for arrow keys
        # these keypresses are three bytes long
        # the first byte is an escape character
        elif char == 0x1B:  # check for escape character
            if ord(stdin.read(1)) == 0x5B:  # check for next byte, same for up and down
                last = ord(stdin.read(1))
                if last == 0x42:  # up arrow
                    # adjust the cursor position, wrapping if reached the end
                    self.cursor_location = (self.cursor_location + 1) % len(
                        self.options
                    )
                elif last == 0x41:  # down arrow
                    self.cursor_location = (self.cursor_location - 1) % len(
                        self.options
                    )
        termios.tcsetattr(
            fd, termios.TCSADRAIN, default
        )  # reset the terminal out of raw mode

    def prompt_user(self):
        self.show_prompt()  # display prompt and options

        while not self.limit_reached():  # if the user still needs to select options
            self.get()  # run interaction until the user presses enter
            # update output
            for i in range(len(self.options) + 1):
                stdout.write("\x1b[1A")
                stdout.write("\x1b[2K")
            self.show_prompt()
        # logic after user is done with input
        self.cursor = " "  # get rid of cursor and reprint
        for i in range(len(self.options) + 1):
            stdout.write("\x1b[1A")
            stdout.write("\x1b[2K")
        self.show_prompt()

