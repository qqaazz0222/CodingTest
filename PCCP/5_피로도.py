# 정답을 DFS함수 안에서도 사용하기위해 전역 변수로 설정
answer = 0


def DFS(k, cnt, dungeons, ch):
    # DFS 함수 안에서 전역 변수 answer를 사용하겠다고 정의
    global answer
    # answer를 cnt와 비교하여 더 큰값으로 변경
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        # 피로도가 던전 최소 필요 피로도 보다 높고, 간적 없는 던전이라면
        if k >= dungeons[i][0] and ch[i] == 0:
            # 던전에 체크, 즉 해당 던전을 방문했음을 표시
            ch[i] = 1
            # 피로도에서 던전 소모피로도를 빼고, 카운트를 증가시켜 다음 던전으로 이동
            DFS(k-dungeons[i][1], cnt+1, dungeons, ch)
            # 던전을 빠져나오며 해당 던전 방문했음을 지움
            ch[i] = 0


def solution(k, dungeons):
    # 던전 방문을 확인하기위한 0으로 이루어진 배열을 만듬, 0 : 방문한적 없음, 1 : 방문한적 있음
    ch = [0] * len(dungeons)
    DFS(k, 0, dungeons, ch)
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
# 3
