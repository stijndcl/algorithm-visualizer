import math
from abc import ABC

import pygame as pg

from algorithm_visualizer.algorithms import Algorithm
from algorithm_visualizer.graphics import Renderer


class ListSortingAlgorithm(Algorithm, ABC):
    """Base class for list sorting algorithms, which abstracts some things away"""

    data: list[int]
    greatest: int

    rectangle_colour: pg.Color = pg.Color(255, 255, 255)
    current_rectangle_colour: pg.Color = pg.Color(255, 0, 0)

    current_index: int = -1

    def __init__(self, data: list[int]):
        self.data = data
        self.greatest = max(self.data)
        self.reset_state()

    def render_current_state(self, renderer: Renderer):
        renderer.fill_background()

        rect_width = renderer.width // len(self.data)
        height_factor = renderer.height / self.greatest

        # Draw a rectangle for every data point
        for i, data_point in enumerate(self.data):
            if i == self.current_index:
                colour = self.current_rectangle_colour
            else:
                colour = self.rectangle_colour

            bar_height = math.ceil(data_point * height_factor)

            renderer.draw_rectangle(i * rect_width, renderer.height - bar_height, rect_width, bar_height, colour)

        pg.display.update()
