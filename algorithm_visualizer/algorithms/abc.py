from abc import ABC, abstractmethod

from algorithm_visualizer.graphics import Renderer


class Algorithm(ABC):
    """Abstract class for algorithms that can be visualized"""

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
