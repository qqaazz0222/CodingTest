def solution(operations):
    answer = []
    que = []
    for i in operations:
        temp = i.split(' ')
        if temp[0] == 'I':
            que.append(int(temp[1]))
        elif temp[0] == 'D':
            if len(que) != 0:
                if temp[1] == '1':
                    del que[que.index(max(que))]
                elif temp[1] == '-1':
                    del que[que.index(min(que))]
    if len(que) == 0:
        answer = [0, 0]
    else:
        answer = [max(que), min(que)]
    return answer


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642",
      "I 45", "I 97", "D 1", "D -1", "I 333"]))
