total = 0
for i in range(101):
    if i % 4 == 0:
        print(total, "+", i, "=")
        total += i
        print(total)
