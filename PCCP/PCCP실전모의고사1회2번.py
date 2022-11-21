answer = 0


def DFS(L, s, ability, ch):
    global answer
    n = len(ability)
    m = len(ability[0])
    if L == m:
        answer = max(answer, s)
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                DFS(L+1, s+ability[i][L], ability, ch)
                ch[i] = 0


def solution(ability):
    global answer
    ch = [0]*len(ability)
    DFS(0, 0, ability, ch)
    return answer


print(solution([[40, 10, 10], [20, 5, 0], [
      30, 30, 30], [70, 0, 70], [100, 100, 100]]))
# 210
print(solution([[20, 30], [30, 20], [20, 30]]))
# 60
