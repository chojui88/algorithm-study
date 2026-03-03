import math

def solution(progresses, speeds):
    result = []
    
    # 1️⃣ 각 기능의 완료일 계산
    days = []
    for p, s in zip(progresses, speeds):
        remain = 100 - p
        days.append(math.ceil(remain / s))
    
    # 2️⃣ 기준 설정
    기준 = days[0]
    count = 1
    
    # 3️⃣ 앞에서부터 비교
    for i in range(1, len(days)):
        if days[i] <= 기준:
            count += 1
        else:
            result.append(count)
            기준 = days[i]
            count = 1
    
    # 4️⃣ 마지막 묶음 추가
    result.append(count)
    
    return result