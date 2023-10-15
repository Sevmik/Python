"""
Ввести произвольное натуральное число, не превосходящее 1000000000, и вывести (через «*») все его разложения на натуральные сомножители, превосходящие 1, без учёта перестановок.
Сомножители в каждом разложении и сами разложения (как последовательности) при выводе должны быть упорядочены по возрастанию.
Само число также считается разложением.
Можно использовать рекурсию.
"""

listAll = []

def df1(n, listzOfDel=[], start=2):
    if n == 1:
        listAll.append(listzOfDel)
    else:
        for d in range(start, n + 1):
            if n % d == 0:
                p = listzOfDel.copy()
                p.append(d)
                df1(n=int(n / d), start=d, listzOfDel=p)


m = int(input())
df1(m)

for i in listAll:
    print(*i, sep = "*")