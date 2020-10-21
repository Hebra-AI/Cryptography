import math


def function(n):
    for j in range(0, n):
        j = j + 1
        k = math.gcd(n, j)
        if k == 1:
            if n != j:
                print(j, ',', end='')


number = int(input('Write number: '))
function(number)

