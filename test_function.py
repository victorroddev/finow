import unittest

from function import function

class TestFunction(unittest.TestCase):
    def test1(self):
        self.assertAlmostEqual(function(1000, 0.40), 400)
        self.assertAlmostEqual(function(500, 0.10), 50)


unittest.main()