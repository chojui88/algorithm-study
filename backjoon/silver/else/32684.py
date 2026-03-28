#dgist 장기 
#16개 기물, 궁 차 포 마 상 사 졸
import sys
input=sys.stdin.readline

first = list(map(int,input().split()))
second = list(map(int,input().split()))

first_score = first[0]*13 + first[1]*7 + first[2]*5 + first[3]*3 + first[4]*3 + first[5]*2
second_score = second[0]*13 + second[1]*7 + second[2]*5 + second[3]*3 + second[4]*3 + second[5]*2 + 1.5
    
if (first_score>second_score):    
    print("cocjr0208")
else:
    print("ekwoo")

