N = int(input())
A = input().split()
temp = []
for i in range(N):
    temp.append(int(A[i])%2)
while True:
    ans = 0
    for i in range(N-1):
        if temp[i] == temp[i+1]:
            ans += 1
    if ans > 1:
        
