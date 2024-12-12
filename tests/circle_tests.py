import unittest
import math
from ..circle import area, perimeter  # Относительный импорт

class CircleTestCase(unittest.TestCase):
    """Тесты для функций расчета площади и периметра круга."""

    def test_area_positive(self):
        """Тест: положительный радиус круга."""
        r = 5
        expected_area = math.pi * r * r
        result = area(r)
        self.assertAlmostEqual(result, expected_area, places=5, msg="Area calculation is incorrect.")

    def test_area_zero(self):
        """Тест: радиус равен 0."""
        r = 0
        expected_area = 0
        result = area(r)
        self.assertEqual(result, expected_area, msg="Area for radius 0 should be 0.")

    def test_perimeter_positive(self):
        """Тест: положительный радиус круга."""
        r = 5
        expected_perimeter = 2 * math.pi * r
        result = perimeter(r)
        self.assertAlmostEqual(result, expected_perimeter, places=5, msg="Perimeter calculation is incorrect.")

    def test_perimeter_zero(self):
        """Тест: радиус равен 0."""
        r = 0
        expected_perimeter = 0
        result = perimeter(r)
        self.assertEqual(result, expected_perimeter, msg="Perimeter for radius 0 should be 0.")

if __name__ == "__main__":
    unittest.main()
