n, k =map(int, input().split())
arr = list(input().strip())

count = 0
#사람 for문을 돈다
for i in range(n):  
#만약 햄버거가 있다면 먹고 flag를 1로 만든다.
    if (arr[i] == 'P'):
        for j in range(max(0, i-k), min(n,i+k+1)):
            if (arr[j] == 'H'):
                count+=1
                arr[j]= 'X'
                break

print(count)