# import numpy as np
#
# a = np.zeros(3, dtype=[('a', 'f4'), ('b', 'i4'), ('c', 'S5')])
# b = np.zeros(3, dtype=[('a', 'f2'), ('b', 'i2'), ('c', 'S2')])
#
# #배열에 대해 각 필드에 데이터 할당
# a = np.zeros(13, dtype=[('a', 'f4'), ('b', 'i4'), ('c', 'S7')])
# a['a'], a['b'], a['c'] = np.arange(0.5, 7, 0.5), np.arange(2, 28, 2), [b'a' + i * b'a' for i in range(13)]
#
# b = np.zeros(10, dtype=[('a', 'f2'), ('b', 'i2'), ('c', 'S2')])
# b['a'], b['b'], b['c'] = [i ** 2 for i in range(1, 11)], [1, 32, 243, 1024, 3125, 7776, 16807, -32768, -6487, -31072], [bytes([97+i]) for i in range(10)]
#
# print(a)
# print(b)