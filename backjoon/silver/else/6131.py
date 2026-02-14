n = int(input())
cnt = 0

for j in range(1,1001):
    for i in range (j,1001):
        if(j*j + n == i*i):
            cnt+=1

print(cnt)