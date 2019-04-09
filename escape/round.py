from escape.gamestate import *
from escape.citizen import *
from typing import List


class Round(object):
    def __init__(self, state: GameState):
        self.__gamestate = state

    def run(self, citizens: List[Citizen]) -> None:
        self.__gamestate.round += 1

        for citizen in citizens:
            citizen.do_your_turn(self.__gamestate)
            if self.__gamestate.finished:
                return
