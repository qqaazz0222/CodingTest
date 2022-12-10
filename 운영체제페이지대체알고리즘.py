from collections import defaultdict as dd


def fifoq(sl):
    q = []
    cnt = 0
    for i in sl:
        if i not in q:
            if len(q) > 2:
                q[cnt % 3] = i
                cnt += 1
            else:
                q.append(i)
            print(q)


def beladyq(sl):
    q = dd(int)
    for i in sl:
        if len(q) > 2:

        else:


            # print(fifoq([1, 2, 3, 2, 1, 5, 2, 1, 6, 2, 5, 6, 3, 1, 3, 6, 1, 2, 4, 3]))
print(beladyq([1, 2, 3, 2, 1, 5, 2, 1, 6, 2, 5, 6, 3, 1, 3, 6, 1, 2, 4, 3]))
