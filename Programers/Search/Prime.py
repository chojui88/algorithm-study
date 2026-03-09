from itertools import permutations

def solution(numbers):
    count = 0
    candidate = set()
    for i in range(1,len(numbers)+1):
        #numbers 나열하는거 하나씩 확인해서 
        for j in permutations(numbers,i):
            #j는 순열
            num = int(''.join(j))
            candidate.add(num)

    for j in candidate:
        if j<2:
            continue
        
        is_prime = True
        for i in range(2,int(j**0.5) + 1):
            if j % i == 0:
                is_prime = False
                break
        if is_prime:
            count +=1
    return count