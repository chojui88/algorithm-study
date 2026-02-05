import sys
input = sys.stdin.readline
#n 팀의 수 ,k 셋의 합 최소조건 , l 개인 조건
n,k,l = map(int, input().split())

team = []
for _ in range(n):
    team.append(list(map(int,input().split())))

count = 0
vip = []
for i in range(n):
    if team[i][0] >= l and team[i][1] >= l and team[i][2] >= l:
        if sum(team[i]) >= k:
            count+=1 
            vip.extend(team[i]) 
print(count)
print(*vip)