#덕후, 어리고 티어 높을수록 덕후, 덕후력 자신의 덕후력 60

import sys
input = sys.stdin.readline

a, t =map(int,input().split())

p = 10 + 2*(25-a+t)

if p<0:
    print(0)
else:   
    print(p)
