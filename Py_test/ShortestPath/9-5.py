import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int,input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

#간선 정보 = 통로의 개수
for i in range (m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q  = []
    #시작 노드로 가기 위한 최단경로는 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: #만약 q가 비어있지 않다면
        #가장 최단거리짧은 노드 정보 꺼내기
        dist,now = heapq.heappop(q) #0,start가 꺼내짐
        if distance[now] <dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리와 비교
            if cost < distance[i[0]]: #처음에 distance는 무한으로 채워져있다
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

count = 0
#도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와 최단거리
max_distance = 0
for d in distance:
    if d!= INF:
        count += 1
        max_distance = max(max_distance,d)
        
print(count,max_distance)
