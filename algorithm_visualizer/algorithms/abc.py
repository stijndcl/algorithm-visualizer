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
    def run(self):
        """Start running this algorithm
        In order to pause to render the current state, and check for keyboard events,
        the algorithm should yield whenever desired
        """

    @abstractmethod
    def reset_state(self):
        """Reset state of the data stored in the algorithm
        This method is called to re-run the algorithm again on new data, so an implementation
        should preferably randomize the state
        """

    def process_inputs(self):
        """Process keyboard inputs during execution of the algorithm"""
        # pylint: disable=R0801 # The handling of inputs can't really be moved away because
        # that part starts the algorithm itself
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key in (pg.K_ESCAPE, event.key == pg.K_q):
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_SPACE:
                    self.paused = not self.paused

                    if self.paused:
                        raise HaltingException
