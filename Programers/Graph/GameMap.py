from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    if maps[0][0] == 0:
        return -1
    
    dx = (-1,1,0,0)
    dy = (0,0,-1,1)

    #현재 있는 좌표
    q = deque()
    q.append((0,0))

    while q:
        x,y = q.popleft()

    #한 칸씩 이동하면서 만약 1이면 이동하고 0으로    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >=n or ny>=m or nx<0 or ny<0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1
                q.append((nx,ny))


        #만약 마지막 최종 좌표가 5,5에 도달하지 못했다면
    if maps[n-1][m-1] == 1:
        return -1
    
    return maps[n-1][m-1]