from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    #b는 연결되는 간선의 노드
    a,b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

#처음의 출발도시정보
q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now]+1
            q.append(next)

check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True           

if check == False:
    print(-1)
