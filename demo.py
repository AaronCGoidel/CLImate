from interactions import *
from information import *
from styler import Styler

import time

s = Styler()

Header("CLImate Demo").display()
time.sleep(0.5)
Message(Message.tags.info, "Welcome to the CLImate component demo").display()
print()
time.sleep(2)

Header("Message Demo", align="left", pattern_color=s.colors.purple).display()
time.sleep(0.5)
Message(
    Message.tags.info,
    "{} messages are all tagged to help organize output".format(
        s.apply("CLImate", s.mods.bold, s.colors.pink)
    ),
).display()
time.sleep(0.5)
Message(Message.tags.info, "Let's take a look at them").display()
time.sleep(4.5)
print()

Message(Message.tags.start, "Some process").display()
time.sleep(1)
Message(Message.tags.info, "Here, let's look at how far along we are").display()
time.sleep(0.5)
p = ProgressBar(70)
p.display()
for i in range(70):
    p.increment()
    time.sleep(0.1)
Message(Message.tags.done, "Some process").display()
time.sleep(2)
Message(Message.tags.info, "There are also issue tags").display()
time.sleep(1.2)
Message(Message.tags.error, "Something went wrong").display()
time.sleep(1.5)
Message(Message.tags.warn, "Something went kinda wrong").display()
time.sleep(2)
print()

Header("Interaction Demo", align="left", pattern_color=s.colors.blue).display()
time.sleep(0.5)
Message(
    Message.tags.info,
    "{} offers user interaction components as well".format(
        s.apply("CLImate", s.mods.bold, s.colors.pink)
    ),
).display()
time.sleep(2.5)
print()

s = Selector(
    "Pick some options",
    ["thing", "other thing", "yet another thing", "item", "the last thing"],
    2,
)

s.prompt_user()
time.sleep(0.3)

YesNo("Did you like this demo?").prompt_user()
time.sleep(0.3)
YesNo("Is love a fruit?", default="n").prompt_user()

