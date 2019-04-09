from functools import total_ordering
from datetime import *
import logging


@total_ordering
class Event(object):
    def __init__(self, **kwargs):
        self.__title: str = kwargs.get("title")
        self.__description: str = kwargs.get("description")
        self.__date: datetime = kwargs.get("date")

        assert self.__title is not None

    @property
    def date(self) -> datetime:
        return self.__date

    @property
    def title(self) -> str:
        return self.__title

    @property
    def description(self) -> str:
        return self.__description

    def __eq__(self, other) -> bool:
        a = self.date or other.date
        b = other.date or self.date
        return a == b

    def __ne__(self, other) -> bool:
        a = self.date or other.date
        b = other.date or self.date
        return a != b

    def __lt__(self, other):
        if self.date is None and other.date is None:
            return False
        a = self.date or other.date
        b = other.date or self.date
        return a < b

    def __le__(self, other):
        if self.date is None and other.date is None:
            return True
        a = self.date or other.date
        b = other.date or self.date
        return a <= b
