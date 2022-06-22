from algorithm_visualizer.algorithms.presets import RandomSort
from algorithm_visualizer.visualizer import Visualizer


if __name__ == "__main__":
    visualizer = Visualizer(RandomSort(list(range(1, 100))))
    visualizer.game_loop()
