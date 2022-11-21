import unittest

from ascii_renderer.text import Text
from ascii_renderer.sprite import Sprite


class TestText(unittest.TestCase):
    string = "abcde abcde \n xxxx\n\ny y y y y \n\n jjjj\n\n\n\nx\n \n\n"
    text: Text

    def setUp(self) -> None:
        self.text = Text(self.string)
    
    def test_init(self):
        self.assertEqual(self.string, self.text.string)

    def test_to_sprite_grid(self):
        self.assertEqual(
            [[Sprite('a'),
              Sprite('b'),
              Sprite('c'),
              Sprite('d'),
              Sprite('e'),
              Sprite(' '),
              Sprite('a'),
              Sprite('b'),
              Sprite('c'),
              Sprite('d'),
              Sprite('e'),
              Sprite(' ')],
             [Sprite(' '),
              Sprite('x'),
              Sprite('x'),
              Sprite('x'),
              Sprite('x')],
             [],
             [Sprite('y'),
              Sprite(' '),
              Sprite('y'),
              Sprite(' '),
              Sprite('y'),
              Sprite(' '),
              Sprite('y'),
              Sprite(' '),
              Sprite('y'),
              Sprite(' ')],
             [],
             [Sprite(' '),
              Sprite('j'),
              Sprite('j'),
              Sprite('j'),
              Sprite('j')],
             [],
             [],
             [],
             [Sprite('x')],
             [Sprite(' ')],
             []],
            self.text.to_sprite_grid()
        )
