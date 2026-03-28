import sys
input = sys.stdin.readline

# 양의 정수 n, 더큰 소수 p
n,p = map(int,input().split())

if n>=p:
    print (0)
else: 
    n_pac = 1

    for i in range (1,n+1):
        n_pac = i * n_pac % p

        
    print (n_pac)
#n!을 p로 나눈 나머지