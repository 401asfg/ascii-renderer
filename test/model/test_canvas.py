import unittest
from typing import List

from src.content import EMPTY_SPACE, NEW_LINE
from src.model.canvas import Canvas
from src.model.sprite import Sprite


class TestCanvas(unittest.TestCase):
    WIDTH = 10
    HEIGHT = 4

    canvas: Canvas
    contents: List[List[str]]

    def setUp(self) -> None:
        self.canvas = Canvas(self.WIDTH, self.HEIGHT)
        self.contents = [[EMPTY_SPACE for i in range(self.WIDTH)] for j in range(self.HEIGHT)]

    def get_content_str(self):
        content_str = ""

        for content in self.contents:
            for char in content:
                content_str += char

        return content_str

    def test_init(self):
        self.assertEqual(self.WIDTH, self.canvas.width)
        self.assertEqual(self.HEIGHT, self.canvas.height)
        self.assertEqual(self.get_content_str(), str(self.canvas))

        def assert_fail(width: int, height: int):
            try:
                Canvas(width, height)
                self.fail()
            except ValueError:
                pass

        assert_fail(0, -1)
        assert_fail(-1, 0)
        assert_fail(-1, -1)
        assert_fail(-1, 1)
        assert_fail(1, -1)

    def test_clear(self):
        self.assertEqual(self.WIDTH, self.canvas.width)
        self.assertEqual(self.HEIGHT, self.canvas.height)
        self.assertEqual(EMPTY_SPACE * self.WIDTH * self.HEIGHT, str(self.canvas))

    def test_in_frame(self):
        def assert_in_frame(x: int, y: int):
            self.assertTrue(self.canvas.in_frame(x, y))

        def assert_not_in_frame(x: int, y: int):
            self.assertFalse(self.canvas.in_frame(x, y))

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
                self.canvas.draw(Sprite('x'), x, y)
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
            sprite = Sprite(sprite_str)

            self.contents[y][x] = str(sprite)
            self.canvas.draw(sprite, x, y)

            content_str = self.get_content_str()
            canvas_content_str = str(self.canvas)

            self.assertEqual(len(content_str), len(canvas_content_str))
            self.assertEqual(content_str, canvas_content_str)

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

    def test_render(self):
        expected_render = ""

        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                char = str(x * y)[:1]
                self.canvas.draw(Sprite(char), x, y)
                expected_render += char
            expected_render += NEW_LINE

        self.assertEqual(expected_render, self.canvas.render())


if __name__ == '__main__':
    unittest.main()
