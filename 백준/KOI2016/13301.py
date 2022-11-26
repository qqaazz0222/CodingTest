N = int(input())
A = [1]
for i in range(N):
    if i == 0:
        A.append(1)
    else:
        A.append(A[-1]+A[-2])
print(A[-1]*2 + A[-2]*2)