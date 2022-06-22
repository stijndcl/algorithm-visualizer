from algorithm_visualizer.algorithms.presets import BubbleSort
from algorithm_visualizer.visualizer import Visualizer


if __name__ == "__main__":
    visualizer = Visualizer(BubbleSort())
    visualizer.game_loop()
