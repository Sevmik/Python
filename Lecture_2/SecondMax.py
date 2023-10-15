"""
Ввести по одному в строке целые числа, не равные нулю (не менее одного, конец ввода — 0),
вывести второй максимум последовательности (число, строго меньшее максимума последовательности,
и не меньшее остальных чисел в ней), и NO, если такового нет.
"""



# max1 = 0
max2 = 0
setMax1 = False
setMax2 = False

while True:
    n = int(input())

    if n == 0:
        break

    if not setMax1:
        setMax1 = True
        max1 = n
    elif not setMax2:
        if n > max1:
            max2 = max1
            max1 = n
            setMax2 = True
        elif n != max1:
            max2 = n
            setMax2 = True
    elif n > max1:
        max2 = max1
        max1 = n
    elif n > max2 and n != max1:
        max2 = n

if max2 == 0:
    print("NO")
else:
    print(max2)