import unittest

from katas.beta.easy_kata import print_x


class PrintXTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(print_x(1), 1)

    def test_equals_2(self):
        self.assertEqual(print_x('x'), 'x')
