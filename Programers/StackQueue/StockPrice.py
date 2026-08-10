def solution(prices):
    time = [0] * len(prices)

    # 가격 하나씩 하나씩 확인하는 루틴
    for i in range(len(prices)):
    #만약 다음에 들어오는 값이 이전 값보다 작으면 time[i]의 값 +1
        for j in range(i+1,len(prices)): #i보다 큰 값을 비교해야 하므로
            time[i]+=1 
            if prices[j]<prices[i]:
                break
        #i 번째가 마지막까지 갔을때, 얼마나 유지가 되는지
        
    #가격 안떨어진 기간은 몇초인지 
    return time