from .message import Message
from styler import Styler

# In order to solve issue #2
s = Styler()


class LoadingSpinner(Message):
    """
    A loading spinner to add to message so that the user knows he has to wait.

    Parameters:
    -----------
    tag (tags): The tage of the message to use
    info (str): The info to print
    spinner (str): The type of spinner. Use one of ('bar', 'dot', 'equal')
    """

    def __init__(self, tag, info, spinner='bar'):
        self.text = info
        Message.__init__(self, tag, info, "\r")
        if spinner == 'bar':
            self.spinner = ['/', '-', '\\', '|']
        elif spinner == 'dot':
            self.spinner = ['   ', '.  ', '.. ', '...', ' ..', '  .']
        elif spinner == 'equal':
            self.spinner = [
                '[   ]', '[=  ]', '[== ]', '[===]', '[ ==]', '[  =]'
            ]
        else:
            raise ValueError("'spinner' can't be {}.".format(spinner))
        self.count = 0
        self.spinner_length = len(self.spinner)
        self.spinner_status = self.spinner[self.count % self.spinner_length]
        self.finished = False

    def display(self):
        """ Display the LoadingSpinner message"""
        self.info = self.text + " " + self.spinner_status
        Message.display(self)

    def increment(self, stop=False):
        """
        Increment the LoadingSpinner object, and stop displaying the spinner
        if the process is over.
        """
        if stop:
            self.finished = True
        if self.finished:
            self.end = "\n"
            self.spinner_status = " " * len(self.spinner[0])
        else:
            self.count += 1
            self.spinner_status = self.spinner[self.count %
                                               self.spinner_length]
        self.display()
