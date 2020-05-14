import pygame as pg


def main(args):
    try:
        gamemain(args)
    except KeyboardInterrupt:
        print('Keyboard Interrupt...')
        print('Exiting')

def gamemain(args):

    from .game import Game
    if len(args)>1 and args[1]=="ai":
        Game().mainloop("ai")
    else:
        Game().mainloop("manual")
