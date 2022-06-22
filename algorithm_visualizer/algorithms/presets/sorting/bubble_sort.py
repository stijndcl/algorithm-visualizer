import random

from algorithm_visualizer.algorithms.presets.sorting.abc_list import (
    ListSortingAlgorithm,
)
from algorithm_visualizer.graphics import Renderer


class BubbleSort(ListSortingAlgorithm):
    """Bubble sort"""

    def start(self, renderer: Renderer):
        for i in range(len(self.data)):
            for j in range(len(self.data) - i - 1):
                self.current_index = j
                self.render_current_state(renderer)

                # If the next element is bigger, swap
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

                self.render_current_state(renderer)

        # Sorting is done, render final state
        # Set current index back to -1 to remove the selection highlight
        self.current_index = -1
        self.render_current_state(renderer)

    def reset_state(self):
        random.shuffle(self.data)
