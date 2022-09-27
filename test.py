answer = 0
num = 6
while True:
    print(answer, num)
    if answer < 500:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num / 3 + 1