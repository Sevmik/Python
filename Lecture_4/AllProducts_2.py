listAll = []

def df1(n, listzOfDel = [], start = 2):
    if n == 1:
        listAll.append(listzOfDel)
    else:
        for d in range(start, n+1):
            if n % d == 0:
                p = listzOfDel
                p.append(d)
                df1(n=int(n/d), start=d, listzOfDel=p)



print(df1(24))