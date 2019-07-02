from information import Information
from styler import Styler

s = Styler()


def make_tag(tag_name, color, bold=False):
    raw = "[" + tag_name.upper() + "]"
    if bold:
        return s.apply(raw, color, s.mods.bold)
    else:
        return s.apply(raw, color)


class Message(Information):
    def __init__(self, tag, info, end="\n"):
        self.tag = tag
        self.end = end
        Information.__init__(self, info)

    def display(self):
        print("{} {}".format(self.tag, self.info), end=self.end)

    class tags:
        start = make_tag("starting", s.colors.pink, True)
        done = make_tag("done", s.colors.green, True)
        error = make_tag("error", s.colors.red)
        warn = make_tag("warning", s.colors.yellow)
        info = make_tag("info", s.colors.blue)
        progress = make_tag("progress", s.colors.purple)

