#고양이 마리수, 친구들 버틸 수 있는 무게
n, k = map(int,input().split())
weight = list(map(int,input().split()))

weight.sort()
for i in range(n):
    if (weight[i]>k):
        weight.pop(i)
count = 0
i = 0
while(i<=n-i-1):
    if (weight[i] == weight[n-i-1]):
        if(weight[i] <= k):
            count +=1
            break
    if (weight[i]+weight[n-1-i] <= k):
        count +=1
    i+=1   
    

print(count)