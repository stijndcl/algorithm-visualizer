from algorithm_visualizer.algorithms.presets.sorting.abc_list import (
    ListSortingAlgorithm,
)


class BubbleSort(ListSortingAlgorithm):
    """Bubble sort"""

    def run(self):
        for i in range(len(self.data)):
            for j in range(len(self.data) - i - 1):
                self.current_index = j
                yield

                # If the next element is bigger, swap
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

                yield

        # Sorting is done, render final state
        # Set current index back to -1 to remove the selection highlight
        self.current_index = -1
