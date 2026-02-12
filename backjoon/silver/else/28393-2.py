n, k = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort()

left = 0
right = n - 1
count = 0

while left < right:
    if weight[left] + weight[right] <= k:
        count += 1
        left += 1
        right -= 1
    else:
        right -= 1

print(count)
