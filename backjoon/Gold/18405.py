import sys
input = sys.stdin.readline
from collections import deque

# n,k
n, k = map(int, input().split())
graph = []
target_s, target_x, target_y = map(int, input().split())

# 바이러스 정보
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    virus, s, x, y = q.popleft()

    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])
