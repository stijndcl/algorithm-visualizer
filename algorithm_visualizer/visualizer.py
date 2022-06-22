import sys
from typing import Optional

import pygame as pg

from .algorithms import Algorithm
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
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    elif event.key == pg.K_SPACE:
                        self.algorithm.start(self.renderer)
                    elif event.key == pg.K_r:
                        self.algorithm.reset_state()
                        self.algorithm.render_current_state(self.renderer)
