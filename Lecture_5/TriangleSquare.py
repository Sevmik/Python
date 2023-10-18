"""
Ввести через запятую шесть чисел: x1, y1, x2, y2, x3, y3
и вывести точное значение площади треугольника (x1, y1), (x2, y2), (x3, y3).
"""
import decimal
count = 0
decimal.getcontext().prec = 1000
str_numbers =input().split(',')
x1, y1 = decimal.Decimal(str_numbers[0]), decimal.Decimal(str_numbers[1])
x2, y2 = decimal.Decimal(str_numbers[2]), decimal.Decimal(str_numbers[3])
x3, y3 = decimal.Decimal(str_numbers[4]), decimal.Decimal(str_numbers[5])
square = decimal.Decimal(1/2)*abs((x1*(y2-y3)+x2*(y3-y1) + x3*(y1-y2)))
if int(square) == square:
    print(int(square))
else:
    print(square.normalize())