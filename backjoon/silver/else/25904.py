n, x = map(int, input().split())

t = list(map(int, input().split()))
             
i = 0
while True:
    if(t[i]>=x):
        x+= 1
        i= (i+1) % n
    else:
        print(i + 1)
        break




    