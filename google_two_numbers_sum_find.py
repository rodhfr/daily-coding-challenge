# author: Rodolfo Franca de Souza
# mail: souzafrodolfo@gmail.com
# date: 2026-02-16
# license: GPLv3
# topics: arrays, hash set
# difficulty: easy
#

def find_value_two_pass():
    lst = [10, 15, 3, 7]
    k = 17
    for x in lst:
        for y in lst:
            op = x + y
            print(x, "+", y, "=", op)
            if op == k:
                return True


print("Two pass find: ")
print(find_value_two_pass(), "\n")


def find_value_one_pass():
    lst = [10, 15, 3, 7]
    print("lst =", lst)

    k = 17
    print("objetivo =", k)

    # criar set de ja vistos pra ver se a diferenca entre
    # o novo numero e o k ja esta presente no set de vistos
    seen = set()

    for x in lst:
        print("x =", x)
        # se a diferenca entre o k e o novo item ja estiver presente retorne True.
        diff = k - x
        if diff in seen:
            return True
        # se nao encontrar adicione o novo valor aos vistos
        seen.add(x)
        print("add to set:", x, "\nvistos:", seen)

    return False


print("One pass find: ")
print(find_value_one_pass())
