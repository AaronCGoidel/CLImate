from styler import Styler
from .information import Information

s = Styler()


class Header(Information):
    justifies = {"left": "{0} {1}", "right": "{1} {0}", "center": "{1} {0} {1}"}

    def __init__(
        self,
        text,
        width=30,
        align="center",
        char="=",
        pattern_color=s.colors.red,
        text_color=s.mods.clear,
    ):
        self.text = text
        self.width = width
        self.align = align
        self.char = char
        self.pattern_color = pattern_color
        self.text_color = text_color

    def display(self):
        pattern_len = self.width - len(self.text) - 1
        if self.align == "center":
            pattern_len //= 2
        pattern = s.apply(self.char * pattern_len, self.pattern_color, s.mods.bold)
        title = s.apply(self.text, self.text_color, s.mods.bold)

        header = self.justifies[self.align].format(title, pattern)
        print(header)

