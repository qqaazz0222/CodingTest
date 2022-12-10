import random
a = []
for i in range(10):
    a.append(random.randrange(10000, 100000))
print(sorted(a, reverse=True))
