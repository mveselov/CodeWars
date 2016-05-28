import unittest

from katas.beta.chessboard import chessboard


class ChessboardTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(chessboard('2 2'), '*.\n.*')

    def test_equal_2(self):
        self.assertEqual(chessboard('5 2'), '*.\n.*\n*.\n.*\n*.')

    def test_equal_3(self):
        self.assertEqual(chessboard('8 8'),
                         '*.*.*.*.\n.*.*.*.*\n*.*.*.*.\n.*.*.*.*\n'
                         '*.*.*.*.\n.*.*.*.*\n*.*.*.*.\n.*.*.*.*')


if __name__ == '__main__':
    unittest.main()
