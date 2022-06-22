import sys
from typing import Optional

import pygame as pg

from .algorithms import Algorithm
from .exceptions import HaltingException
from .graphics import Renderer


class Visualizer:
    """Main class that handles the game loop"""

    algorithm: Algorithm
    renderer: Renderer

    def __init__(
        self,
        algorithm: Algorithm,
        width: int = 1600,
        height: int = 900,
        renderer: Optional[Renderer] = None,
    ):
        self.algorithm = algorithm
        if renderer is not None:
            self.renderer = renderer
        else:
            # Create a renderer
            surface = pg.display.set_mode((width, height))
            self.renderer = Renderer(surface)

        pg.display.set_caption("Algorithm Visualizer | Stijndcl")
        self.algorithm.render_current_state(self.renderer)

        # Initialize Pygame
        pg.init()

    def game_loop(self):
        """Main loop"""
        while True:
            self.algorithm.render_current_state(self.renderer)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    elif event.key == pg.K_SPACE:
                        try:
                            self.algorithm.paused = False

                            # Algorithm.run() pauses using yield, so it must be called
                            # using a for-loop
                            for _ in self.algorithm.run():
                                self.algorithm.process_inputs()
                                self.algorithm.render_current_state(self.renderer)
                        except HaltingException:
                            # Catch this in case custom implementations don't
                            pass
                    elif event.key == pg.K_r:
                        self.algorithm.reset_state()
                        self.algorithm.render_current_state(self.renderer)
