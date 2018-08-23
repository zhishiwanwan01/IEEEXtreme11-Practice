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


# numpy and scipy are available for use
import numpy as np

# from numba import jit
# import scipy
# s = get_number()


# def carry(a, b):
#     for i in range(len(a)):
#         if a[i] > b[i]:
#             if i < len(a) - 1:
#                 a[i] = 0
#                 a[i + 1] += 1
#             else:
#                 return False
#     return a

def varGen(a):

    b = 1
    for i in a:
        b *= (i + 1)
    # print(b)
    x = np.zeros((b, len(a)), dtype='i4')
    den = b
    # num = 0
    for i in range(len(a)):
        temp = []
        den /= (a[i] + 1)
        # print(den)
        den = int(den)
        for k in range(a[i] + 1):
            temp += [k] * den
        # print(temp)
        # num = b // len(temp)
        # print(num)
        x[:, i] = np.array(temp * (b // len(temp)))
    return x, b


def layerTotalNumber(a, n):
    if n == 0:
        return 1
    b = n // np.array(a)
    # c = 1
    # for i in b:
    #     c *= (i + 1)
    # x = np.zeros((c, len(a)))
    # temp = x[0, :]
    # for i in range(c):
    #     x[i, :] = temp
    #     temp[0] += 1
    #     temp = carry(temp, b)
    x, row_nums = varGen(b)
    # k = 0
    # print('x=', x)
    aa = np.tile(a, (row_nums, 1))
    # print('aa*x:', np.sum(aa * x, 1) == n)
    yy = np.sum(np.sum(aa * x, 1) == n)
    # for row in x:
    #     if np.sum(row * a) == n:
    #         k += 1
    return yy


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


s = 21
pas_tri = pascals_triangle(int(np.log2(s)) + 1)

n = 0
for i in range(len(pas_tri)):
    x1 = np.array(pas_tri)[i]
    x2 = s - 2 ** i
    # print('x1: ', x1)
    # print('x2: ', x2)
    p = layerTotalNumber(x1, x2)
    print('p=', p)
    n += p

print(n)
# for x1 in range(c // b[0] + 1):
#     for x2 in range(c // b[1] + 1):
#         for x3 in range(c // b[2] + 1):
#             for x4 in range(c // b[3] + 1):
#                 if x1 * b[0] + x2 * b[1] + x3 * b[2] + x4 * b[3] == c:
#                     n += 1
