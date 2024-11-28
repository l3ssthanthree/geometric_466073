import sys
import os
import unittest
import math

# Добавляем путь к модулю triangle.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/lucky/geometric_lib_466073')))

from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    """Тесты для функций расчета площади и периметра треугольника."""

    def test_area_positive(self):
        """Тест: положительные основания и высота."""
        a = 3
        b = 4
        expected_area = (a * b) / 2
        result = area(a, b)
        self.assertEqual(result, expected_area, msg="Area calculation is incorrect.")

    def test_area_zero(self):
        """Тест: основание или высота равны 0."""
        a = 0
        b = 4
        expected_area = 0
        result = area(a, b)
        self.assertEqual(result, expected_area, msg="Area for one side 0 should be 0.")

    def test_perimeter_positive(self):
        """Тест: положительные основания и высота."""
        a = 3
        b = 4
        c = math.sqrt(a**2 + b**2)  # Гипотенуза
        expected_perimeter = a + b + c
        result = perimeter(a, b)
        self.assertAlmostEqual(result, expected_perimeter, places=5, msg="Perimeter calculation is incorrect.")

    def test_perimeter_zero(self):
        """Тест: одно основание равно 0."""
        a = 0
        b = 4
        c = math.sqrt(a**2 + b**2)  # Гипотенуза
        expected_perimeter = b + c  # Периметр при a = 0
        result = perimeter(a, b)
        self.assertAlmostEqual(result, expected_perimeter, places=5, msg="Perimeter for side a = 0 should be correct.")

if __name__ == "__main__":
    unittest.main()