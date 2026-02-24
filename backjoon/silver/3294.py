import sys
input = sys.stdin.readline
#n번째 줄의 문서
n,k = map(int,input().split())

next = [0] * (n+1)
prev = [0] * (n+1)

for i in range(1,n+1):
    next[i] = i+1
    prev[i] = i-1

next[n] = 0
prev[1] = 0

head = 1

if pa != 0:
    next[pa] = nb
for _ in range (k):
    a,b,c = map(int,input().split())

    #구간 제거
    pa = prev[a]
    nb = next[b]

    if pa!=0:
        next[pa] = nb
    else:
        head = nb

    if nb !=0:
        prev[nb] = pa
        
    #삽입
    if c == 0:
        prev[a] = 0
        next[b] = head

        if head !=0:
            prev[head] = b
    
        head = a
    else: 
        nc = next[c]

        next[c] = a
        prev[a] = c

        next[b] = nc
        if nc != 0:
            prev[nc] = b

cur = head
for _ in range(10):
    print(cur)
    cur = next[cur]
            """
        next[prev[a]] = next[b]
        prev[next[b]] = prev[a]

    
    prev[head] = b
    head = a
    
    if c == 0:
        prev[1] = b
    next[b] = next[c]
    prev[next[c]] = b
    next[c] = a
    prev[a] = c


class Node:
     def __init__(self,data):
         self.data = data
          self.next = None
           
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

node = Node(0)
node.next = head
head = node
while node:
     if node.next is None:
         node.next = Node(4)
        break
    node = node.next """
