#c로 시작하는 문자열을 새 대회이름으로
import sys
input = sys.stdin.readline

n = int(input())
lst = []
count = 0
for i in range (n):
    lst.append(input().strip())
    if lst[i].startswith("C"):
        count+=1

print (count)
#문자열의 개수