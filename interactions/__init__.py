"""CLImate: Interactions package
Classes which implement various interactions with the user via command line

YesNo: prompts the user with a yes or no question
Selector: prompts the user with a list of options from which they may choose a specified number

Created by: Aaron Goidel
"""

from .interaction import Interaction
from .yes_no import YesNo
from .selector import Selector
