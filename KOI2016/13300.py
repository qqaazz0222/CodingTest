import math
N, K = map(int, input().split())
SYN = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
R = 0
for i in range(N):
    S, Y = map(int, input().split())
    SYN[Y-1][S] += 1
for i in SYN:
    R += math.ceil(i[0]/K)
    R += math.ceil(i[1]/K)
print(R)