import collections


def solution(gems):
    # 정답을 저장하기 위한 배열, [시작 진열대 번호, 끝 진열대 번호]
    answer = [0, 0]
    # lt와 rt 사이에 있는 보석 종류와 갯수를 저장하기 위한 dict
    sH = collections.defaultdict(int)
    # k에 보석의 종류 수를 저장
    k = len(set(gems))
    # lt, 즉 투 포인트중 왼쪽, 검색 시작점을 0으로 초기화
    lt = 0
    # 조건을 성립하는 lt와 rt 사이의 길이를 나타내기 위해 큰 값으로 초기화
    maxL = 10000000
    # rt를 한칸씩 이동시킴
    for rt in range(len(gems)):
        # 한칸씩 이동하며 보석종류 : 보석갯수를 증가 시킴
        sH[gems[rt]] += 1
        # 보석 종류가 sH안에, 즉 lt와 rt사이에 모두 모였을때
        while (len(sH) == k):
            # lt와 rt사이 길이가 maxL보다 작을 때
            if rt-lt+1 < maxL:
                # maxL을 변경
                maxL = rt-lt+1
                # 답도 변경
                answer = [lt+1, rt+1]
            # lt가 한칸씩 이동하며 영역에서 벗어난 보석 갯수를 감소
            sH[gems[lt]] -= 1
            # 만약 보석 갯수가 0개일 때, 보석을 삭제
            if sH[gems[lt]] == 0:
                del sH[gems[lt]]
            # lt 위치를 한칸씩 증가
            lt += 1
    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA",
      "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 3]
print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# [1, 5]
