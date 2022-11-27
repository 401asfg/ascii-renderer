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
    _sprite_grid: List[List[Sprite]]

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
        self._sprite_grid = [[self.empty_space_sprite for _ in range(self.width)] for _ in range(self.height)]

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

        self._sprite_grid[y][x] = sprite

    def overlay(self, base: 'Screen'):
        """
        Draw this screen on top of the given base; The top left corner of this screen is drawn in the top left corner
        of the base; Doesn't draw sprites that can't fit on the base; Doesn't draw sprites if they are empty space

        :param base: The base that has this screen drawn on top of it
        """

        def is_not_empty_space(x, y):
            sprite = self._sprite_grid[y][x]
            return sprite != self.empty_space_sprite

        def draw(x, y):
            sprite = self._sprite_grid[y][x]
            base.draw(sprite, x, y)

        min_width = min(self.width, base.width)
        min_height = min(self.height, base.height)

        [draw(x, y)
         for y in range(min_height)
         for x in range(min_width)
         if is_not_empty_space(x, y)]

    def render(self) -> str:
        """
        :return: The contents of the screen as a single string, with each row as a new line
        """
        render = ""

        for y in range(self.height):
            row = self._sprite_grid[y]

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
        return self._sprite_grid == sprite_grid

    @property
    def empty_space_sprite(self) -> Sprite:
        return self._empty_space_sprite

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height
