from typing import List
from ascii_renderer.renderable import Renderable

from ascii_renderer.sprite import Sprite


class Screen(Renderable):
    """
    A grid onto which sprites can be drawn
    """

    _empty_space_sprite: Sprite
    _width: int
    _height: int
    _grid: List[List[Sprite]]

    def __init__(self, empty_space_sprite: Sprite, width: int, height: int):
        """
        Initializes the class; the entire screen is just empty space

        :param empty_space_sprite: A sprite representing empty space
        :param width: The width of the screen
        :param height: The height of the screen
        :raise ValueError: If the width or height < 0
        """
        if width < 0 or height < 0:
            raise ValueError(f'Attempted to create a screen with the following dimensions: {width}x{height}')

        self._empty_space_sprite = empty_space_sprite
        self._width = width
        self._height = height
        self.clear()

    def clear(self):
        """
        Make the screen composed of only empty space with its assigned width and height
        """
        self._grid = [[self.empty_space_sprite for _ in range(self.width)] for _ in range(self.height)]

    def draw(self, sprite: Sprite, x: int, y: int):
        """
        Draws the given sprite onto the screen at the given x and y coordinates

        :param sprite: The sprite to draw
        :param x: The x coordinate of the screen to draw the sprite at
        :param y: The y coordinate of the screen to draw the sprite at
        :raise ValueError: If x is less than 0 or >= the screen's width, or y is less than 0 or >= the screen's height
        """
        if not self.in_frame(x, y):
            raise ValueError("Attempted to draw a sprite outside of the screen")

        self._grid[y][x] = sprite

    def render(self) -> str:
        """
        :return: The contents of the screen as a single string, with each row as a new line
        """
        render = ""

        for y in range(self.height):
            row = self._grid[y]

            for x in range(self.width):
                sprite = row[x]
                render += sprite.render()

            render += '\n'

        return render

    def in_frame(self, x: int, y: int) -> bool:
        """
        :param x: The x coordinate to check that it is inside the screen's frame
        :param y: The y coordinate to check that it is inside the screen's frame
        :return: True if the given x is >= 0 and < width and y is >= 0 and < height
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def is_match(self, sprite_grid: List[List[Sprite]]) -> bool:
        """
        :param sprite_grid: The sprite grid to compare this screen to
        :return: True if the given sprite_grid matches that of this screen
        """
        return self._grid == sprite_grid

    @property
    def empty_space_sprite(self) -> Sprite:
        return self._empty_space_sprite

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height
