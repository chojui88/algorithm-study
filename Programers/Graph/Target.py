def solution(numbers , target):
    ing = [0]
    
    for i in (numbers):
        temp = []
        for j in ing:
            temp.append(j + i)
            temp.append(j - i)
        ing = temp
    
    return ing.count(target)
