import math


def solution(fees, records):
    # 답을 저장할 배열
    answer = []
    # 차량 들어온 시간을 저장할 배열
    inTime = [0]*10000
    # 차량이 들어와 있는지 상태를 저장할 배열
    isIn = [0]*10000
    # 주차 총 시간을 저장할 배열
    sumT = [0]*10000

    # recordes 배열에서 기록을 하나씩 가져와 record에 저장
    for record in records:
        # 기록 중 시간을 a, 차량번호를 b, 입출 상태를 c에 각각 저장
        a, b, c = record.split()
        # 시간을 시와 분으로 나누어 각각 h와 m에 저장
        h, m = a.split(":")
        # 차량이 들어왔을 때
        if c == "IN":
            # inTime 배열의 차량번호 인덱스에 시간을 분으로 환산하여(시간 * 60 + 분) 저장
            inTime[int(b)] = int(h)*60+int(m)
            # isIn 배열의 차량번호 인덱스에 차량이 주차장에 있음을 저장
            isIn[int(b)] = 1
        # 차량이 나갔을 때
        else:
            # 총 시간에 (출차 시간 - 입차 시간)을 더함
            sumT[int(b)] += (int(h)*60+int(m))-inTime[int(b)]
            # isIn 배열의 차량번호 인덱스에 차량이 주차장에 없음을 저장
            isIn[int(b)] = 0

    # isIn 배열을 처음부터 끝까지 돌며 주차장에 남아있는, 즉 입차 기록은 있지만 출차 기록은 없는 차들을 검색
    for i in range(10000):
        # isIn 배열의 차량번호 인덱스가 주차장에 있음이면
        if isIn[i] == 1:
            # 총 시간에 (23시59분 - 입차 시간)을 더함
            sumT[i] += (23*60+59)-inTime[i]
    # sumT 배열을 처음부터 끝까지 돌며, 주차 시간을 요금으로 환산
    for i in range(10000):
        # i번 차량의 총 주차시간이 0분 초과면
        if sumT[i] > 0:
            # i번 차량의 요금을 구해서 answer배열에 추가함
            answer.append(
                fees[1]+max(math.ceil((sumT[i]-fees[0])/fees[2]), 0)*fees[3])
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# [14600, 34400, 5000]
print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN",
      "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
# [0, 591]
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
# [14841]
