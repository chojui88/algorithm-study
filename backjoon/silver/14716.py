import sys
sys.setrecursionlimit(10**7)


m,n = map(int, input().split())

#1이면 글자 값이 있음
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

# 왼위,상,오위 하, 좌,하좌, 우, 하우
dx = [-1,-1,-1, 0, 0,1,1,1]
dy = [-1,0, 1, -1, 1,-1,0,1]

def dfs(x, y):
    if(x <0 or y < 0 or x >= m or y>=n):
        return False
    
    if graph[x][y] == 1:
        graph[x][y] = 0

        #대각선까지 8개방향 알아야해
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

        return True
    return False

count = 0
for i in range(m):
    for j in range(n):
        if dfs(i,j):
            count += 1
    
print(count)