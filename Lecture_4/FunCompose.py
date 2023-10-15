from math import *

def compose(f, g, *kwargs):
    def r(*kwargs):
        def h():
            return f(g(kwargs), g(kwargs[::-1]))

        return h
    return r()

print(max(pow(5, 6), pow(6,5)))

print(compose(max, pow)(5,6, 7, 8))