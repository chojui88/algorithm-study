n,m = map(int, input().split())

result = 0

for i in range(m):
    data = list(map(int, input().split()))
    #현재 줄에서 가장 작은 수 
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    
    result = max(result, min_value)

print(result)
