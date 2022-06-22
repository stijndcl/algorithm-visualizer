import pygame as pg


class Renderer:
    """Class that handles all graphics rendering"""

    background_colour: pg.Color = pg.Color(20, 20, 20)
    screen: pg.surface.Surface

    def __init__(self, screen: pg.surface.Surface):
        self.screen = screen

    def fill_background(self):
        """Fill the screen with the background colour"""
        self.screen.fill(self.background_colour)
