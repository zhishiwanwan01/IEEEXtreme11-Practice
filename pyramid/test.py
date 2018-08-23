# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)


input_parser = parser()


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


def getSolutionNos(a, b, odd):

    n = 0

    if b == 0:
        return 1
    elif b > 0:
        if len(a) >= 2:
            if odd:
                for i in range(b // a[-1] + 1):
                    n += getSolutionNos(a[:-1], b - a[-1] * i, False)
            else:
                for i in range(b // a[-1] + 1):
                    n += (i + 1) * getSolutionNos(a[:-1], b - a[-1] * i, False)
            return n
        else:
            n += (b + 1)
            return n
    else:
        return n


# numpy and scipy are available for use
import numpy as np
# import scipy


# get from https://stackoverflow.com/questions/24093387/pascals-triangle-for-python

def pascals_triangle(n_rows):
    results = []  # a container to collect the rows
    for _ in range(n_rows):
        row = [1]  # a starter 1 in the row
        if results:  # then we're in the second row or beyond
            last_row = results[-1]  # reference the previous row
            # this is the complicated part, it relies on the fact that zip
            # stops at the shortest iterable, so for the second row, we have
            # nothing in this list comprension, but the third row sums 1 and 1
            # and the fourth row sums in pairs. It's a sliding window.
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # finally append the final 1 to the outside
            row.append(1)
        results.append(row)  # add the row to the results.
    return results


s = 30
pas_tri = pascals_triangle(int(np.log2(s)) + 1)

n = 0
for i in range(len(pas_tri)):
    x1 = np.array(pas_tri)[i]
    x2 = s - 2 ** i
    odd = len(x1) % 2 == 1
    if len(x1) == 1:
        p = 1
    else:
        if odd:
            x1 = x1[:len(x1) // 2 + 1]
        else:
            x1 = x1[:len(x1) // 2]
        p = getSolutionNos(x1, x2, odd)
    print('p=', p)
    n += p

print(n % (10**9 + 7))
# for x1 in range(c // b[0] + 1):
#     for x2 in range(c // b[1] + 1):
#         for x3 in range(c // b[2] + 1):
#             for x4 in range(c // b[3] + 1):
#                 if x1 * b[0] + x2 * b[1] + x3 * b[2] + x4 * b[3] == c:
#                     n += 1
