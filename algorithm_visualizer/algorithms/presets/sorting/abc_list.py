from abc import ABC

import pygame as pg

from algorithm_visualizer.algorithms import Algorithm
from algorithm_visualizer.graphics import Renderer


class ListSortingAlgorithm(Algorithm, ABC):
    """Base class for list sorting algorithms, which abstracts some things away"""

    data: list

    def __init__(self, data: list):
        self.data = data

    def render_current_state(self, renderer: Renderer):
        renderer.fill_background()
        pg.display.update()
