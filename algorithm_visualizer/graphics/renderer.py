import pygame as pg


class Renderer:
    """Class that handles all graphics rendering"""

    background_colour: pg.Color = pg.Color(20, 20, 20)
    screen: pg.surface.Surface

    def __init__(self, screen: pg.surface.Surface):
        self.screen = screen

    @property
    def width(self) -> int:
        """Width of the screen"""
        return self.screen.get_width()

    @property
    def height(self) -> int:
        """Height of the screen"""
        return self.screen.get_height()

    def fill_background(self):
        """Fill the screen with the background colour"""
        self.screen.fill(self.background_colour)

    def draw_rectangle(self, x: int, y: int, width: int, height: int, colour: pg.Color):
        """Draw a rectangle to the screen
        :param x: the x-position of the rectangle
        :param y: the y-position of the rectangle
        :param width: the width of the rectangle
        :param height: the height of the rectangle
        :param colour: the colour of the rectangle
        """
        pg.draw.rect(self.screen, colour, (x, y, width, height))
