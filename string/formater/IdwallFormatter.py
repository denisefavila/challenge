from string.formater.StringFormatter import StringFormater


class IdwallFormatter(StringFormater):
    def __init__(self, string, limit, justify):
        self.string = string
        self.limit = limit
        self.justify = justify

    def format(self):
        pass
