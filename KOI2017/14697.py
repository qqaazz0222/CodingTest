from unittest import result


A, B, C, N = map(int, input().split())
x = result = 0
for c in range(N // C + 1):
    for b in range(N // B + 1):
        for a in range(N // A + 1):
            x = a * A + b * B + c * C
            if x == N:
                result = 1
print(result)