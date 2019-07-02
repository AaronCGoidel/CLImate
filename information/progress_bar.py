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

    def format_percent(self):
        percent = "{:.1f}%".format((self.completed / self.total) * 100)
        if self.completed >= self.total:
            percent = s.apply(percent, s.colors.green)
        return percent

    def increment(self, step=1):
        self.completed += step
        if self.completed >= self.total:
            self.end = "\n"
        self.display()
