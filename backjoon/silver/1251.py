
a = list(input())
b = a.copy()
b.sort() 
index1 = a.index(b[0])
index2 = a.index(b[1])
first = []
second = []
third = []
#알파벳 순으로 가장 빠른 단어 찾아서 그 앞뒤로 list 저장
for i in range(0,index1+1):
    first.append(a[i])
for i in range(index1+1,index2+1):
    second.append(a[i])
for i in range(index2+1,len(a)):
    third.append(a[i])


first = first[::-1]
second = second[::-1]
third = third[::-1]

print(''.join(first+second+third))