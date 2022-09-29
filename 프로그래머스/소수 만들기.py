def check(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    temp = []
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for l in range(j+1, len(nums)):
                n = nums[i] + nums[j] + nums[l]
                if n not in temp:
                    if check(n):
                        temp.append(n)
    answer = len(temp)
    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))