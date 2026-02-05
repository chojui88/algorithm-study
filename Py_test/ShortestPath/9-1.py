import sys
input = sys.stdin.readline
INF = int(1e9)

#노드 개수, 간선 개수
n, m = map(int, input().split())
#시작 노드 번호 입력받기
start = int(input())

#노드에 연결되어있는 노드의 정보 담는 리스트
graph = [[] for i in range(n+1)]

visited = [False] * (n+1)

#최단거리 테이블
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c))

#시작점으로부터 최단거리가 가장 짧은 노드 번호 반환 , 
# 다음은 어느 노드 기준으로 할지
def get_smalliest_node():
    min_value= INF 
    index = 0 #가장 최단거리가 짧은 노드
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 #최단거리 시작 노드 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1개 노드에 대한 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smalliest_node()
        visited[now] = True

        #현재 노드에서갈 수 있는 간선을 확인한다
        for j in graph[now]:
            #지금 노드에서 다음 노드로 가는데 드는 비용 j[1]
            cost = distance[now] + j[1]
            #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

#모든 노드로 가기 위한 최단 거리  출력
for i in range(1, n+1):
    #도달할 수 없는경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    #도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])
    
