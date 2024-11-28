Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Функция для расчета площади прямоугольного треугольника.
... # Аргументы:
... # - a (float): Основание треугольника.
... # - b (float): Высота треугольника.
... # Возвращает:
... # - float: Площадь треугольника.
... # Пример:
... # >>> area(3, 4)
... # 6.0
... def area(a, b):
...     return (a * b) / 2
... 
... # Функция для расчета периметра прямоугольного треугольника.
... # Аргументы:
... # - a (float): Основание треугольника.
... # - b (float): Высота треугольника.
... # Возвращает:
... # - float: Периметр треугольника.
... # Пример:
... # >>> perimeter(3, 4)
... # 12.0
... def perimeter(a, b):
...     c = math.sqrt(a**2 + b**2)  # Гипотенуза
...     return a + b + c
