def area(side):
    """Вычисляет площадь квадрата."""
    if side < 0:
        raise ValueError("Сторона не может быть отрицательной.")
    return side**2

def perimeter(side):
    """Вычисляет периметр квадрата."""
    if side < 0:
        raise ValueError("Сторона не может быть отрицательной.")
    return 4 * side