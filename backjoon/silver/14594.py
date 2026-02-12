def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#동아리 방 개수
n = int(input())
m = int(input())

for _ in range(m):
    a,b = map(int,input().split())
    
    for i in range(a,b):
        union_parent(i,i+1)

result = 0
