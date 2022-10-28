import asyncio
import unittest

from ascii_renderer.char import Char
from ascii_renderer.renderer import Renderer
from ascii_renderer.screen import Screen


class TestRenderer(unittest.TestCase):
    SCREEN_WIDTH = 10
    SCREEN_HEIGHT = 7

    screen: Screen
    renderer: Renderer

    render_output: str

    async def send_to_render_output(self, msg: str):
        self.render_output = msg

    def setUp(self) -> None:
        self.screen = Screen(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.renderer = Renderer(self.send_to_render_output, self.screen)

    def test_init(self):
        self.assertEqual(self.send_to_render_output, self.renderer.send_to_output)
        self.assertEqual(self.screen, self.renderer.screen)

    def test_render(self):
        def assert_render():
            asyncio.run(self.renderer.render())
            self.assertEqual(self.screen.render(), self.render_output)

        assert_render()

        self.screen.draw(Char('a'), 0, 0)

        self.screen.draw(Char('b'),
                         int(self.SCREEN_WIDTH / 2),
                         int(self.SCREEN_HEIGHT / 3))

        self.screen.draw(Char('c'),
                         self.SCREEN_WIDTH - 1,
                         self.SCREEN_HEIGHT - 1)

        assert_render()


if __name__ == '__main__':
    unittest.main()
