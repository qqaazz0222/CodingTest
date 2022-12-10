sl = [1, 2, 3, 2, 1, 5, 2, 1, 6, 2, 5, 6, 3, 1, 3, 6, 1, 2, 4, 3]
fifoq = []
cnt = 0
for i in sl:
    if i not in fifoq:
        if len(fifoq) > 2:
            fifoq[cnt % 3] = i
            cnt += 1
        else:
            fifoq.append(i)
        print(fifoq)
