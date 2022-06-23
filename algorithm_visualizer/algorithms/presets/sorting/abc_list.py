import math
import random
from abc import ABC

import pygame as pg

from algorithm_visualizer.algorithms import Algorithm
from algorithm_visualizer.graphics import Renderer


class ListSortingAlgorithm(Algorithm, ABC):
    """Base class for list sorting algorithms, which abstracts some things away"""

    data: list[int]

    current_index: int = -1

    rectangle_colour: pg.Color = pg.Color(255, 255, 255)
    highlighted_rectangle_colour: pg.Color = pg.Color(255, 0, 0)

    renderer: Renderer
    bar_width: int
    height_factor: float

    def __init__(self, data: list[int]):
        self.data = data
        self.reset_state()

    def setup(self):
        """Pre-compute the width & scaling factors"""
        self.bar_width = self.renderer.width // len(self.data)
        self.height_factor = self.renderer.height / max(self.data)

    def is_highlighted(self, index: int, value: int) -> bool:
        """Check if the current element should be considered highlighted or not"""
        _ = (index, value)  # Keep Pylint from complaining
        return index == self.current_index

    def get_colour(self, index: int, value: int, highlighted: bool) -> pg.Color:
        """Get the colour to use for rendering of one bar
        This allows you to get funky with the colouring process (eg. creating rainbows)
        """
        _ = (index, value)  # Keep Pylint from complaining
        return self.highlighted_rectangle_colour if highlighted else self.rectangle_colour

    def render_highlighted_data_point(self, index: int, value: int):
        """Render a data point when it is highlighted"""
        self._render_bar(index, value, self.get_colour(index, value, True))

    def render_data_point(self, index: int, value: int):
        """Render a regular data point"""
        self._render_bar(index, value, self.get_colour(index, value, False))

    def _render_bar(self, index: int, value: int, colour: pg.Color):
        """Render a bar"""
        bar_height = math.ceil(value * self.height_factor)
        self.renderer.draw_rectangle(
            index * self.bar_width, self.renderer.height - bar_height, self.bar_width, bar_height, colour
        )

    def render_current_state(self, renderer: Renderer):
        renderer.fill_background()

        # Draw a rectangle for every data point
        for i, data_point in enumerate(self.data):
            if self.is_highlighted(i, data_point):
                self.render_highlighted_data_point(i, data_point)
            else:
                self.render_data_point(i, data_point)

        pg.display.update()

    def reset_state(self):
        random.shuffle(self.data)
