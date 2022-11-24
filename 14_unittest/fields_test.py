import unittest
from fields import square_area


class FieldsTestCase(unittest.TestCase):
    def test_square_area_with_corrent_values(self):
        result_s = square_area(5)
        self.assertEqual(result_s, 25)

    # 2 funkcje testujące trójkąt i prostokąt


if __name__ == '__main__':
    unittest.main()
