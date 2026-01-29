n, m = map(int,input().split())

d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1 #현재 좌표 방문처리

#전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북 동 남 서
dx = [-1,0,1,0 ]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction] #방향에 맞게 한칸 전진
    ny = y + dy[direction]
    
    #d = 방문했는지 안했는지 , array = 바다인지 육지인지
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1 #방문한 칸 수
        turn_time = 0
        continue
    else: 
        turn_time += 1
    #네 방향 모두 갈 수 없으면 뒤로 가기
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)