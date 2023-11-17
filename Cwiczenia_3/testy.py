import unittest
from Vector2d import Vector2d
from OptionsParser import OptionsParser
from MoveDirection import MoveDirection

class TestVector2d(unittest.TestCase):
    def test_precedes(self):
        v1 = Vector2d(1, 2)
        v2 = Vector2d(3, 4)
        self.assertTrue(v1.precedes(v2))

    def test_follows(self):
        v1 = Vector2d(1, 2)
        v2 = Vector2d(3, 4)
        self.assertTrue(v2.follows(v1))

    def test_add(self):
        v1 = Vector2d(1, 2)
        v2 = Vector2d(3, 4)
        result = v1.add(v2)
        self.assertEqual(result.get_x(), 4)
        self.assertEqual(result.get_y(), 6)

    def test_subtract(self):
        v1 = Vector2d(1, 2)
        v2 = Vector2d(3, 4)
        result = v2.subtract(v1)
        self.assertEqual(result.get_x(), 2)
        self.assertEqual(result.get_y(), 2)

    def test_upperRight(self):
        v1 = Vector2d(1, 2)
        v2 = Vector2d(3, 4)
        result = v1.upperRight(v2)
        self.assertEqual(result.get_x(), 3)
        self.assertEqual(result.get_y(), 4)

    def test_lowerLeft(self):
        v1 = Vector2d(1, 2)
        v2 = Vector2d(3, 4)
        result = v1.lowerLeft(v2)
        self.assertEqual(result.get_x(), 1)
        self.assertEqual(result.get_y(), 2)

    def test_opposite(self):
        v1 = Vector2d(1, 2)
        result = v1.opposite()
        self.assertEqual(result.get_x(), -1)
        self.assertEqual(result.get_y(), -2)

    def test_eq(self):
        v1 = Vector2d(1, 2)
        v2 = Vector2d(1, 2)
        self.assertEqual(v1, v2)

class TestOptionsParser(unittest.TestCase):
    def test_parse_options(self):
        options = ["f", "b", "l", "r"]
        parsed_options = OptionsParser.parse_options(options)
        expected_parsed_options = [MoveDirection.FORWARD, MoveDirection.BACKWARD, MoveDirection.LEFT, MoveDirection.RIGHT]
        self.assertEqual(parsed_options, expected_parsed_options)

if __name__ == '__main__':
    unittest.main()
