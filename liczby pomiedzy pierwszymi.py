from math import *


def llpp(pocz, kon):
    pierwsze = []
    bylo = False
    for i in range(pocz, kon + 1):
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                bylo = True
                break
        if not bylo:
            pierwsze.append(i)
        else:
            bylo = False
    wynik = []
    for i in pierwsze:
        for j in pierwsze:
            if (i + j) % 2 == 0 and i != j:
                wynik.append((i + j) // 2)
    return len(set(wynik))


print(llpp(5, 7))
