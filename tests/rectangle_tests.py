import unittest
from ..rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    """Тесты для функций расчета площади и периметра прямоугольника."""

    def test_area_positive(self):
        """Тест: положительные стороны прямоугольника."""
        a = 5
        b = 10
        expected_area = a * b
        result = area(a, b)
        self.assertEqual(result, expected_area, msg="Area calculation is incorrect.")

    def test_area_zero(self):
        """Тест: одна из сторон равна 0."""
        a = 0
        b = 10
        expected_area = 0
        result = area(a, b)
        self.assertEqual(result, expected_area, msg="Area for one side 0 should be 0.")

    def test_perimeter_positive(self):
        """Тест: положительные стороны прямоугольника."""
        a = 5
        b = 10
        expected_perimeter = 2 * (a + b)
        result = perimeter(a, b)
        self.assertEqual(result, expected_perimeter, msg="Perimeter calculation is incorrect.")

    def test_perimeter_zero(self):
        """Тест: одна из сторон равна 0."""
        a = 0
        b = 10
        expected_perimeter = 2 * (a + b)
        result = perimeter(a, b)
        self.assertEqual(result, expected_perimeter, msg="Perimeter for one side 0 should be correct.")

    def test_perimeter_equal_sides(self):
        """Тест: стороны равны (квадрат)."""
        a = 5
        b = 5
        expected_perimeter = 2 * (a + b)
        result = perimeter(a, b)
        self.assertEqual(result, expected_perimeter, msg="Perimeter for square should be correct.")

if __name__ == "__main__":
    unittest.main()
