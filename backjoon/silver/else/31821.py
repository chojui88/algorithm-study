import sys
input = sys.stdin.readline

#번호 부여된 여러 코너

n = int(input())
lstA = [int(input()) for _ in range(n)]


m = int(input())
lstB = []
for i in range(m):
    lstB.append(int(input()))

total = 0
for i in range(m):
    menu = lstB[i]
    total+=lstA[menu-1]
    #인덱스 반복문 안에서 쓰지말기 ㅜ
    #학생이 원하는 메뉴의 값 = lstA의 인덱스
   
#금액의 총액
print (total)