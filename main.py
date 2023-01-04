import pygame as pg
import sys
from settings import *  # import from settings tab in the whole doomgame folder
from map import *
from player import *
from raycasting import *
from object_renderer import *
class Game:
    def __init__(self):
        pg.init()  # pygame modules
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)  # render the set resolution in an instance of a clock class
        self.clock = pg.time.Clock()
        self.delta_time = 1 # the time passed since the last frame
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)


    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')  # display the current FPS

    def draw(self):
        # self.screen.fill('black')  # paint the screen black
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):  # method/loop to check closing the tab with escape key and if said events occur, exiting the application
        for event in pg.event.get():
            if (event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                pg.quite()
                sys.exit()

    def run(self):
        while True:  # loop to constantly update the game (kind of like an event loop)
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()
