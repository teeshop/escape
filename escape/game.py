from escape.citizen import *
from escape.round import *
from typing import List

class Game(object):
    def __init__(self):
        self.__citizens: List[Citizen] = [
            Citizen("Maurer"),
            Citizen("Pfarrer"),
            Citizen("LPG-Vorsitzender"),
            Citizen("Alt-Nazi")
        ]

    def run(self):
        s = GameState()
        while not s.finished:
            r = Round(s)
            r.run(self.__citizens)