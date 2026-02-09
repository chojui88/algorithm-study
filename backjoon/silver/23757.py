import heapq

#n개의 선물 상자, m명의 아이들
n, m = map(int,input().split())

#각 선물상자에 들어있는 선물 개수
c = list(map(int,input().split()))
#아이들이 원하는 선물개수
w = list(map(int,input().split()))

heap = []
for i in c:
    heapq.heappush(heap,-i)

for i in range(m):
    largest = -heapq.heappop(heap)

    if largest<w[i]:
        print(0)
        exit()
        
    heapq.heappush(heap,-(largest-w[i]))

print(1)
        