import sys
input = sys.stdin.readline

#주사위 던지고 코딩도 한데
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    print(f"Case {i+1}: {a+b}")