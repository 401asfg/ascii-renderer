import unittest

from ascii_renderer.char import Char


class TestChar(unittest.TestCase):
    CHAR_A = 'a'
    CHAR_B = 'b'
    CHAR_C = 'c'

    char_a: Char
    char_b: Char
    char_c: Char

    def setUp(self) -> None:
        self.char_a = Char(self.CHAR_A)
        self.char_b = Char(self.CHAR_B)
        self.char_c = Char(self.CHAR_C)

    def test_new(self):
        self.assertEqual(self.CHAR_A, self.char_a)
        self.assertEqual(self.CHAR_B, self.char_b)
        self.assertEqual(self.CHAR_C, self.char_c)

        def assert_fail(string: str):
            try:
                Char(string)
                self.fail()
            except ValueError:
                pass

        assert_fail('')
        assert_fail('xx')
        assert_fail('abc')
        assert_fail('abcxxxxxx')
        assert_fail('yyyyyyyyyyyyyyyyyyy')


if __name__ == '__main__':
    unittest.main()
