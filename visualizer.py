from algorithm_visualizer.algorithms.presets import BubbleSort
from algorithm_visualizer.visualizer import Visualizer


if __name__ == "__main__":
    visualizer = Visualizer(BubbleSort(list(range(1, 100))))
    visualizer.game_loop()
