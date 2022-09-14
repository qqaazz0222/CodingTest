N = int(input())
temp = []
for i in range(N):
    t = input()
    s = int(t[0])
    r = int(t[1])
    if s < r:
        temp.append(r)
if temp == []:
    print(-1)
else:
    print(min(temp))