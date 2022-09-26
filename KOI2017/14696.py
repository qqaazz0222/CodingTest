N = int(input())
for i in range(N):
    R = ''
    tempA = [0 ,0 ,0 ,0]
    tempB = [0 ,0 ,0 ,0]
    A = input().split()
    B = input().split()
    for j in A[1:]:
        tempA[int(j)-1] += 1
    for j in B[1:]:
        tempB[int(j)-1] += 1
    for j in range(3, -1, -1):
        if tempA[j] > tempB[j]:
            R = 'A'
            break
        elif tempA[j] < tempB[j]:
            R = 'B'
            break
        elif tempA[j] == tempB[j]:
            if j == 0:
                R = 'D'
                break
            else:
                continue
    print(R)