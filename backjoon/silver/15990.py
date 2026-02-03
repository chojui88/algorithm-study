t = int(input())
d = [[0, 0, 0] for _ in range(100001)]

queries = [int(input()) for _ in range(t)]

mod = 1000000009
d[1] = [1,0,0]
d[2] = [0, 1, 0]   # 2
d[3] = [1, 1, 1]   # 1+2, 2+1, 3

             
for i in range(4,100001):
    d[i][0] = (d[i-1][1] + d[i-1][2]) % mod
    d[i][1] = (d[i-2][0] + d[i-2][2]) % mod
    d[i][2] = (d[i-3][0] + d[i-3][1]) % mod

for n in queries:
    print((d[n][0] + d[n][1]+ d[n][2]) % mod)
    
    
