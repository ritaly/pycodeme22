import unittest
from fields import square_area, rectangle_area, triangle_area


class FieldsTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 50
        self.b = 60

    def test_square_area_with_correct_values(self):
        self.assertEqual(square_area(self.a), 2500)

    def test_rectangle_area_with_correct_values(self):
        result = rectangle_area(self.a, self.b)
        self.assertEqual(result, 3000)

    def test_triangle_area_with_correct_values(self):
        result = triangle_area(self.a, self.b)
        self.assertEqual(result, 1500)

    def tearDown(self):
        del self.a
        del self.b


if __name__ == '__main__':
    unittest.main()
