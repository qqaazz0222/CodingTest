def solution(k, room_number):
    answer = []
    t_list = [0]*k
    for i in range(len(room_number)):
        if t_list[room_number[i]] == 0:
            t_list[room_number[i]] = room_number[i]
            answer.append(room_number[i])
        else:
            temp = room_number[i]+1
            idx = t_list[temp:].index(0)
            t_list[temp+idx] = temp+idx
            answer.append(temp+idx)
    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))


# 한 번에 한 명씩 신청한 순서대로 방을 배정합니다.
# 고객은 투숙하기 원하는 방 번호를 제출합니다.
# 고객이 원하는 방이 비어 있다면 즉시 배정합니다.
# 고객이 원하는 방이 이미 배정되어 있으면 원하는 방보다 번호가 크면서 비어있는 방 중 가장 번호가 작은 방을 배정합니다.

#
