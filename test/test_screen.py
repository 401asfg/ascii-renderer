import unittest
from typing import List

from ascii_renderer.screen import Screen
from ascii_renderer.sprite import Sprite


class TestScreen(unittest.TestCase):
    EMPTY_SPACE_CHAR = ' '
    WIDTH = 10
    HEIGHT = 4

    empty_space_sprite: Sprite
    screen: Screen
    sprite_grid: List[List[Sprite]]

    def set_sprite_grid_empty(self, empty_space_sprite: Sprite, width: int, height: int):
        self.sprite_grid = [[empty_space_sprite for _ in range(width)] for _ in range(height)]

    def setUp(self) -> None:
        self.empty_space_sprite = Sprite(self.EMPTY_SPACE_CHAR)
        self.screen = Screen(self.empty_space_sprite, self.WIDTH, self.HEIGHT)
        self.set_sprite_grid_empty(self.empty_space_sprite, self.WIDTH, self.HEIGHT)

    def assert_matching(self):
        self.assertTrue(self.screen.is_match(self.sprite_grid))

    def test_init(self):
        def assert_init(empty_space_sprite: Sprite, width: int, height: int):
            self.screen = Screen(empty_space_sprite, width, height)
            self.set_sprite_grid_empty(empty_space_sprite, width, height)

            self.assertEqual(empty_space_sprite, self.screen.empty_space_sprite)
            self.assertEqual(width, self.screen.width)
            self.assertEqual(height, self.screen.height)
            self.assert_matching()

        assert_init(self.empty_space_sprite, self.WIDTH, self.HEIGHT)

        assert_init(self.empty_space_sprite, 0, 0)
        assert_init(self.empty_space_sprite, 1, 0)
        assert_init(self.empty_space_sprite, 0, 1)
        assert_init(self.empty_space_sprite, 1, 1)
        assert_init(self.empty_space_sprite, 0, 0)

        assert_init(self.empty_space_sprite, 3, 9)
        assert_init(self.empty_space_sprite, 27, 27)
        assert_init(self.empty_space_sprite, 34, 534)

        assert_init(Sprite('.'), 0, 0)
        assert_init(Sprite('a'), 1, 0)
        assert_init(Sprite('x'), 0, 1)
        assert_init(Sprite('d'), 1, 1)
        assert_init(Sprite('f'), 0, 0)

        assert_init(Sprite('/'), 3, 9)
        assert_init(Sprite(','), 27, 27)
        assert_init(Sprite('_'), 34, 534)

        def assert_fail(width: int, height: int):
            try:
                Screen(Sprite(self.EMPTY_SPACE_CHAR), width, height)
                self.fail()
            except ValueError:
                pass

        assert_fail(0, -1)
        assert_fail(-1, 0)
        assert_fail(-1, -1)
        assert_fail(-1, 1)
        assert_fail(1, -1)

    def test_in_frame(self):
        def assert_in_frame(x: int, y: int):
            self.assertTrue(self.screen.in_frame(x, y))

        def assert_not_in_frame(x: int, y: int):
            self.assertFalse(self.screen.in_frame(x, y))

        assert_in_frame(0, 0)
        assert_in_frame(int(self.WIDTH / 2), 0)
        assert_in_frame(self.WIDTH - 1, 0)

        assert_in_frame(0, int(self.HEIGHT / 2))
        assert_in_frame(int(self.WIDTH / 2), int(self.HEIGHT / 2))
        assert_in_frame(self.WIDTH - 1, int(self.HEIGHT / 2))

        assert_in_frame(0, self.HEIGHT - 1)
        assert_in_frame(int(self.WIDTH / 2), self.HEIGHT - 1)
        assert_in_frame(self.WIDTH - 1, self.HEIGHT - 1)

        assert_not_in_frame(-1, -1)
        assert_not_in_frame(int(self.WIDTH / 2), -1)
        assert_not_in_frame(self.WIDTH + 1, -1)

        assert_not_in_frame(-1, int(self.HEIGHT / 2))
        assert_not_in_frame(self.WIDTH + 1, int(self.HEIGHT / 2))

        assert_not_in_frame(self.WIDTH, 0)
        assert_not_in_frame(self.WIDTH, int(self.HEIGHT / 2))

        assert_not_in_frame(0, self.HEIGHT)
        assert_not_in_frame(int(self.WIDTH / 2), self.HEIGHT)
        assert_not_in_frame(self.WIDTH, self.HEIGHT)

        assert_not_in_frame(-1, self.HEIGHT + 1)
        assert_not_in_frame(int(self.WIDTH / 2), self.HEIGHT + 1)
        assert_not_in_frame(self.WIDTH + 1, self.HEIGHT + 1)

    def test_draw_sprite_fail(self):
        def assert_fail(x: int, y: int):
            try:
                self.screen.draw_sprite(Sprite('x'), x, y)
                self.fail()
            except ValueError:
                pass

        assert_fail(-1, -1)
        assert_fail(int(self.WIDTH / 2), -1)
        assert_fail(self.WIDTH + 1, -1)

        assert_fail(-1, int(self.HEIGHT / 2))
        assert_fail(self.WIDTH + 1, int(self.HEIGHT / 2))

        assert_fail(self.WIDTH, 0)
        assert_fail(self.WIDTH, int(self.HEIGHT / 2))

        assert_fail(0, self.HEIGHT)
        assert_fail(int(self.WIDTH / 2), self.HEIGHT)
        assert_fail(self.WIDTH, self.HEIGHT)

        assert_fail(-1, self.HEIGHT + 1)
        assert_fail(int(self.WIDTH / 2), self.HEIGHT + 1)
        assert_fail(self.WIDTH + 1, self.HEIGHT + 1)

    def test_draw_sprite_pass(self):
        def assert_draw_sprite(sprite_str: str, x: int, y: int):
            sprite = Sprite(sprite_str)

            self.sprite_grid[y][x] = sprite
            self.screen.draw_sprite(sprite, x, y)

            self.assert_matching()

        assert_draw_sprite('a', 0, 0)
        assert_draw_sprite('b', int(self.WIDTH / 2), 0)
        assert_draw_sprite('c', self.WIDTH - 1, 0)

        assert_draw_sprite('d', 0, int(self.HEIGHT / 2))
        assert_draw_sprite('e', int(self.WIDTH / 2), int(self.HEIGHT / 2))
        assert_draw_sprite('f', self.WIDTH - 1, int(self.HEIGHT / 2))

        assert_draw_sprite('g', 0, self.HEIGHT - 1)
        assert_draw_sprite('h', int(self.WIDTH / 2), self.HEIGHT - 1)
        assert_draw_sprite('i', self.WIDTH - 1, self.HEIGHT - 1)

        assert_draw_sprite('b', 0, 0)

    # def test_draw_text_completely_inside(self):
    #     # TODO: write

    # def test_draw_text_top_left_corner(self):
    #     # TODO: write

    # def test_draw_text_outside_top_left(self):
    #     # TODO: write
    
    # def test_draw_text_outside_bottom_right(self):
    #     # TODO: write
    
    # def test_draw_text_indside_offset_top_left(self):
    #     # TODO: write
    
    # def test_draw_text_inside_offset_bottom_right(self):
    #     # TODO: write

    # def test_draw_text_partially_inside_but_inside_is_empty_space_top_left(self):
    #     # TODO: write

    # def test_draw_text_partially_inside_but_inside_is_empty_space_bottom_right(self):
    #     # TODO: write
    
    def test_clear(self):
        self.screen.draw_sprite(Sprite('a'), 0, 0)
        self.screen.draw_sprite(Sprite('b'), self.WIDTH - 1, self.HEIGHT - 1)
        self.screen.draw_sprite(Sprite('c'), int(self.WIDTH / 2), int(self.HEIGHT / 2))
        self.screen.draw_sprite(Sprite('d'), int(self.WIDTH / 5), int(self.HEIGHT / 7))
        self.screen.draw_sprite(Sprite('e'), int(self.WIDTH / 4), int(self.HEIGHT / 3))

        self.screen.clear()

        self.assertEqual(self.WIDTH, self.screen.width)
        self.assertEqual(self.HEIGHT, self.screen.height)
        self.assert_matching()

    def test_render(self):
        expected_render = ""

        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                char = str(x * y)[:1]
                self.screen.draw_sprite(Sprite(char), x, y)
                expected_render += char
            expected_render += '\n'

        self.assertEqual(expected_render, self.screen.render())

    def test_overlay_smaller_empty(self):
        top = Screen(Sprite(self.EMPTY_SPACE_CHAR), 1, 1)
        top.draw_sprite(Sprite(self.EMPTY_SPACE_CHAR), 0, 0)

        self.screen.draw_sprite(Sprite('x'), 0, 0)
        self.sprite_grid[0][0] = Sprite('x')

        top.overlay(self.screen)
        self.assert_matching()

    def test_overlay_smaller_not_empty(self):
        top = Screen(Sprite(self.EMPTY_SPACE_CHAR), int(self.WIDTH / 2), int(self.HEIGHT / 2))

        [top.draw_sprite(Sprite('x'), x, y)
         for x in range(top.width) for y in range(top.height)]

        [self.screen.draw_sprite(Sprite('y'), x, y)
         for x in range(self.screen.width) for y in range(self.screen.height)]
         
        def set_sprite_grid(char, x, y):
            self.sprite_grid[y][x] = Sprite(char)

        [set_sprite_grid('y', x, y)
         for x in range(self.screen.width) for y in range(self.screen.height)]

        [set_sprite_grid('x', x, y)
         for x in range(top.width) for y in range(top.height)]

        top.overlay(self.screen)
        self.assert_matching()

    def test_overlay_smaller_empty(self):
        top = Screen(Sprite(self.EMPTY_SPACE_CHAR), int(self.WIDTH / 2), int(self.HEIGHT / 2))

        [top.draw_sprite(Sprite(self.EMPTY_SPACE_CHAR), x, y)
         for x in range(top.width) for y in range(top.height)]

        [self.screen.draw_sprite(Sprite('y'), x, y)
         for x in range(self.screen.width) for y in range(self.screen.height)]
         
        def set_sprite_grid(char, x, y):
            self.sprite_grid[y][x] = Sprite(char)

        [set_sprite_grid('y', x, y)
         for x in range(self.screen.width) for y in range(self.screen.height)]

        top.overlay(self.screen)
        self.assert_matching()

    def test_overlay_same_size(self):
        top = Screen(Sprite(self.EMPTY_SPACE_CHAR), int(self.WIDTH), int(self.HEIGHT))

        [top.draw_sprite(Sprite('x'), x, y)
         for x in range(int(top.width / 2), top.width)
         for y in range(int(top.height / 2), top.height)]

        [self.screen.draw_sprite(Sprite('y'), x, y)
         for x in range(self.screen.width) for y in range(self.screen.height)]
         
        def set_sprite_grid(char, x, y):
            self.sprite_grid[y][x] = Sprite(char)

        [set_sprite_grid('y', x, y)
         for x in range(self.screen.width) for y in range(self.screen.height)]

        [set_sprite_grid('x', x, y)
         for x in range(int(top.width / 2), top.width)
         for y in range(int(top.height / 2), top.height)]

        top.overlay(self.screen)
        self.assert_matching()

    # def test_overlay_larger_not_empty(self):
    #     # TODO: write

    # def test_overlay_different_empty_spaces(self):
    #     # TODO: write


if __name__ == '__main__':
    unittest.main()
