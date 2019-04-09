from escape.event import Event
import typing
import random
from datetime import *


class GameState(object):
    def __init__(self):
        self.__round = 0
        self.__pending_events: typing.List[Event] = [
            Event(title="Beispiel1"),
            Event(title="Beispiel2"),
            Event(title="Beispiel3")
        ]
        for _ in range(1,3):
            random.shuffle(self.__pending_events)

        timed_events : typing.List[Event] = [
            Event(date=datetime(day=7, month=10, year=1949),
                  title="Gründung der DDR"),
            Event(date=datetime(day=3, month=10, year=1990),
                  title="Auflösung der DDR"),
            Event(date=datetime(day=13, month=8, year=1961),
                  title="Bau der Berliner Mauer")
        ]

        timed_events.sort()
        min_index = 0
        while len(timed_events) > 0:
            idx = random.randint(min_index, len(self.__pending_events))
            self.__pending_events.insert(idx, timed_events.pop(0))
            min_index = idx + 1
        assert(self.__are_events_sorted())

    def draw_event(self) -> Event:
        assert len(self.__pending_events) > 0
        return self.__pending_events.pop(0)

    @property
    def finished(self) -> bool:
        return len(self.__pending_events) == 0

    @property
    def round(self) -> int:
        return self.__round

    @round.setter
    def round(self, current_round: int):
        if current_round <= self.__round:
            raise ValueError()
        else:
            self.__round = current_round

    def __are_events_sorted(self):
        if len(self.__pending_events) < 2:
            return True
        for idx in range(0, len(self.__pending_events)-2):
            for elem in self.__pending_events[idx+1:]:
                if not self.__pending_events[idx] <= elem:
                    return False
        return True
