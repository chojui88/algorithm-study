n,m = map(int, input().split())
result = 0

while n>=k:
    while n%k != 0:
        n -= 1
        result += 1
    n // K
    result += 1

print(result)