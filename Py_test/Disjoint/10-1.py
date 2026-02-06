#특정 원소가 속한 집합
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 떄까지 재귀적으로 호출
    if parent[x] !=x:
        return find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

#노드의 개수와 간선의 개수 입력받기

