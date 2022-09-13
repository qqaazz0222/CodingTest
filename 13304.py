# 백준 13304번 문제
import math

NK = input().split()
N = int(NK[0])
K = int(NK[1])
SYN = [0, 0, 0, 0, 0]
R = 0
for i in range(N):
    SY = input().split()
    S = int(SY[0])
    Y = int(SY[1])
    if Y == 1 or Y == 2:
        SYN[0] += 1
    if Y == 3 or Y == 4:
        if S == 0:
            SYN[1] += 1
        if S == 1:
            SYN[2] += 1
    if Y == 5 or Y == 6:
        if S == 0:
            SYN[3] += 1
        if S == 1:
            SYN[4] += 1
for i in SYN:
    R += math.ceil(i/K)
print(R)