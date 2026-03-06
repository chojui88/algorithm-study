from collections import deque
# 다리에 올라갈 수 있는 트럭 수, 다리 무게int , 다리가 견딜 수 있는 무게 int,트럭별 무게 리스트
def solution(bridge_length,weight,truck_weights):
    
    #다리를 큐로 만들기
    bridge = deque([0] * bridge_length)
    truck = deque( truck_weights)
    time = 0
     #일단 시간이 흘러야 하니까
    current = 0
    while truck:
    
    #먼저 다리에서 트럭 하나 나감
        a = bridge.popleft()
        current = current - a
        w = truck[0]
        # 무게 계산
        if current +w <= weight:
            bridge.append(w)
            truck.popleft()
            current +=w
            #만약에 못올라간다면 0 추가
        else:
           bridge.append(0)
            
        time +=1
  
    return time+bridge_length