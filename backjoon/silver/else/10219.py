#고기 명우 고기 구워 
#h * w 칸
#격자 가득 채우는 고기
#고기 각각이 겹치지 않고 뒤집힌 상태가 되도록
'''
t = int(input())
h,w = map(int,input().split())
case = [input().rstrip() for i in range(h)]

#.rstrip() 입력받은 문자열 끝의 공백/개행 문자 제거
#input Enter 누르면 전체 문자열 반환 (개행문자 = \n)
#불판 전체를 좌우반전
for i in range(h):
    case[i] = case[i][::-1]
#슬라이싱 , 자료형에서 부분 잘라내는 방법
#swquence[start:stop:step]

for i in case:
    print(i) */
'''

count = int(input())

for j in range(count):
    h,w = map(int,input().split())
    for i in range(h):
        a = input()
        b=w-1
        while b>=0:
            print(a[b],end="")
            #end="" 줄바꿈 없이 이어서 끝냄
            b=b-1
        print()
    