"""
Имеется большая последовательность объектов (неважно каких), допускающих операцию сравнения.
Известно, что некоторых одинаковых объектов в последовательности больше половины.
Требуется, не храня последовательности, выяснить, чему они равны (т. е. вывести пример такого объекта).
Ввод построчный, последняя строка — пустая.
"""




pair_count = 0
pair_name = ""
c = ""

while True:
    a = input()
    if a == "":
        break
    a = str(eval(a))
    if c == a:
        if pair_count == 0:
            pair_name = a
        if a == pair_name:
            pair_count += 1
        else:
            pair_count -= 1
    c = a

if pair_count == 0:
    pair_name = c


print(pair_name)

if sum_otr - a >= a:
    count_sum = True
    sum = a
else:
    sum -= a