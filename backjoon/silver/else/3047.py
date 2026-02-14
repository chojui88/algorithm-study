a,b,c = map(int,input().split())
order = input()

#세 수를 오름차순 하고 나서
numbers = [a,b,c]
numbers.sort()


result = []
for i in order:
    if i == 'A':
        result.append(numbers[0])
    elif i == 'B':
        result.append(numbers[1])
    elif i == 'C':
        result.append(numbers[2])
    
print(*result)

