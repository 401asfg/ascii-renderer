from dataclasses import dataclass
from typing import List, Tuple
from ascii_renderer.renderable import Renderable
from ascii_renderer.sprite import Sprite


class Text:
    """
    A set of sprites
    """

    _string: str

    def __init__(self, string: str):
        """
        Initializes the class

        :param string: The source of the text's sprites' characters
        """
        self._string = string

    def to_sprite_grid(self) -> List[List[Sprite]]:
        """
        :return: A grid of the sprites that represent each of the characters of the text
        """
        lines = self.string.splitlines()
        return [[Sprite(char) for char in line]
                for line in lines]

    @property
    def string(self) -> str:
        return self._string
