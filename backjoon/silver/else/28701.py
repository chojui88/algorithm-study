import sys
input = sys.stdin.readline

#1+n , 1+N 세제곱의 함

n = int(input())

total = 0
for i in range(1, n+1):
    total += i
print(total)
print(total * total)

three = 0
for i in range(1,n+1):
    three += i * i * i

print(three)
