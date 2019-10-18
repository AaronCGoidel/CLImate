from interaction import *
from information import *
from styler import *

import time


class CLI:
    def __init__(self, rest=0):
        self.s = Styler()
        self.rest = rest
        self.bar = None
        self.ops = []

    def header(self, text, rest=self.rest):
        Header(text).display()
        time.sleep(rest)

    def info(self, text, rest=self.rest):
        Message(Message.tags.info, text).display()
        time.sleep(rest)

    def start(self, text, rest=self.rest):
        Message(Message.tags.start, text).display()
        self.ops.append(text)
        time.sleep(rest)

    def end(self, rest=self.rest):
        currentOp = self.ops.pop()
        Message(Message.tags.done, currentOp).display()
        time.sleep(rest)

    def progressBar(self, total=0, step=1):
        if self.bar is None:
            self.bar = ProgressBar(total)
        else:
            self.bar.increment(step)
            if self.bar.is_done():
                self.bar = None
