n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k #정확히 k 로 나눠지는 n의 값
    result += n - target #k로 나눈 나머지 수 
    n = target #정확히 k로 나눠떨어지는 n이 됨
    
    if n < k:
        break

    result +=1
    n //=k

result += (n-1)