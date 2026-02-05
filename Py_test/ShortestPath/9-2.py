import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
#시작 노드 번호 입력받기
start = int(input())

#각 노드 연결되어있는 노드에 대한 정보 담는 리스트 만들기
graph = [[] for i in range(n+1)]

#최단 거리 테이블 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #가장 최단거리 짧은 노드에 대해 정보 꺼내기
        dist, now = heapq.heappop(q)#거리, 노드번호 = 거리 가장 낮은것
        #현재 노드 처리된 적 있다면 무시
        if distance[now] < dist: #지금 꺼낸 거리보다 distance 최단거리가 짧다면
            continue
        #다음에 갈 노드 확인
        for i in graph[now]:
            cost = dist + i[1] #지금 경로를 경유해서 다음 경로로 가는 비용
            #현재 노드를 거쳐서, 다른 노드로 이동하는 가리가 더 짧은경우
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

#모든 노드로 가기위한 최단 거리  출력
for i in range(1,n+1):
    #도달할 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])