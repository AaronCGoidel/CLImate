from .message import Message
from styler import Styler

s = Styler()


class ProgressBar(Message):
    bar = "[{}{}] {}"

    def __init__(self, total, length=30):
        self.length = length
        self.total = total
        self.completed = 0

        Message.__init__(
            self,
            Message.tags.progress,
            self.bar.format("", "-" * length, self.format_percent()),
            "\r",
        )

        self.display()

    def display(self):
        progress = self.length * self.completed // self.total
        fill = "#" * progress
        remainder = "-" * (self.length - progress)

        self.info = self.bar.format(fill, remainder, self.format_percent())
        Message.display(self)

    def is_done(self):
        return self.completed >= self.total

    def format_percent(self):
        percent = "{:.1f}%".format((self.completed / self.total) * 100)
        if self.is_done():
            percent = s.apply(percent, s.colors.green)
        return percent

    def increment(self, step=1):
        self.completed += step
        if self.is_done():
            self.end = "\n"
        self.display()
