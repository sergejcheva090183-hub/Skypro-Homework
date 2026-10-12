import math

def square(side):
    area = side * side
    if isinstance(side, int):
        return area
    else:
        return math.ceil(area)
side1 = 5
result1 = square(side1)
print(f"Сторона: {side1}, Площадь: {result1}") 