from abc import ABC, abstractmethod


class Renderable(ABC):
    """
    Can be rendered by a renderer
    """

    @abstractmethod
    def render(self) -> str:
        """
        :return: A rendering of this class
        """
