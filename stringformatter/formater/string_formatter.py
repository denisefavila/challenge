
from abc import ABC, abstractmethod


class StringFormatter(ABC):

    def __init__(self, string, limit, justify):
        self.string = string
        self.limit = limit
        self.justify = justify

    @abstractmethod
    def format(self):
        pass
