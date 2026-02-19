import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#n세로 m가로
n,m = map(int,input().split())
data = [list(map(int, input().split())) for _ in range(n)]
temp = [[0]*m for _ in range(n)] #벽 세훈후
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#DFS 함수 만들기
def virus(x,y):   
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <0 or ny < 0 or nx >= n or ny >= m:
            continue

        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx,ny)

#안전 영역 크기 계산 함수
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score +=1
    return score

result = 0
#여기서 바이러스가 퍼지는것을 막는 벽을 3개 조합
#dfs로 계산하는데 count 현재까지 세운 벽 개수
def dfs(count):
    global result

#울타리가 3개면 바이러스 파졌을떄 생존된 0 값 계산하고, 최대값인 경우 찾기
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        #바이러스 전파하고
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        #최대값 계산
        result = max(result,get_score())
        return
#3개가 아니면 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count+=1
                dfs(count)
                data[i][j]= 0
                count -= 1

dfs(0)
print(result)

