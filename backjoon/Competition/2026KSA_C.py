import sys
input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1, N):
        a = A[i]
        b = A[j]
        lcm = a * b // gcd(a, b)

        if not is_prime(lcm):
            print("YES")
            print(2)
            print(a, b)
            sys.exit()

print("NO")