import unittest
from geometric_lib.square import area, perimeter

class SquareTestCase(unittest.TestCase):
    """Тесты для функций расчета площади и периметра квадрата."""

    def test_area_positive(self):
        """Тест: положительная длина стороны квадрата."""
        a = 4
        expected_area = a * a
        result = area(a)
        self.assertEqual(result, expected_area, msg="Area calculation is incorrect.")

    def test_area_zero(self):
        """Тест: длина стороны равна 0."""
        a = 0
        expected_area = 0
        result = area(a)
        self.assertEqual(result, expected_area, msg="Area for side 0 should be 0.")

    def test_perimeter_positive(self):
        """Тест: положительная длина стороны квадрата."""
        a = 4
        expected_perimeter = 4 * a
        result = perimeter(a)
        self.assertEqual(result, expected_perimeter, msg="Perimeter calculation is incorrect.")

    def test_perimeter_zero(self):
        """Тест: длина стороны равна 0."""
        a = 0
        expected_perimeter = 0
        result = perimeter(a)
        self.assertEqual(result, expected_perimeter, msg="Perimeter for side 0 should be 0.")

if __name__ == "__main__":
    unittest.main()
