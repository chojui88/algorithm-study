
# 매일 다른온 입는데
# 각 종류별로 한가지 의상
# 일부 겹쳐도 의상 추가로 착용하면 다른 방법으로 사용한 것으로 계산
def solution(clothes):
    count = {}

    # 종류별 개수 세기
    for name, kind in clothes:
        count[kind] = count.get(kind, 0) + 1

    # 경우의 수 계산
    answer = 1

    for v in count.values():
        answer *= (v + 1)

    return answer - 1