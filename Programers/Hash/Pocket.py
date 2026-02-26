def solution(nums):
    pocket = {}
    for i in nums:
        pocket[i] +=1
    

    result = min(len(pocket),len(nums)/2)

