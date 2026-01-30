
    
n, m = map(int,input().split())

DNA = []
for _ in range(n):
    DNA.append(input().strip())

RESULT = []

for j in range(m):
    a=t=g=c= 0
    for i in range (n):
       
        if (DNA[i][j] == 'A'):
            a +=1
        elif (DNA[i][j] == 'T'):
            t +=1
        elif (DNA[i][j] == 'G'):
            g +=1
        elif (DNA[i][j] == 'C'):
            c +=1
        
    max_cnt = max(a, c, g, t)

    if max_cnt == a:
            ch = 'A'
    elif max_cnt == c:
            ch = 'C'
    elif max_cnt == g:
            ch = 'G'
    else:
            ch = 'T'

    RESULT.append(ch)

count = 0 
for i in range (n):
    for j in range (m):
        if (DNA[i][j] != RESULT[j]):
             count+=1


print(''.join(RESULT))
print(count)



