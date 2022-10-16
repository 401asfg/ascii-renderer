import unittest

from src.model.sprite import Sprite


class TestSprite(unittest.TestCase):
    def test_init(self):
        def assert_init(character: str):
            self.assertEqual(character, str(Sprite(character)))

        def assert_fail(character: str):
            try:
                Sprite(character)
                self.fail()
            except ValueError:
                pass

        assert_init('a')
        assert_init('b')
        assert_init('c')

        assert_fail('')
        assert_fail('aaa')
        assert_fail('bb')
        assert_fail('ccccccc')

    def test_dict(self):
        sprite_a = Sprite('x')
        sprite_b = Sprite('x')
        sprite_other = Sprite('a')

        self.assertTrue(sprite_a == sprite_a)
        self.assertTrue(sprite_a == sprite_b)
        self.assertFalse(sprite_a == sprite_other)
        self.assertFalse(sprite_b == sprite_other)


if __name__ == '__main__':
    unittest.main()
