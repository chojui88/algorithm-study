def solution(nums):
    pocket = {}
    for i in nums:
        pocket[i] = 0

    for i in nums:
        pocket[i] +=1
    

    result = min(len(pocket),len(nums)//2)
    return result
