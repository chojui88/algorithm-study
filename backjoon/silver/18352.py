from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    a,b = map(int,input().split())
    graph[a].append(b)



