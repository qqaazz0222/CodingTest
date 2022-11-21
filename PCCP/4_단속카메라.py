def solution(routes):
    # 정답을 저장할 변수 선언
    answer = 0
    # 차량의 진입지점 최소 값이 -30000이므로 그보다 작은 -30001로 현재 위치를 초기화
    point = -30001
    # routes를 진출 지점을 기준으로 오름차순 정렬
    routes = sorted(routes, key=lambda x: x[1])
    # routes에서 하나씩 조회하여 route에 저장
    for route in routes:
        # 위치(point)가 route의 진입지점보다 작으면
        if point < route[0]:
            # 카메라 1대 설치
            answer += 1
            # 위치(point)를 route의 진출 지점으로 변경
            point = route[1]
    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
# 2
