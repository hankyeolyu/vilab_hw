# 폰켓몬

def solution(nums):
    answer = 0
    tmp = []
    nums = sorted(nums)
    for i in range(0, len(nums)):
        if len(tmp) == 0 or tmp[len(tmp) - 1] != nums[i]:
            tmp.append(nums[i])
    if len(nums) / 2 > len(tmp):
        answer = len(tmp)
    else:
        answer = len(nums) / 2
    return answer