from escape.gamestate import *
import logging


class Citizen(object):
    def __init__(self, name):
        self.__name = name;

    def do_your_turn(self, state: GameState):
        event: Event = state.draw_event()
        logging.info("drawn event card: %s" % event.title)

    @property
    def name(self):
        return self.__name