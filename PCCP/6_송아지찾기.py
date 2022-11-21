from collections import deque


def solution(s, e):
    # 정답을 저장할 변수를 0으로 초기화
    answer = 0
    # 방문을 저장할 배열을 만듬, 좌표가 1부터 10000까지라고 했음으로 10000개가 필요하지만
    # 각 인덱스에 좌표를 매칭하기위해 0을 포함하여 10001개 생성
    ch = [0]*10001
    # 다음 가야할 곳을 저장할 queue 생성
    dQ = deque()
    # 큐에 시작점 추가
    dQ.append(s)
    # 시작점을 방문했음을 저장
    ch[s] = 1
    # 레벨을 0으로 초기화
    L = 0
    # 큐에 값이 있을 때까지 반복
    while (dQ):
        # 큐에 값이 있는 만큼 실행
        for _ in range(len(dQ)):
            # 큐 앞에서 하나씩 출력
            x = dQ.popleft()
            # 다음 방문할 위치를 확인
            for nx in [x-1, x+1, x+5]:
                # 다음 방문할 위치가 범위 안이고 방문한 적 없으면
                if nx > 0 and nx <= 10000 and ch[nx] == 0:
                    # 다음 방문할 위치가 소가 있는 위치면
                    if nx == e:
                        # 레벨 + 1을 출력
                        # 현재 단계 레벨에서 다음 방문을 찾은 것이므로 +1을 해줘야 함
                        return L+1
                    # 방문했음을 저장
                    ch[nx] = 1
                    # 큐에 추가
                    dQ.append(nx)
        # for 문이 모두 끝났을 때 다음 단계로 넘어감
        L += 1
    return answer


print(solution(5, 14))
# 3
print(solution(8, 3))
# 5
