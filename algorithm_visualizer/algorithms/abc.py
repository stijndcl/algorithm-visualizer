import sys
from abc import ABC, abstractmethod

import pygame as pg

from algorithm_visualizer.exceptions import HaltingException
from algorithm_visualizer.graphics import Renderer


class Algorithm(ABC):
    """Abstract class for algorithms that can be visualized"""

    paused: bool = False

    @abstractmethod
    def render_current_state(self, renderer: Renderer):
        """Render the current state of the algorithm"""

    @abstractmethod
    def start(self, renderer: Renderer):
        """Start running this algorithm"""

    @abstractmethod
    def reset_state(self):
        """Reset state of the data stored in the algorithm
        This method is called to re-run the algorithm again on new data, so an implementation
        should preferably randomize the state
        """

    def process_inputs(self):
        """Process keyboard inputs during execution of the algorithm"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_SPACE:
                    self.paused = not self.paused

                    if self.paused:
                        raise HaltingException
