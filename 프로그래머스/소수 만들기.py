def solution(nums):
    answer = 0
    temp = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for l in range(j+1, len(nums)):
                n = nums[i] + nums[j] + nums[l]
                if n not in temp:
                    temp.append(n)
    print(temp)
    for i in temp:
        for j in range(2, i):
            if i % j != 0:
                answer += 1
                break
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))