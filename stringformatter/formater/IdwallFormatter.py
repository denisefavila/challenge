from formater.StringFormatter import StringFormatter
import textwrap
import re


class IdwallFormatter(StringFormatter):
    def __init__(self, string, limit, justify):
        super().__init__(string=string,
                         limit=limit,
                         justify=justify)

    @staticmethod
    def _items_len(l):
        return sum([len(x) for x in l])

    def _align_string(self, line):
        items = line.split()

        # add required space to each words, exclude last item
        for i in range(len(items) - 1):
            items[i] += ' '

        # number of spaces to add
        left_count = self.limit - self._items_len(items)
        while left_count > 0 and len(items) > 1:
            for i in range(len(items) - 1):
                items[i] += ' '
                left_count -= 1
                if left_count < 1:
                    break

        res = ''.join(items)
        return res

    def format(self):
        wrapper = textwrap.TextWrapper()
        wrapper.width = self.limit

        splitted_string = wrapper.wrap(self.string)

        if not self.justify:
            return "\n".join(splitted_string)

        else:
            wrapped = list()
            while len(splitted_string) > 0:
                line = splitted_string.pop(0)
                aligned = self._align_string(line=line)
                wrapped.append(aligned)

            return "\n".join(wrapped)
