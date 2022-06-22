import random

from algorithm_visualizer.algorithms.presets.sorting.abc_list import ListSortingAlgorithm
from algorithm_visualizer.graphics import Renderer


class RandomSort(ListSortingAlgorithm):
    """Randomize the list until it's sorted"""

    def run(self):
        while self.data != sorted(self.data):
            random.shuffle(self.data)
            yield
