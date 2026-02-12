#date, time, 대회 마치는 시간
d, h, m = map(int,input().split())

time = d*24*60 + h*60 + m
start = 11*24*60 + 11*60 + 11

if (time - start <0):
    print('-1')
else:
    print(time - start)
