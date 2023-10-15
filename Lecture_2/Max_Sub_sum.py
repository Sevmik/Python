"""
Ввести в столбик последовательность целых (положительных и отрицательных) чисел, не равных нулю;
в конце этой последовательности стоит 0.
Вывести наибольшую сумму последовательно идущих элементов этой последовательности (не менее одного).
"""

sum = 0
count_sum = False
sum_better = 0
count_sum_better = False

while True:
    a = int(input())
    if a == 0:
        break

    if sum + a <= a or not count_sum:
        sum = a
        count_sum = True
    else:
        sum += a

    if sum_better < sum or not count_sum_better:
        sum_better = sum
        count_sum_better = True

print(sum_better)