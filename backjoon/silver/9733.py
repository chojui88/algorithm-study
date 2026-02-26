import sys
work = ['Re', 'Pt', 'Cc', 'Ea', 'Tb', 'Cm', 'Ex']
bee = {}
for i in work:
    bee[i] = 0

cnt = 0
listWork = sys.stdin.read().split()  # 한 번에 읽고 공백/줄바꿈 기준으로 나누기
for i in listWork:
    if i in bee:
        bee[i] +=1
    
total = sum(bee.values())

for i in work:
    count = bee[i]
    ratio = count / total if total > 0 else 0
    print(f"{i} {count} {ratio:.2f}")

print(f"Total {total} 1.00")
