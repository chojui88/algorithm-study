#distracted so somethig (산만한)
# put periods , end of sentences
# if period is not already present

import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    s = input().strip()
    if s[-1] != '.':
        s+= '.'
        # 문자열은 리스트가 아니라 append 못쓴다
    lst.append(s)

for i in lst:
    print (i)
