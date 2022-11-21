import collections


def solution(id_list, report, k):
    # 답을 저장할 배열
    answer = []
    # 중복된 신고를 처리하기 위해서 set형으로 변환 후, list형으로 변환
    report = list(set(report))
    # 유저가 신고한 유저들 목록을 저장하기 위해 Hashing 자료형을 만듬
    reportHash = collections.defaultdict(set)
    # 유저가 신고 받은 횟수를 저장하기 위해 Hashing 자료형을 만듬
    stoped = collections.defaultdict(int)

    # 신고 내역을 하나씩 조회
    for x in report:
        # 조회한 신고 내역을 split 명령어로 잘라, 신고한 회원은 a, 신고받은 회원은 b에 저장
        a, b = x.split(" ")
        # 신고한 회원 : {신고받은 회원} 의 형태로 저장
        reportHash[a].add(b)
        # 신고받은 회원 : 신고받은 횟수 의 형태로 저장
        stoped[b] += 1

    # 아이디 목록에서 하니씩 조회
    for name in id_list:
        # 받는 메일수를 0으로 초기화
        mail = 0
        # 조회한 아이디의 유저가 신고한 유저들을 조회
        for user in reportHash[name]:
            # 조회한 유저들 중 신고를 k번 이상 당해 정지 당한 회원을 조회
            if stoped[user] >= k:
                # 정지 당한 회원이 있으면 받는 메일수를 1 증가
                mail += 1
        # answer배열에 받는 메일수를 추가
        answer.append(mail)
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con",
      "ryan con", "ryan con", "ryan con"], 3))
