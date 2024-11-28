Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... 
... # Функция для расчета площади круга.
... # Аргументы:
... # - r (float): Радиус круга.
... # Возвращает:
... # - float: Площадь круга.
... # Пример:
... # >>> area(5)
... # 78.53981633974483
... def area(r):
...     return math.pi * r * r
... 
... # Функция для расчета периметра (длины окружности) круга.
... # Аргументы:
... # - r (float): Радиус круга.
... # Возвращает:
... # - float: Периметр круга.
... # Пример:
... # >>> perimeter(5)
... # 31.41592653589793
... def perimeter(r):
...     return 2 * math.pi * r
