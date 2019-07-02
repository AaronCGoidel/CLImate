from information import Information
from styler import Styler

s = Styler()


class Message(Information):
    def __init__(self, tag, info, end="\n"):
        self.tag = tag
        self.end = end
        Information.__init__(self, info)

    def display(self):
        print("{} {}".format(self.tag, self.info), end=self.end)

    class tags:
        def make_tag(self, tag_name, color, bold=False):
            raw = "[" + tag_name.upper() + "]"
            if bold:
                return s.apply(raw, color, s.mods.bold)
            else:
                return s.apply(raw, color)

        def __init__(self):
            self.start = self.make_tag("starting", s.colors.pink, True)
            self.done = self.make_tag("done", s.colors.green, True)
            self.error = self.make_tag("error", s.colors.red)
            self.warn = self.make_tag("warning", s.colors.yellow)
            self.info = self.make_tag("info", s.colors.blue)
            self.progress = self.make_tag("progress", s.colors.cyan)

