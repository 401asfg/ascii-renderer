from typing import List

from src.content import EMPTY_SPACE, NEW_LINE
from src.model.sprite import Sprite


class Canvas:
    """
    A grid onto which sprites can be drawn
    """

    _width: int
    _height: int
    _grid: str

    def __init__(self, width: int, height: int):
        """
        Initializes the class; the entire canvas is just empty space

        :param width: The width of the canvas
        :param height: The height of the canvas
        :raise ValueError: If the width or height < 0
        """
        if width < 0 or height < 0:
            raise ValueError(
                f'Attempted to create a canvas with the following dimensions: {width}x{height}'
            )

        self._width = width
        self._height = height
        self.clear()

    def clear(self):
        """
        Clear all sprites from the canvas so that the entire canvas is just empty space
        """
        self._grid = EMPTY_SPACE * self.width * self.height

    def draw(self, sprite: Sprite, x: int, y: int):
        """
        Draws the given sprite onto the canvas at the given x and y coordinates

        :param sprite: The sprite to draw
        :param x: The x coordinate of the canvas to draw the sprite at
        :param y: The y coordinate of the canvas to draw the sprite at

        :raise ValueError: If x is less than 0 or >= the canvas' width, or y is less than 0 or >= the canvas' height
        """
        if not self.in_frame(x, y):
            raise ValueError("Attempted to draw a sprite outside of the canvas")

        index = self._get_index(x, y)
        self._grid = self._grid[:index] + str(sprite) + self._grid[index + 1:]

    def render(self) -> str:
        """
        Renders the canvas

        :return: The sprite grid as a single string, with each row as a new line
        """
        render = ""

        for i in range(self.height):
            index_start = i * self.width
            render += self._grid[index_start:index_start + self.width] + NEW_LINE

        return render

    def in_frame(self, x: int, y: int) -> bool:
        """
        :param x: The x coordinate to check that it is inside the canvas' frame
        :param y: The y coordinate to check that it is inside the canvas' frame
        :return: True if the given x is >= 0 and < width and y is >= 0 and < height
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def __str__(self) -> str:
        """
        :return: A string representing the current contents of the canvas with no formatting
        """
        return self._grid

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def _get_index(self, x: int, y: int) -> int:
        """
        :param x: The x coordinate in the canvas
        :param y: The y coordinate in the canvas
        :return: The index of a sprite in the frame that has the given coordinates
        """
        return x + (y * self.width)
