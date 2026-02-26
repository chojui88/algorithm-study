def solution(participant , completion):
    hashDict = {}
    sumHash = 0

    #1. hash : par 딕셔너리 만들기
    #2. par의 sum 구하기
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    #3. completion의 sum 빼기
    for i in completion:
        sumHash -= hash(i)
    #4. 남은 값을 return
        
    return hashDict[sumHash]
