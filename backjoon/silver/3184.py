import sys
sys.setrecursionlimit(10**7)

#행, 열
r, c = map(int,input().split())

yard = []
for i in range(r):
    yard.append(list(input().strip()))

def dfs(x,y):
    #주어진 범위 벗어나면 종료
    if x< 0 or x >=r or y<0 or y >=c:
        return 0,0
    
    if  yard[x][y] == '#':
        return 0,0
       
    sheep = 0
    wolf = 0

    if yard[x][y] == 'o':
        sheep +=1
    elif yard[x][y] == 'v':
        wolf +=1

    yard[x][y] = '#'

    s1, w1 = dfs(x-1,y)
    s2, w2 = dfs(x,y-1)
    s3, w3 =    dfs(x+1,y)
    s4, w4 =     dfs(x,y+1)

    sheep += s1 + s2 + s3 + s4
    wolf  += w1 + w2 + w3 + w4
    
    return sheep,wolf

total_sheep = 0
total_wolf = 0

for i in range(r):
    for j in range(c):
        if yard[i][j] != '#':
            s, w = dfs(i,j)
            if s > w:
                total_sheep += s
            else:
                total_wolf += w

print(total_sheep,total_wolf)