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

parent = [0] * (n+1)
count = 0
#각각의 방이다
for i in range(n+1):
    parent[i] = i

for i in range(m):
    a,b=(map(int,input().split()))
    
    
    x = find_parent(parent,a)
    while x < b:
        parent[x] = x + 1
        x = find_parent(parent,x)
        

for i in range(1,n+1):
    if find_parent(parent,i) == i:
        count+=1

print(count)