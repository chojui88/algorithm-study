import sys

for i in sys.stdin:
    if i.strip() =="0 0":
        break
    a,b = map(int,i.split())
    print(a+b)
