answer = 0


def DFS(lv, total, ability, ch):
    global answer
    answer = max(answer, total)
    for i in range(len(ability)):
        if lv < len(ability[i]) and ch[i] == 0:
            ch[i] = 1
            total += ability[i][lv]
            DFS(lv+1, total, ability, ch)
            ch[i] = 0
            total -= ability[i][lv]


def solution(ability):
    ch = [0]*len(ability)
    DFS(0, 0, ability, ch)
    return answer


print(solution([[40, 10, 10], [20, 5, 0], [
      30, 30, 30], [70, 0, 70], [100, 100, 100]]))
