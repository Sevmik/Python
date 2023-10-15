def conditionEmpty(a):
    if a is None:
        return True
    elif isinstance(a, bool):
        return True
    elif isinstance(a, int|float):
        return False
    elif len(a) == 0:
        return True
    return False


def sheff(a, b):
    if conditionEmpty(a):
        if not conditionEmpty(b): return b
        else: return True
    else:
        if not conditionEmpty(b): return False
        else: return a

