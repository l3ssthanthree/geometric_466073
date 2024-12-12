import unittest
import math
from ..geometric_lib.triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    """Тесты для функций расчета площади и периметра треугольника."""

    def test_area_positive(self):
        """Тест: положительные стороны треугольника."""
        a = 3
        b = 4
        c = 5
        expected_area = 6.0
        try:
            result = area(a, b, c)
            self.assertAlmostEqual(result, expected_area, places=5, msg="Area calculation is incorrect.")
        except ValueError as e:
            self.fail(f"ValueError raised unexpectedly: {e}")

    def test_area_zero(self):
        """Тест: стороны треугольника равны 0."""
        a = 0
        b = 0
        c = 0
        expected_area = 0
        try:
            result = area(a, b, c)
            self.assertEqual(result, expected_area, msg="Area should be 0 for zero sides.")
        except ValueError as e:
            self.assertTrue(True, f"ValueError raised as expected: {e}")  # Ожидаем ValueError


    def test_perimeter_positive(self):
        """Тест: положительные стороны треугольника."""
        a = 3
        b = 4
        c = 5
        expected_perimeter = 12
        try:
            result = perimeter(a, b, c)
            self.assertAlmostEqual(result, expected_perimeter, places=5, msg="Perimeter calculation is incorrect.")
        except ValueError as e:
            self.fail(f"ValueError raised unexpectedly: {e}")

    def test_perimeter_zero(self):
        """Тест: одна сторона равна 0."""
        a = 0
        b = 4
        c = 4
        expected_perimeter = 8
        try:
          result = perimeter(a, b, c)
          self.assertAlmostEqual(result, expected_perimeter, places=5, msg="Perimeter for side a = 0 should be correct.")
        except ValueError as e:
          self.assertTrue(True, f"ValueError raised as expected: {e}") # Ожидаем ValueError

if __name__ == "__main__":
    unittest.main()
