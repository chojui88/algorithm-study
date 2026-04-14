import sys
input = sys.stdin.readline

# 청소년 위해서 앱 만드는 회사
# 데이트 비용  광ㅗ로 때운다
# 광고 효과 예측

n = int(input())
for i in range(n):
    #광고 하지 않았을때 수익, 광고했을떄 수익, 광고 비용
    r,e,c = map(int(),input().split())
    if e-c > r:
        print("advertise")
    elif e-c < r:
        print("do not advertise")
    else:
        print("does not matter")


#advertise, do not advertise, does not matter
