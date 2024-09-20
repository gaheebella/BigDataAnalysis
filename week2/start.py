from numpy import random
x = random.randint(1, 47)
print(x)

from sys import path
path = "/home/sungshin"
x = path

for i in range(len(x)):
    print(x[i])


def add(x, y):
    return x + y

print(add(3, 4))

class mymath:
    def add(self, x, y):
        return x + y

p1 = mymath()
print(p1.add(3, 4))


