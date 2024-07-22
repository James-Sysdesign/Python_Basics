#!/usr/bin/python3

def len_int(n):
    if type(n) != int:
        raise TypeError('provide only integer input')

    str_n = str(abs(n))
    return len(str_n)

assert len_int(123) == 3
assert len_int(2) == 1
assert len_int(+42) == 2
assert len_int(-42) == 2
assert len_int(572342) == 6
assert len_int(962306349871524124750813401378124) == 33
"""/*

    # n x n adjacency matric
    len_matrix = len(matrix)

    # build graph and visited nodes
    connected = defaultdict(list)
    seen = set()

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                connected[i].append(j)

*/"""
try:
    len_int('a')
except TypeError as e:
    assert str(e) == 'provide only integer input'

print('all tests passed')
