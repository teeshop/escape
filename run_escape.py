import escape
import logging, coloredlogs

if __name__ == '__main__':
    coloredlogs.install(level='DEBUG')
    game = escape.Game()
    game.run()