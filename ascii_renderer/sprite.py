from dataclasses import dataclass
from ascii_renderer.renderable import Renderable


@dataclass
class Sprite(Renderable):
    """
    A single, renderable ascii character
    """

    _char: str

    def __init__(self, char: str):
        """
        Initializes the class

        :param char: The ascii character that the sprite represents
        :raise ValueError: If the given char has a length that isn't equal to 1
        """
        if len(char) != 1:
            raise ValueError("Tried to create a sprite with multiple characters")

        self._char = char

    def render(self) -> str:
        return self.char
    
    @property
    def char(self) -> str:
        return self._char
