import numpy as np


def getSolutionNos(a, b, odd):

    n = 0
    nn = np.array([])
    if b == 0:
        return 1
    elif b > 0:
        if len(a) >= 2:
            bb = b - a[-1] * np.array(np.arange(0, b // a[-1] + 1))
            if odd:
                print('entering odd')
                print('bb:', bb)
                print('a:', a)
                for i in bb:
                    print("odd_n[i]:", i)
                    print('odd_a[:-1]', a[:-1])
                    # print('fun:', getSolutionNos(a[:-1], i, False))
                    n += getSolutionNos(a[:-1], i, False)
                print('odd_n', n)
            else:
                print('entering odd')
                print('bb:', bb)
                print('a:', a)
                for i in bb:
                    print("even_n[i]:", i)
                    print('even_a[:-1]', a[:-1])
                    nn = np.append(nn, getSolutionNos(a[:-1], i, False))
                    print('nn:', nn)
                n += np.dot(nn, np.array(np.arange(1, len(nn) + 1) + 1))
                print('even_n', n)

            return n
        else:
            n += (b + 1)
            print('len1_n', n)
            return n
    else:
        return n


a = np.array([1, 4, 6, 4, 1])
# a = np.array([1, 3, 3, 1])
b = 14
odd = len(a) % 2 == 1
if odd:
    a = a[:len(a) // 2 + 1]
else:
    a = a[:len(a) // 2]
n = 0
# for _ in a:
#     if odd:
#         n += getSolutionNos(a, b, odd)
#         odd = False
#     else:
#         n += getSolutionNos(a, b, odd)
#     a = a[:-1]
n += getSolutionNos(a, b, odd)
print('a:', a)
print('res:', n)
