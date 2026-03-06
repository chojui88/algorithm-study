from collections import deque

def solution(priorities, location):
    list_q = []
    q = deque()
    #priorities랑 location(인덱스 + 1)이랑 같이 저장하는 큐를 만든다
    for i,j in enumerate(priorities):
        q.append((i,j))
    while q: 
    #큐에서 값을 꺼냈는데
        cur = q.popleft()
        #q.pop 값이 q의[1, 즉 우선순위의 max 값과 같다면 
        if q and cur[1] < max(x[1] for x in q):
        #출력용 list =[] 에다가 기록한다
            q.append(cur)
        #만약에 값이 작다면 다시 큐에다가 넣는데
        else:
            list_q.append(cur)
            if cur[0] == location:
                return len(list_q) 

    
