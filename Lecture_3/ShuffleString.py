"""
Ввести построчно две строки и проверить, есть ли такое число n,
что вторая строка получается из первой,
если сначала взять каждый n-й символ, затем — каждый n-й,
начиная с первого и т. д. до каждого n-го, начиная с n-1-го.
Вывести наименьшее возможное n, а если такого числа нет — No.
"""



str1, str2 = input(), input()
count, len1, a = 0, len(str1), ""

if len1 != len(str2): print("No")
else:
    while count < len1 and a != str2:
        count += 1
        k, c, a, b = 0, 0, "", 0
        while k < len1:
            if str1[c] != str2[k]: break
            a+=str1[c]
            c += count
            if c > len1 - 1:
                b += 1
                c = b
            k += 1

    print(count) if a == str2 else print("No")
