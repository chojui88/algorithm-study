#DFS 문제
#세로 n 가로 m
n, m = map(int,input().split())

#2차원 리스트 맵 정보
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    #주어진 범위 벗어나면 종료
    if x<= -1 or x >=n or y<= -1 or y >=m:
        return False
    #현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

#모든 위치에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result +=1

print(result)