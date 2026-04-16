import sys
input = sys.stdin.readline

#영단어 순서 뒤바꾸어 같아질 수 있을떄
lst1 = list(input())
lst2 = list(input())

두 문자열에서 각 문자열의 공통된 문자열 개수 차이만큼 제거하고
lst1.sort()
lst2.sort()

count = 0
for i in lst1:
    for j in lst2:
        if i == j:
            break
    lst1.remove(i)
    count+=1

for i in lst2:
    for j in lst1:
        if i == j:
            break
    lst2.remove(i)
    count+=1
        
    
그 차이를 전부 더하기
print(count)
