from collections import deque

#노드, 간선
v, e = map(int,input().split())

#진입차수
indegree = [0] * (v+1)

#노드에 연결된 간선 정보
graph = [[]for i in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result = [] #알고리즘 수행 결과 리스트
    q = deque()

    #진입차수 0인 노드 큐에 삽입 - 처음 시작
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    #q가 빌떄까지 반복
    while q:
        now = q.popleft() #왼쪽 원소 꺼내기
        result.append(now)
        #해당 노드와 연결된 노드 진입차수 1 빼기
        for i in graph[now]:
            indegree[i] -=1
            #새롭게 진입차수 0이 되는 값 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i,end=' ')

topology_sort()