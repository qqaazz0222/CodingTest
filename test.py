n = 78
answer = 0
count = str(bin(n))[2:].count('1')
while True:
    n += 1
    if count == str(bin(n))[2:].count('1'):
        answer = n
        break
print(answer)