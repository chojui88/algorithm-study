def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent.parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#n개의 팀, m입력된 연산 개수
n,m = map(int,input().split())
parent = [0] * (n+1)

#각각의 방이다
for i in range(n+1):
    parent[i] = i

for i in range(m):
    oper,a,b = map(int,input().split())

    if oper == 0:
        union_parent(parent,a,b)
    elif oper == 1: #둘이 같은방인가?
        if find_parent(parent,a) == find_parent(parent,b):
            print('YES')
        else:
            print('NO')
