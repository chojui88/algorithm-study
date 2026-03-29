import sys
input = sys.stdin.readline

# 돈을 조교에게 나누자!
#나 돈 나눠줘!
# 동등하게 분배
#
n, m = map(int,input().split())

print(n//m)
print(n%m)