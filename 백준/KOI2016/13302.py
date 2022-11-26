d1, d3, d5 = 10000, 25000, 37000
C = 0
N, M = map(int, input().split())
D = input().split()
U = [0, 0, 0]
for i in range(1, N+1):
    if str(i) in D:
        continue
    else:
        