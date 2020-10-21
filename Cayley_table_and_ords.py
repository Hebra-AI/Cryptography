def function(c, m):  # function counts Cayley table
    i = 0
    j = 0
    f = 0
    print(c, end="")
    if c == '*':
        i = 1
        j = 1
    while i < m:
        print('', i, end="")
        i = i + 1
    print("")
    while j < m:
        print(j, end='')

        while f < m:
            k = f
            if c == '*':
                k = k + 1
                if (k * j) % m != 0:
                    k = (k * j) % m
            if c == '+':
                k = (k + j) % m
            if k != m:
                print("", k, end="")
            f = f + 1
        f = 0
        print(" ")
        j = j + 1


def vac_machine():
    character = str(input("Write character : "))
    module = int(input("Write mod : "))
    function(character, module)
    if character == '*':  # count ords for operation *
        for el_group in range(1, module):
            for n in range(1, module):
                k = pow(el_group, n, module)
                if k == 1:
                    print('ord', el_group, '=', n)
                    break
    if character == '+':  # count ords for operation +
        print('ord 0 = 1')
        for el_group in range(1, module):
            for n in range(0, module):
                k = (el_group + el_group * n) % module
                if k == 0:
                    print('ord', el_group, '=', n + 1)
                    break


vac_machine()

