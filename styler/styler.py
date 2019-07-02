class Styler:
    BASE = "\033[{}m"

    class colors:  # a place for all the colors to live
        red = 31
        green = 32
        orange = 33
        blue = 34
        purple = 35
        cyan = 36
        yellow = 93
        light_blue = 94
        pink = 95

    class mods:  # a place for other modifications
        clear = 0
        bold = 1
        underline = 4

    def apply(self, text, *codes):
        """Applies a series of modifiers to a string to change its appearance when printed
        
        Args:
            text (str): The string to which the modifiers will be applied
            *codes (Styler.colors.* or Styler.mods.*): All args after ``text`` will be applied as style
        
        Returns:
            string: The text, modified with the attributes specified

        Example:
            >>> apply("foo", Styler.colors.red, Styler.mods.bold) 
            '\x1b[31;1mfoo\x1b[0m' 
            
            (which, when printed, is "foo" bolded and in red)
        """
        # iterates over the codes passed and adds them to the string
        tags = self.BASE.format(";".join([str(code) for code in codes]))
        # returns the prefix, text, and closing tag
        return tags + text + self.BASE.format(str(self.mods.clear))
