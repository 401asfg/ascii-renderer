import unittest

from ascii_renderer.sprite import Sprite


class TestSprite(unittest.TestCase):
    CHAR_A = 'a'
    CHAR_B = 'b'
    CHAR_C = 'c'

    sprite_a: Sprite
    sprite_b: Sprite
    sprite_c: Sprite

    def setUp(self) -> None:
        self.sprite_a = Sprite(self.CHAR_A)
        self.sprite_b = Sprite(self.CHAR_B)
        self.sprite_c = Sprite(self.CHAR_C)

    def test_init(self):
        self.assertEqual(self.CHAR_A, self.sprite_a.char)
        self.assertEqual(self.CHAR_B, self.sprite_b.char)
        self.assertEqual(self.CHAR_C, self.sprite_c.char)

        def assert_fail(string: str):
            try:
                Sprite(string)
                self.fail()
            except ValueError:
                pass

        assert_fail('')
        assert_fail('xx')
        assert_fail('abc')
        assert_fail('abcxxxxxx')
        assert_fail('yyyyyyyyyyyyyyyyyyy')

    def test_eq(self):
        self.assertTrue(self.sprite_a == self.sprite_a)
        self.assertTrue(self.sprite_b == self.sprite_b)
        self.assertTrue(self.sprite_c == self.sprite_c)

        self.assertTrue(self.sprite_a == Sprite(self.CHAR_A))
        self.assertTrue(self.sprite_b == Sprite(self.CHAR_B))
        self.assertTrue(self.sprite_c == Sprite(self.CHAR_C))

        self.assertFalse(self.sprite_a == self.sprite_b)
        self.assertFalse(self.sprite_b == self.sprite_a)
        self.assertFalse(self.sprite_c == self.sprite_b)

    def test_render(self):
        self.assertEqual(self.sprite_a.char, self.sprite_a.render())
        self.assertEqual(self.sprite_b.char, self.sprite_b.render())
        self.assertEqual(self.sprite_c.char, self.sprite_c.render())


if __name__ == '__main__':
    unittest.main()
