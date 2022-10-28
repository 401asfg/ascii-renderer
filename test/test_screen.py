import unittest
from typing import List

from ascii_renderer.special_chars import EMPTY_SPACE, NEW_LINE
from ascii_renderer.screen import Screen
from ascii_renderer.char import Char


class TestScreen(unittest.TestCase):
    WIDTH = 10
    HEIGHT = 4

    screen: Screen
    sprite_grid: List[List[Char]]

    def setUp(self) -> None:
        self.screen = Screen(self.WIDTH, self.HEIGHT)
        self.sprite_grid = [[Char(EMPTY_SPACE) for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]

    def assert_matching(self):
        self.assertTrue(self.screen.is_match(self.sprite_grid))

    def test_init(self):
        self.assertEqual(self.WIDTH, self.screen.width)
        self.assertEqual(self.HEIGHT, self.screen.height)
        self.assert_matching()

        def assert_fail(width: int, height: int):
            try:
                Screen(width, height)
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

    def test_draw_fail(self):
        def assert_fail(x: int, y: int):
            try:
                self.screen.draw(Char('x'), x, y)
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

    def test_draw_pass(self):
        def assert_draw(sprite_str: str, x: int, y: int):
            sprite = Char(sprite_str)

            self.sprite_grid[y][x] = sprite
            self.screen.draw(sprite, x, y)

            self.assert_matching()

        assert_draw('a', 0, 0)
        assert_draw('b', int(self.WIDTH / 2), 0)
        assert_draw('c', self.WIDTH - 1, 0)

        assert_draw('d', 0, int(self.HEIGHT / 2))
        assert_draw('e', int(self.WIDTH / 2), int(self.HEIGHT / 2))
        assert_draw('f', self.WIDTH - 1, int(self.HEIGHT / 2))

        assert_draw('g', 0, self.HEIGHT - 1)
        assert_draw('h', int(self.WIDTH / 2), self.HEIGHT - 1)
        assert_draw('i', self.WIDTH - 1, self.HEIGHT - 1)

        assert_draw('b', 0, 0)

    def test_clear(self):
        self.screen.draw(Char('a'), 0, 0)
        self.screen.draw(Char('b'), self.WIDTH - 1, self.HEIGHT - 1)
        self.screen.draw(Char('c'), int(self.WIDTH / 2), int(self.HEIGHT / 2))
        self.screen.draw(Char('d'), int(self.WIDTH / 5), int(self.HEIGHT / 7))
        self.screen.draw(Char('e'), int(self.WIDTH / 4), int(self.HEIGHT / 3))

        self.screen.clear()

        self.assertEqual(self.WIDTH, self.screen.width)
        self.assertEqual(self.HEIGHT, self.screen.height)
        self.assert_matching()

    def test_render(self):
        expected_render = ""

        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                char = str(x * y)[:1]
                self.screen.draw(Char(char), x, y)
                expected_render += char
            expected_render += NEW_LINE

        self.assertEqual(expected_render, self.screen.render())


if __name__ == '__main__':
    unittest.main()
